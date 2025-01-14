import json
from typing import Literal, Dict, List, Tuple
from uuid import uuid4
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry
from tqdm import tqdm
from requests import HTTPError
from hive.decorators import ratelimiter, refresh, paginate, warmstart
from hive.exceptions import UnauthorizedException
from hive.infrastrucure_keys import Keys
import warnings
import gc


FORCE_STATUS = [429, 500, 502, 503, 504]
METHODS = ["HEAD", "GET", "OPTIONS", "POST"]


def get_session():
    """
    Add retry logic and policies about methods and statuses for requests
    """
    ss = requests.Session()
    retry_strategy = Retry(connect=3, total=3, status_forcelist=FORCE_STATUS, allowed_methods=METHODS)
    ss.mount('https://', HTTPAdapter(max_retries=retry_strategy))
    ss.mount('http://', HTTPAdapter(max_retries=retry_strategy))
    return ss


class ApiManager:
    """
    Class to interact with Xautomata REST APIs.

    Args:
        root (str): root uri
        user (str): username
        password (str): password

    Attributes:
        credentials (tuple): (user, password), tupla che estrae le credenziali da server_endpoint
        token (str): token di autenticazione delle api
    """

    def __init__(self, root, user, password):
        self.root = root.rstrip('/')
        self.credentials = (user, password)
        self.token = 'UNDEFINED'
        self.authenticate()
        self._get_only = False

    ################################################################################################################

    def authenticate(self):
        """
        Metodo che compie l'autenticazione e ottiene il token per la sessione
        """
        user, password = self.credentials
        auth_date = {"grant_type": "password", "username": user, "password": password}
        response = get_session().post(f'{self.root}/login/access-token', auth_date)
        response.raise_for_status()
        self.token = json.loads(response.content.decode('utf-8'))['access_token']

    def openapi(self):
        """metodo che restituisce gli schema degli end point"""
        response = get_session().request('GET', url=f'{self.root}/openapi.js',
                                         headers={'Authorization': f'Bearer {self.token}'})
        data = json.loads(response.content[15:].decode('utf-8'))
        return data

    @refresh
    def execute(self, mode: Literal['GET', 'POST', 'DELETE', 'PUT'], path, headers: Dict = None, single_page: bool = False,
                page_size: int = 5000, payload: Dict or List[dict] = None, warm_start: bool = False,
                params: Dict = None, **kwargs):
        """
        metodo che chiama la API richiesta nella modalita richiesta.

        Args:
            mode (['GET', 'POST']): get o post
            path (str): url dell'api
            headers (dict, optional): dict of headers. Default to None.
            payload (dict or list[dict], optional): contenuto della richiesta, valido solo per la post. Default to False.
            warm_start (bool, optional): activates the warm start mode. Defailt to False.
            params (dict, optional): skip, limit, count, like, sort_by, null_fileds, join. Default to None
                - skip (int, optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0.
                - limit (int, optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000.
                - count (bool, optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.
                - like (bool, optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True.
                - sort_by (str, optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "".
                - null_fileds (str, optional): Stringa separata da virgole di campi di cui si vuole rimuovere, o imporre, un valore nullo nel result set. Esempio "campo:nullable". Default to "".
                - join (bool, optional): Se join = true, ogni riga restituita conterrà chiavi aggiuntive che fanno riferimento ad altre entità, con cui la riga ha relazioni 1:1. Default to False
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.

            **kwargs: additional parameters for the API

        Returns:
            response (list): risposta dell'API selezionata
        """

        bulk = True if isinstance(payload, list) else False
        bulk = True if 'bulk' in path else bulk  # verifico dalla path se è una api bulk
        bulk = True if path == '/metric_ingest/' else bulk  # il metric_ingest e' una bulk ma non compare nel nome
        bulk = True if path == '/probes_log_ingest/' else bulk  # il metric_ingest e' una bulk ma non compare nel nome
        read = True if 'read' in path else False  # verifico dalla path se è una api get, valido solo per le bulk
        query = True if 'query' in path else False  # verifico dalla path se è una api get, valido solo per le bulk
        query = True if path == '/last_status/' and mode == 'POST' else query  # caso specifico della last_status che non ha features riconoscibili

        authentication = {'Authorization': f'Bearer {self.token}'}
        _headers_ = headers.copy().update(authentication) if headers else authentication

        _payload_ = payload.copy() if payload is not None else None  # va lasciato in questa dicitura perche in se si usa if payload quando arriva un {} viene considerato False
        _params_ = params.copy() if params else {}

        _params_['skip'] = _params_.get('skip', 0)
        _params_['limit'] = _params_.get('limit', 1_000_000)
        _params_['count'] = _params_.get('count', False)

        if _params_['count']:
            single_page = True
            warm_start = False

        if mode == 'POST' or mode == 'DELETE' or mode == 'PUT':

            # il controllo qui impedisce di fare chiamate se in modalita POST DELETE PUT se in modalita test,
            # con l'eccezione della presenza della parola read nel path che indica una bulk in lettura
            if self._get_only and not(read and bulk) and not query:
                raise ValueError('you are trying to access a not get_only API')

            # tutto quello che non è bulk e query gli viene impedito di paginare
            # mentre le bulk e query post/delete possono paginare come le get
            if not bulk and not query:
                single_page = True
                warm_start = False
                _params_.pop('count')

            # le bulk post/delete non devono poter fare warm_start mai, se viene impostato a True è per errore e qui viene forzato a False
            if bulk and not read: warm_start = False

        url = f'{self.root}{path}'

        @warmstart(active=warm_start, args_ex=[2], verbose=False)
        @paginate(single_page=single_page, page_size=page_size, skip=_params_['skip'], limit=_params_['limit'], bulk=bulk)
        @ratelimiter
        def run_request(_mode, _url, _headers, _payload, _params, **_kwargs):
            response = get_session().request(_mode, url=_url, json=_payload, params=_params, headers=_headers, **_kwargs)
            if response.status_code == 401: raise UnauthorizedException
            if response.status_code != 200:
                print('-' * 50)
                print('error message:')
                # if 'message' in list(response.json().keys()):
                #     print(response.json()['message'])
                # elif 'detail' in list(response.json().keys()):
                #     print(response.json()['detail'][0])
                # else:
                #     print(response.json())
                print(response.json())
                print('-' * 50)
            response.raise_for_status()

            if response.status_code == 200 and _params.get('count', False):
                num_items = response.headers.get('x-num-items', 'count not found')
                return response.json(), num_items

            return response.json()

        return run_request(mode, url, _headers_, _payload_, _params_, **kwargs)

    def get_post(self, url_get: str, url_post: str = None, get_params: dict = None, post_params: dict = None,
                 prefix: str = None, add_post_params: dict = None, silence_put: bool = False) -> Tuple[str, int, int, int]:
        """
        metodo che prova a fare una get con i parametri selezionati, se la get fallisce perche mancavano i dati
        richiesti allora viene fatta una post per creare il dato cercato

        Args:
            url_get (str): url dell'api di get
            url_post (str, optional): url dell'api di post, se non viene fornito nessun url, viene usato quello della
                get. Default to None.
            get_params (dict, optional): parametri della api di get. Default to None.
            post_params (dict, optional): parametri della api di post. Default to None.
            prefix (str, optional): nel caso la get fornisse un risposta con piu elementi, il prefix rappresenta la
                parte del nome che ci si aspetta sia presente nell'elemento da usare. Default to None.
            add_post_params (dict, optional): parametri della post, put che non rientrano nel payload
            silence_put (bool, optional): se a True le put non vengono fatte.

        Returns:
            uuid (str): uuid dell'oggetto richiesto
            get_count (int): 1 se il metodo e' risultato in una get e 0 se e' risultato in una post
            post_count (int): 1 se il metodo e' risutltato in una post e 0 se e' risultato in una get
        """
        if get_params is None: get_params = {}
        if post_params is None: post_params = {}
        url_post = url_get if url_post is None else url_post
        get_count, post_count, put_count = 0, 0, 0

        # se uno passa lo stesso dizionario sia per get che per post, con la seguente riga impedisce di applicare le modifiche fatte alla get anche alla post
        get_params = get_params.copy()
        post_params = post_params.copy()

        # a meno di definizioni diverse le chiamate get vengono sempre fatte in like = False
        get_params['like'] = get_params.get('like', False)

        try:
            # il primo tentativo e' di chiedere l'oggetto con una get
            response_content = self.execute('GET', url_get, params=get_params)
            # se e' stato inserito un prefisso questo viene usato per selezionare solo la riposta con quel prefisso
            if prefix is not None:
                response_content = [g for g in response_content if g['name'].startswith(prefix)]
            # se la risposta e' un vettore a lunghezza 0 allora viene postato un elemento con le caratteristiche cercate
            if len(response_content) == 0:
                # in fase di testing non viene postato nulla
                if self._get_only:
                    response_content = [{'uuid': 'F4FF'+str(uuid4())[4:]}]
                else:
                    # viene postato l'elemento con le caratteristiche richieste
                    response_content = self.execute('POST', url_post, payload=post_params, params=add_post_params)
                post_count = 1
            else:
                # se post_params è vuoto o se siamo in modalita silence, la put non viene provata
                if post_params and not silence_put:
                    # se l'oggetto esiste controllo le sue chiavi
                    for chiave in post_params:  # ciclo sulle chiavi dei parametri postabili
                        # se incontro un parametro di quelli decisi per il post che è abbinato ad un valore diverso rispetto
                        # a quello che è nella risposta, allora faccio una put
                        if post_params[chiave] != response_content[0][chiave]:
                            # estraggo lo uuid dell'oggetto
                            uuid = response_content[0]['uuid']
                            # compio la put con il nuovo set di parametri
                            if not self._get_only:
                                response_content = self.execute('PUT', url_post+uuid, payload=post_params, params=add_post_params)
                            # alzo il contatore delle put
                            put_count = 1
                            # se ho fatto una put non continuo con il ciclo
                            break
                # se ho fatto una put non alzo anche il contatore delle get
                get_count = 1 if put_count == 0 else 0

        # se la risposta alla prima get era un errore questo viene catturato qui
        except HTTPError as e:
            # se l'errore era un 404 o un 405 significa che l'oggetto non esiste e viene quindi postato come sopra
            if e.response.status_code in [404, 405]:
                if self._get_only:
                    response_content = [{'uuid': 'F4FF'+str(uuid4())[4:]}]
                else:
                    response_content = self.execute('POST', url_post, payload=post_params)
                post_count = 1
            else:
                # ogni altro errore viene restituito come tale
                print(e.response.json())
                raise ValueError(e)

        return response_content[0]['uuid'], get_count, post_count, put_count

    def get_post_bulk(self, post_params: List[dict], url_get: str, url_post: str = None, url_put: str = None,
                      add_get_params: dict = None, add_post_params: dict = None, silence_put: bool = False,
                      page_size: int = 5000) -> Tuple[List[str], int, int, int]:
        """
        metodo che prova a fare una get con i parametri selezionati, se la get fallisce perche mancavano i dati
        richiesti allora viene fatta una post per creare il dato cercato

        Args:
            post_params (list[dict], optional): parametri della api di post. Default to None.
            url_get (str): url dell'api di get
            url_post (str, optional): url dell'api di post, se non viene fornito nessun url, viene usato quello della
                get. Default to None.
            url_put (str): url dell'api di put
            add_get_params (dict, optional): parametri della get che non rientrano nel payload. Default to None.
            add_post_params (dict, optional): parametri della post, put che non rientrano nel payload
            silence_put (bool, optional): se a True le put non vengono fatte.
            page_size (int, optional): numero di elementi che vengono caricati in un unica chiamata

        Returns:
            uuid (list[str]): lista di tutti gli uuid degli oggetti richiesti
            get_count (int): 1 se il metodo e' risultato in una get e 0 se e' risultato in una post
            post_count (int): 1 se il metodo e' risutltato in una post e 0 se e' risultato in una get
        """

        # se viene dato il solo elemento dell'url, questo viene convertito nella sua versione bulk
        if 'bulk/read' not in url_get: url_get = '/' + url_get.lstrip('/').rstrip('/') + '/bulk/read_by/'
        else:                          url_get = '/' + url_get.lstrip('/').rstrip('/') + '/'

        # inizializzo url post se non viene passato
        if url_post is None: url_post = url_get.split('bulk/read')[0]
        if 'bulk/create' not in url_post: url_post = '/' + url_post.lstrip('/').rstrip('/') + '/bulk/create/'
        else:                             url_post = '/' + url_post.lstrip('/').rstrip('/') + '/'

        # inizializzo url put se non viene passato
        url_put = url_get.split('bulk')[0] if url_put is None else url_put
        url_put = '/' + url_put.lstrip('/').rstrip('/') + '/'

        method = url_get.split('/')[1]

        get_count, post_count, put_count = 0, 0, 0

        # se uno passa lo stesso dizionario sia per get che per post, con la seguente riga impedisce di applicare le modifiche fatte alla get anche alla post
        post_params = post_params.copy()

        # ottengo le chiavi univoche da un dizionario
        chiavi_dict = {'customers': Keys.customer_keys, 'virtual_domains': Keys.virtual_domain_keys, 'sites': Keys.site_keys,
                       'groups': Keys.group_keys, 'objects': Keys.object_keys, 'metric_types': Keys.metric_type_keys,
                       'metrics': Keys.metric_keys, 'services': Keys.service_keys}
        chiavi = chiavi_dict[method]['univocal']

        # si chiedono tutti gli oggetti in con la get e si ottiene una lista di riposta con gli uuid di quelli trovati e dei None per quelli non trovati
        # non serve filtrare le richieste alla get con le sole chiavi primarie perche l'API fa il filtro internamente
        response_content_temp = self.execute('POST', url_get, payload=post_params, params=add_get_params, page_size=page_size)  # questo metodo puo introdurre dei duplicati se lo stesso oggetto viene chiesto piu volte e si sta paginando

        # creo un dizionario con gli elementi primari come chiavi e le rispote come valori
        response_content_temp_dict = dict()
        for cont in response_content_temp:
            # creo le chiavi con il risultato dei valori degli elementi primari
            chiave = tuple(cont[k] for k in chiavi)
            # abbino a questa chiave il contenuto della risposta
            response_content_temp_dict[chiave] = cont

        # precrea una lista vuota
        response_content = [None for _ in range(len(post_params))]
        # seleziono dalla lista postata gli indici degli elementi che hanno dato un None come risultato dalla get
        id_element_to_post, id_element_getted, key_post = [], [], []

        # creo un dizionario con gli elementi primari come chiavi e le rispote come valori
        post_params_dict = dict()
        # cicla su tutti gli elementi e discrimino quelli che sono gia stati ottenuti da quelli che mancano
        for i, ele in enumerate(post_params):
            # creo le chiavi con il risultato dei valori degli elementi primari
            chiave = tuple(ele[k] for k in chiavi)
            # abbino a questa chiave il contenuto della risposta
            post_params_dict[chiave] = ele

            # vado a cercare nella risposta se presente la chiave cercata, in caso positivo inserisco quel valore come elemento del vettore risposte
            # questo mi garantisce di mantenere lo stesso ordine delle richieste
            # se una richiesta genera piu risposte viene considerata solo l'ultima
            # se una richiesta non genera nessuna risposta viene abbinato il None
            # se vengono fatte piu richieste uguali vengono abbinati sempre gli stessi risultati tutte le volte che sono stati chiesti
            # a senconda se il responce e' None o meno popolo un vettore diverso dell'incide
            if chiave in response_content_temp_dict:
                response_content[i] = response_content_temp_dict[chiave]
                id_element_getted.append(i)
            else:
                response_content[i] = chiave
                id_element_to_post.append(i)
                # mi creo una lista che contiene le chiavi primarie degli oggetti da postare
                key_post.append(tuple(ele[k] for k in chiavi))

        # ottendo le chiavi univoche per postare gli elementi, eliminando eventuali ripetizioni
        key_post = set(key_post)
        # il numero delle post sono tutti gli elementi che non sono tornati da una get
        post_count = len(key_post)

        ###################################################
        put_count = self._put_cicle(add_post_params, chiavi, post_params_dict, put_count, response_content_temp_dict, silence_put, url_put)
        # il numero delle get reali sono il numero di chiavi uniche presenti nella riposta delle get, meno quelli su cui e' stata fatta una put
        get_count = len(response_content_temp_dict) - put_count
        ###################################################

        # prese le chiavi univoche degli elementi da postare, vengono recuperati gli oggetti da postare dal dizionario dei parametri da postare
        element_to_post = [post_params_dict[id_key] for id_key in key_post]

        # faccio la post di tutti gli elementi che hanno dato None nella get
        # se in modalita test genero gli uuid
        if len(element_to_post) > 0:
            if self._get_only: response_content_post = ['F4FF' + str(uuid4())[4:] for _ in range(len(element_to_post))]
            else:
                response_content_post_raw = self.execute('POST', url_post, payload=element_to_post, params=add_post_params,
                                                         page_size=page_size)
                response_content_post = [response_content_post_ele['uuids'] for response_content_post_ele in response_content_post_raw]
                response_content_post = [item for sublist in response_content_post for item in sublist]

            post_to_key_res_dict = dict()
            for i, id_key in enumerate(key_post):
                post_to_key_res_dict[id_key] = response_content_post[i]

            # inserisco i nuovi uuid trovati nella risposta originale
            for i, _id in enumerate(id_element_to_post):
                chiave = response_content[_id]
                response_content[_id] = {'uuid': post_to_key_res_dict[chiave]}

        # seleziono dalla lista postata gli indici degli elementi che hanno dato un None come risultato dalla get
        uuid_res = []
        none_count = 0
        for val in response_content:
            if val is None:
                uuid_res.append(val)
                none_count += 1
            else:
                uuid_res.append(val['uuid'])

        if none_count > 0:
            warnings.warn(f'{none_count} elements have not been matched with a uuid and can be found as None in the resutl list')

        return uuid_res, get_count, post_count, put_count

    def _put_cicle(self, add_post_params, chiavi, post_params_dict, put_count, response_content_temp_dict, silence_put, url_put):
        # se post_params è vuoto o se siamo in modalita silence, la put non viene provata
        if not silence_put:
            # ciclo sulla risposta della get con i soli oggetti trovati dalla get
            for res_get_i in response_content_temp_dict:
                # seleziono l'iesimo elemento del dizionario delle rispote get
                # non uso il vettore delle risposte perche se la risposta viene paginata rischio di avere dei duplicati, mentre con il dizionario della risposta stessa non puo succedere
                res_get = response_content_temp_dict[res_get_i]

                # creo le chiavi con il risultato dei valori degli elementi primari dentro alle risposte ottenute
                chiave = tuple(res_get[k] for k in chiavi)

                # se l'oggetto esiste controllo le sue chiavi
                for chiave_getted in res_get:  # ciclo sulle chiavi dei parametri ottenuti

                    # se incontro un parametro di quelli decisi per il post che è abbinato ad un valore diverso rispetto
                    # a quello che è nella risposta, allora faccio una put

                    # vado a prendere il valore delle post che combacia con il risultato ottenuto dalle get
                    # la chiave viene chiesta con il metodo get su post_params perche non necessariamente i parametri data dall'utente hanno tutte le chiavi
                    if res_get[chiave_getted] != post_params_dict[chiave].get(chiave_getted, res_get[chiave_getted]):

                        # estraggo lo uuid dell'oggetto
                        uuid = res_get['uuid']
                        # compio la put con il nuovo set di parametri
                        # la put va a modificare il dato sul db ma non mi serve che venga poi inserito il valore nello script
                        if not self._get_only: self.execute('PUT', url_put + uuid, payload=post_params_dict[chiave], params=add_post_params)
                        # alzo il contatore delle put e riduco le get
                        put_count += 1
                        break
        return put_count


def handling_single_page_methods(kwargs, params):
    """
    metodo per gestire gli kwargs e params dei metodi il cui single_page deve essere forzato a True

    Args:
        kwargs: kwargs
        params: params

    Returns: kwargs, params
    """
    kwargs['single_page'] = True
    if 'single_page' in list(params.keys()): params.pop('single_page')
    if 'page_size' in list(params.keys()): params.pop('page_size')
    return kwargs, params


# gli import vengono messi qui per evitare una parziale import di api.py
# hive imports start
from hive.cookbook.acl_docs import AclDocs
from hive.cookbook.acl_overrides import AclOverrides
from hive.cookbook.analytics import Analytics
from hive.cookbook.anomalies import Anomalies
from hive.cookbook.calendars import Calendars
from hive.cookbook.contacts import Contacts
from hive.cookbook.customers import Customers
from hive.cookbook.dashboards import Dashboards
from hive.cookbook.dispatchers import Dispatchers
from hive.cookbook.downtimes import Downtimes
from hive.cookbook.external_tickets import ExternalTickets
from hive.cookbook.firmware_updates import FirmwareUpdates
from hive.cookbook.groups import Groups
from hive.cookbook.metric_ingest import MetricIngest
from hive.cookbook.last_status import LastStatus
from hive.cookbook.tree_hierarchy import TreeHierarchy
from hive.cookbook.login import Login
from hive.cookbook.messages import Messages
from hive.cookbook.metrics import Metrics
from hive.cookbook.probes_log_ingest import ProbesLogIngest
from hive.cookbook.metric_types import MetricTypes
from hive.cookbook.notification_providers import NotificationProviders
from hive.cookbook.notification_provider_types import NotificationProviderTypes
from hive.cookbook.objects import Objects
from hive.cookbook.opening_reasons import OpeningReasons
from hive.cookbook.probes import Probes
from hive.cookbook.probe_types import ProbeTypes
from hive.cookbook.profile_topics import ProfileTopics
from hive.cookbook.reason_for_closure import ReasonForClosure
from hive.cookbook.retention_rules import RetentionRules
from hive.cookbook.schedules import Schedules
from hive.cookbook.services import Services
from hive.cookbook.sites import Sites
from hive.cookbook.ts_cost_azure_raw import TsCostAzureRaw
from hive.cookbook.ts_cost_management import TsCostManagement
from hive.cookbook.ts_metric_status import TsMetricStatus
from hive.cookbook.ts_metric_value import TsMetricValue
from hive.cookbook.ts_ntop_flows import TsNtopFlows
from hive.cookbook.ts_service_status import TsServiceStatus
from hive.cookbook.ts_service_value import TsServiceValue
from hive.cookbook.users import Users
from hive.cookbook.virtual_domains import VirtualDomains
from hive.cookbook.widgets import Widgets
from hive.cookbook.webhooks import Webhooks
from hive.cookbook.widget_groups import WidgetGroups
# hive imports stop


class XautomataApi(AclDocs, AclOverrides, Analytics, Anomalies, Calendars, Contacts, Customers, Dashboards, Dispatchers, Downtimes, ExternalTickets, FirmwareUpdates, Groups, MetricIngest, LastStatus, TreeHierarchy, Login, Messages, Metrics, ProbesLogIngest, MetricTypes, NotificationProviders, NotificationProviderTypes, Objects, OpeningReasons, Probes, ProbeTypes, ProfileTopics, ReasonForClosure, RetentionRules, Schedules, Services, Sites, TsCostAzureRaw, TsCostManagement, TsMetricStatus, TsMetricValue, TsNtopFlows, TsServiceStatus, TsServiceValue, Users, VirtualDomains, Widgets, Webhooks, WidgetGroups):
    """
    Class with each specific API, based on the ApiManager Class created for a more general interaction with Xautomata API
    """

    active_items = {
        "customer_status": "A",
        "site_status": "A",
        "group_status": "A",
        "object_status": "A",
        "metric_type_status": "A",
        "metric_status": "A"
    }

    active_items_bulk = {
        "customer_status": ["A"],
        "site_status": ["A"],
        "group_status": ["A"],
        "object_status": ["A"],
        "metric_type_status": ["A"],
        "metric_status": ["A"]
    }

    @staticmethod
    def multi_method(method, name_to_cicle: str, multi_uuid: list, single_page: bool = False, page_size: int = 5000,
                     warm_start: bool = False, position: int = 0,  kwargs: dict = None, **params):
        """
        metodo generico per iterare un metodo selezionato su una lista di parametri scelti.

        Args:
            method: metodo di XautomataApi
            name_to_cicle (str): nome dell'argomento del metodo scelto su cui iterare
            multi_uuid (list): lista di valori su cui iterare
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            position (int, optional): posizione della barra di caricamento. Default to 0.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API

        Returns: list

        """

        @warmstart(active=warm_start, verbose=False, kwargs_ex=['_method'])
        def run_multi(method_name, _method, _name_to_cicle, _multi_uuid, _single_page, _page_size, _kwargs, **_params):
            # method_name e' correttamente non usato, serve come chiave da usare nel warmstart che riconosce cosi se
            # e' cambiato il metodo usato
            _response = []
            pbar_uuids = tqdm(_multi_uuid, position=position, leave=True, ascii=True, unit=_name_to_cicle)
            for uuid in pbar_uuids:
                temp_response = _method(**{_name_to_cicle: uuid}, single_page=_single_page, page_size=_page_size,
                                        warm_start=False, kwargs=_kwargs, **_params)
                _response += temp_response
                del temp_response
                gc.collect()
            return _response

        response = run_multi(method.__name__, _method=method, _name_to_cicle=name_to_cicle, _multi_uuid=multi_uuid,
                             _single_page=single_page, _page_size=page_size, _kwargs=kwargs, **params)

        return response

    @staticmethod
    def multi_method_put(method, multi_uuid: list, position: int = 0,  kwargs: dict = None, **payload):
        """
        metodo generico per iterare un metodo selezionato su una lista di parametri scelti.

        Args:
            method: metodo di XautomataApi
            multi_uuid (list): lista di valori su cui iterare
            position (int, optional): posizione della barra di caricamento. Default to 0.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Returns: list

        """

        response = []
        pbar_uuids = tqdm(multi_uuid, position=position, leave=True, ascii=True, unit=' uuids')
        for uuid in pbar_uuids:
            temp_response = method(uuid=uuid, kwargs=kwargs, **payload)
            response += temp_response
            del temp_response
            gc.collect()

        return response

####
    def dispatecher(self, uuids, types='metric'):
        code = ''
        app_name = ''
        name_caledar = ''

        # notification provider types
        params = {'code': code, 'json_schema': {}}
        uuid_npt, _, _, _ = self.get_post(url_get='/notification_provider_types/', get_params=params, post_params=params)

        # notification providers
        params = {
            "uuid_notification_provider_type": uuid_npt,
            "app_name": app_name,
            "endpoint": {}
        }
        uuid_np, _, _, _ = self.get_post(url_get='/notification_providers/', get_params=params, post_params=params)

        # messages
        params = {
            "code": "string",
            "description": "string",
            "mask": "string",
            "mask_mime_type": "string"
        }
        uuid_m, _, _, _ = self.get_post(url_get='/messages/', get_params=params, post_params=params)

        # calendar
        # chiedi un calendar per nome
        # se passi un json post_put del calender in json
        uuid_calendar = self.execute(mode='GET', path='/calendar/', params={'name': name_caledar, 'limit': 1})[0]

        # dispatcher
        params = {
          "uuid_notification_provider": uuid_npt,
          "uuid_calendar": uuid_calendar,
          "uuid_message": uuid_m,
          "code": "string",
          "description": "string",
          "delay": 0,
          "status": "s",
          "country": "st",
          "state_province": "string",
          "data_profile": [
            "string"
          ]
        }
        uuid_d, _, _, _ = self.get_post(url_get='/dispatcehrs/', get_params=params, post_params=params)

        # COLLEGAMENTO
        # lista degli uuid degli oggetti da legare a questo dispacter
        for uuid in uuids:
            if types == 'metric':
                self.execute(mode='POST', path=f'/dispatcehrs/{uuid_d}/metrics{uuid}')
            else:
                raise NotImplementedError
