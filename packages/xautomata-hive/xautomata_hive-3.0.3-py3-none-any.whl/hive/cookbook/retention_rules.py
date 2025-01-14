from hive.api import ApiManager, handling_single_page_methods


class RetentionRules(ApiManager):
    """Class that handles all the XAutomata retention_rules APIs"""

    def retention_rules(self, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Read Admin Retention Rules
        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            sort_by (string optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "". - parameter
            null_fields (string optional): additional filter - parameter
            metric_profile (string optional): additional filter - parameter
            priority (integer optional): additional filter - parameter
            average_after_days (integer optional): additional filter - parameter
            average_over_minutes (integer optional): additional filter - parameter
            deletion_after_days (integer optional): additional filter - parameter
            skip (integer optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (integer optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
            like (boolean optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True. - parameter
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('GET', path=f'/retention_rules/',
            single_page=single_page, page_size=page_size, warm_start=
            warm_start, params=params, **kwargs)
        return response

    def retention_rules_create(self, kwargs: dict = None, **payload) -> list:
        """Create Retention Rule
        Args:
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.
        Keyword Args:
            uuid_customer (string required): additional filter - payload
            metric_profile (string optional): additional filter - payload
            priority (integer required): additional filter - payload
            average_after_days (integer optional): additional filter - payload
            average_over_minutes (None optional): additional filter - payload
            deletion_after_days (integer optional): additional filter - payload
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=f'/retention_rules/', payload=
            payload, **kwargs)
        return response

    def retention_rule(self, uuid: str, warm_start: bool = False,
        kwargs: dict = None) -> list:
        """Read Admin Retention Rule
        Args:
            uuid (str, required): uuid
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('GET', path=f'/retention_rules/{uuid}',
            warm_start=warm_start, **kwargs)
        return response

    def retention_rules_put(self, uuid: str, kwargs: dict = None, **payload
        ) -> list:
        """Update Retention Rule
        Args:
            uuid (str, required): uuid
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.
        Keyword Args:
            uuid_customer (string optional): additional filter - payload
            metric_profile (string optional): additional filter - payload
            priority (integer optional): additional filter - payload
            average_after_days (integer optional): additional filter - payload
            average_over_minutes (None optional): additional filter - payload
            deletion_after_days (integer optional): additional filter - payload
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('PUT', path=f'/retention_rules/{uuid}',
            payload=payload, **kwargs)
        return response

    def retention_rules_delete(self, uuid: str, kwargs: dict = None) -> list:
        """Delete Retention Rule
        Args:
            uuid (str, required): uuid
            kwargs (dict, optional): additional parameters for execute. Default to None.
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('DELETE', path=f'/retention_rules/{uuid}',
            **kwargs)
        return response
