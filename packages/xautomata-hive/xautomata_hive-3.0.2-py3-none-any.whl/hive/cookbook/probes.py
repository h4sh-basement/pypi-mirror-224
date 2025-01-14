from hive.api import ApiManager, handling_single_page_methods


class Probes(ApiManager):
    """Class that handles all the XAutomata probes APIs"""

    def probes(self, warm_start: bool = False, single_page: bool = False,
        page_size: int = 5000, kwargs: dict = None, **params) -> list:
        """Read Probes
        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            sort_by (string optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "". - parameter
            null_fields (string optional): additional filter - parameter
            uuid_virtual_domain (string optional): additional filter - parameter
            uuid_probe_type (string optional): additional filter - parameter
            uuid_host (string optional): additional filter - parameter
            name (string optional): additional filter - parameter
            description (string optional): additional filter - parameter
            notes (string optional): additional filter - parameter
            status (string optional): additional filter - parameter
            extract_severity (boolean optional): Se True nella risposta e' anche presente la severita, Default to False. - parameter
            skip (integer optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (integer optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
            like (boolean optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True. - parameter
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('GET', path=f'/probes/', single_page=
            single_page, page_size=page_size, warm_start=warm_start, params
            =params, **kwargs)
        return response

    def probes_create(self, kwargs: dict = None, **payload) -> list:
        """Create Probe
        Args:
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.
        Keyword Args:
            uuid_virtual_domain (string required): additional filter - payload
            uuid_probe_type (string required): additional filter - payload
            uuid_host (string required): additional filter - payload
            name (string required): additional filter - payload
            description (string optional): additional filter - payload
            data_profile (array object required): additional filter - payload
            notes (string optional): additional filter - payload
            status (string required): additional filter - payload
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=f'/probes/', payload=payload,
            **kwargs)
        return response

    def probe(self, uuid: str, warm_start: bool = False,
        kwargs: dict = None, **params) -> list:
        """Read Probe
        Args:
            uuid (str, required): uuid
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        response = self.execute('GET', path=f'/probes/{uuid}', warm_start=
            warm_start, params=params, **kwargs)
        return response

    def probes_put(self, uuid: str, kwargs: dict = None, **payload) -> list:
        """Update Probe
        Args:
            uuid (str, required): uuid
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.
        Keyword Args:
            uuid_virtual_domain (string optional): additional filter - payload
            uuid_probe_type (string optional): additional filter - payload
            uuid_host (string optional): additional filter - payload
            name (string optional): additional filter - payload
            description (string optional): additional filter - payload
            data_profile (array object optional): additional filter - payload
            notes (string optional): additional filter - payload
            status (string optional): additional filter - payload
            last_seen (string optional): additional filter - payload
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('PUT', path=f'/probes/{uuid}', payload=
            payload, **kwargs)
        return response

    def probes_delete(self, uuid: str, kwargs: dict = None) -> list:
        """Delete Probe
        Args:
            uuid (str, required): uuid
            kwargs (dict, optional): additional parameters for execute. Default to None.
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('DELETE', path=f'/probes/{uuid}', **kwargs)
        return response

    def probes_agent_put(self, uuid: str, kwargs: dict = None, **payload
        ) -> list:
        """Agent Update Probe
        Args:
            uuid (str, required): uuid
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.
        Keyword Args:
            phone (string optional): additional filter - payload
            password (string optional): additional filter - payload
            email (string optional): additional filter - payload
            active (boolean optional): additional filter - payload
            acl (object optional): additional filter - payload
            uuid_acl_override (string optional): additional filter - payload
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('PUT', path=f'/probes/agent/{uuid}',
            payload=payload, **kwargs)
        return response

    def probes_objects(self, uuid: str, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """List Objects
        Args:
            uuid (str, required): uuid
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            not_in (boolean optional): additional filter - parameter
            skip (integer optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (integer optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
            like (boolean optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True. - parameter
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('GET', path=f'/probes/{uuid}/objects',
            single_page=single_page, page_size=page_size, warm_start=
            warm_start, params=params, **kwargs)
        return response

    def probes_objects_create(self, uuid: str, uuid_object: str,
        kwargs: dict = None) -> list:
        """Add Object
        Args:
            uuid (str, required): uuid
            uuid_object (str, required): uuid_object
            kwargs (dict, optional): additional parameters for execute. Default to None.
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=
            f'/probes/{uuid}/objects/{uuid_object}', **kwargs)
        return response

    def probes_objects_delete(self, uuid: str, uuid_object: str,
        kwargs: dict = None) -> list:
        """Remove Object
        Args:
            uuid (str, required): uuid
            uuid_object (str, required): uuid_object
            kwargs (dict, optional): additional parameters for execute. Default to None.
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('DELETE', path=
            f'/probes/{uuid}/objects/{uuid_object}', **kwargs)
        return response

    def probes_bulk(self, payload: list, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Bulk Read Probes
        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            payload (list[dict], optional): List dict to create.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
        Examples:
            payload = 
          [
            "uuid": "str", required
          ]
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=f'/probes/bulk/read/',
            single_page=single_page, page_size=page_size, warm_start=
            warm_start, params=params, payload=payload, **kwargs)
        return response

    def probes_create_bulk(self, payload: list, single_page: bool = False,
        page_size: int = 5000, kwargs: dict = None, **params) -> list:
        """Bulk Create Probes
        Args:
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            best_effort (boolean optional): additional filter - parameter
        Examples:
            payload = 
          [
           {
            "uuid_virtual_domain": "string", required
            "uuid_probe_type": "string", required
            "uuid_host": "string", required
            "name": "string", required
            "description": "string", optional
            "data_profile": "array object", required
            "notes": "string", optional
            "status": "string", required
           }
          ]
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=f'/probes/bulk/create/',
            single_page=single_page, page_size=page_size, params=params,
            payload=payload, **kwargs)
        return response

    def probes_delete_bulk(self, payload: list, single_page: bool = False,
        page_size: int = 5000, kwargs: dict = None) -> list:
        """Bulk Delete Probes
        Args:
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
        Examples:
            payload = 
          [
            "uuid": "str", required
          ]
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=f'/probes/bulk/delete/',
            single_page=single_page, page_size=page_size, payload=payload,
            **kwargs)
        return response

    def probes_objects_create_bulk(self, payload: list,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Bulk Link Objects
        Args:
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            best_effort (boolean optional): additional filter - parameter
        Examples:
            payload = 
          [
           {
            "uuid_object": "string", required
            "uuid_probe": "string", required
           }
          ]
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=f'/probes/bulk/create/objects',
            single_page=single_page, page_size=page_size, params=params,
            payload=payload, **kwargs)
        return response

    def probes_objects_delete_bulk(self, payload: list,
        single_page: bool = False, page_size: int = 5000, kwargs: dict = None
        ) -> list:
        """Bulk Unlink Objects
        Args:
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
        Examples:
            payload = 
          [
           {
            "uuid_object": "string", required
            "uuid_probe": "string", required
           }
          ]
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=f'/probes/bulk/delete/objects',
            single_page=single_page, page_size=page_size, payload=payload,
            **kwargs)
        return response

    def probes_logs(self, uuid: str, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Consume Probe Log
        Args:
            uuid (str, required): uuid
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            skip (None optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (None optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('GET', path=f'/probes/{uuid}/logs',
            single_page=single_page, page_size=page_size, warm_start=
            warm_start, params=params, **kwargs)
        return response
