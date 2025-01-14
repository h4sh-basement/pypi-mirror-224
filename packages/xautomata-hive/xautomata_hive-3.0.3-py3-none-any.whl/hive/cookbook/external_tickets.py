from hive.api import ApiManager, handling_single_page_methods


class ExternalTickets(ApiManager):
    """Class that handles all the XAutomata external_tickets APIs"""

    def external_tickets(self, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Read External Tickets
        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            sort_by (string optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "". - parameter
            in_sla (boolean optional): additional filter - parameter
            uuid_customer (string optional): additional filter - parameter
            uuid_virtual_domain (string optional): additional filter - parameter
            uuid_object (string optional): additional filter - parameter
            object (string optional): additional filter - parameter
            metric_type (string optional): additional filter - parameter
            metric (string optional): additional filter - parameter
            external_itsm (string optional): additional filter - parameter
            external_ticket (string optional): additional filter - parameter
            opening_date_start (string optional): additional filter - parameter
            opening_date_end (string optional): additional filter - parameter
            closing_date_start (string optional): additional filter - parameter
            closing_date_end (string optional): additional filter - parameter
            ticket_type (None optional): additional filter - parameter
            mode (None optional): additional filter - parameter
            severity (None optional): additional filter - parameter
            organization (string optional): additional filter - parameter
            responsibility (None optional): additional filter - parameter
            stage_start_sla_l1 (number optional): additional filter - parameter
            working_period_l1 (number optional): additional filter - parameter
            target_stage_start_sla_l1 (number optional): additional filter - parameter
            stage_start_sla_l2 (number optional): additional filter - parameter
            working_period_l2 (number optional): additional filter - parameter
            target_stage_start_sla_l2 (number optional): additional filter - parameter
            resolution_sla (number optional): additional filter - parameter
            working_period_resolution (number optional): additional filter - parameter
            target_period_resolution (number optional): additional filter - parameter
            null_fields (string optional): additional filter - parameter
            skip (integer optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (integer optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
            like (boolean optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True. - parameter
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('GET', path=f'/external_tickets/',
            single_page=single_page, page_size=page_size, warm_start=
            warm_start, params=params, **kwargs)
        return response

    def external_tickets_create(self, kwargs: dict = None, **payload) -> list:
        """Create External Ticket
        Args:
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.
        Keyword Args:
            uuid_customer (string required): additional filter - payload
            uuid_virtual_domain (string optional): additional filter - payload
            uuid_object (string optional): additional filter - payload
            object (string optional): additional filter - payload
            metric_type (string optional): additional filter - payload
            metric (string optional): additional filter - payload
            external_itsm (string required): additional filter - payload
            external_ticket (string required): additional filter - payload
            opening_date (string required): additional filter - payload
            closing_date (string required): additional filter - payload
            ticket_type (None required): additional filter - payload
            mode (None required): additional filter - payload
            severity (None required): additional filter - payload
            organization (string required): additional filter - payload
            responsibility (None required): additional filter - payload
            stage_start_sla_l1 (number required): additional filter - payload
            working_period_l1 (number required): additional filter - payload
            target_stage_start_sla_l1 (number required): additional filter - payload
            stage_start_sla_l2 (number required): additional filter - payload
            working_period_l2 (number required): additional filter - payload
            target_stage_start_sla_l2 (number required): additional filter - payload
            resolution_sla (number required): additional filter - payload
            working_period_resolution (number required): additional filter - payload
            target_period_resolution (number required): additional filter - payload
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=f'/external_tickets/', payload
            =payload, **kwargs)
        return response

    def external_ticket(self, uuid: str, warm_start: bool = False,
        kwargs: dict = None, **params) -> list:
        """Read External Ticket
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
        response = self.execute('GET', path=f'/external_tickets/{uuid}',
            warm_start=warm_start, params=params, **kwargs)
        return response

    def external_tickets_put(self, uuid: str, kwargs: dict = None, **payload
        ) -> list:
        """Update External Ticket
        Args:
            uuid (str, required): uuid
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.
        Keyword Args:
            uuid_customer (string optional): additional filter - payload
            uuid_virtual_domain (string optional): additional filter - payload
            uuid_object (string optional): additional filter - payload
            object (string optional): additional filter - payload
            metric_type (string optional): additional filter - payload
            metric (string optional): additional filter - payload
            external_itsm (string optional): additional filter - payload
            external_ticket (string optional): additional filter - payload
            opening_date (string optional): additional filter - payload
            closing_date (string optional): additional filter - payload
            ticket_type (None optional): additional filter - payload
            mode (None optional): additional filter - payload
            severity (None optional): additional filter - payload
            organization (string optional): additional filter - payload
            responsibility (None optional): additional filter - payload
            stage_start_sla_l1 (number optional): additional filter - payload
            working_period_l1 (number optional): additional filter - payload
            target_stage_start_sla_l1 (number optional): additional filter - payload
            stage_start_sla_l2 (number optional): additional filter - payload
            working_period_l2 (number optional): additional filter - payload
            target_stage_start_sla_l2 (number optional): additional filter - payload
            resolution_sla (number optional): additional filter - payload
            working_period_resolution (number optional): additional filter - payload
            target_period_resolution (number optional): additional filter - payload
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('PUT', path=f'/external_tickets/{uuid}',
            payload=payload, **kwargs)
        return response

    def external_tickets_delete(self, uuid: str, kwargs: dict = None) -> list:
        """Delete External Ticket
        Args:
            uuid (str, required): uuid
            kwargs (dict, optional): additional parameters for execute. Default to None.
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('DELETE', path=f'/external_tickets/{uuid}',
            **kwargs)
        return response

    def external_tickets_ticket_by_params(self, ticket_type: str,
        uuid_customer: str, warm_start: bool = False, kwargs: dict = None,
        **params) -> list:
        """Pie Charts
        Args:
            ticket_type (str, required): ticket_type
            uuid_customer (str, required): uuid_customer
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        response = self.execute('GET', path=
            f'/external_tickets/ticket_by_params/{ticket_type}/{uuid_customer}'
            , warm_start=warm_start, params=params, **kwargs)
        return response

    def external_tickets_ticket_by_sla(self, ticket_type: str,
        uuid_customer: str, warm_start: bool = False, kwargs: dict = None,
        **params) -> list:
        """Sla Charge And Resolution
        Args:
            ticket_type (str, required): ticket_type
            uuid_customer (str, required): uuid_customer
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        response = self.execute('GET', path=
            f'/external_tickets/ticket_by_sla/{ticket_type}/{uuid_customer}',
            warm_start=warm_start, params=params, **kwargs)
        return response

    def external_tickets_ticket_by_date(self, uuid_customer: str,
        warm_start: bool = False, kwargs: dict = None, **params) -> list:
        """History
        Args:
            uuid_customer (str, required): uuid_customer
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        response = self.execute('GET', path=
            f'/external_tickets/ticket_by_date/{uuid_customer}', warm_start
            =warm_start, params=params, **kwargs)
        return response

    def external_tickets_ticket_by_params_customers_filtering(self,
        ticket_type: str, warm_start: bool = False, kwargs: dict = None, **
        params) -> list:
        """Customers Filtering Pie Charts
        Args:
            ticket_type (str, required): ticket_type
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        response = self.execute('GET', path=
            f'/external_tickets/ticket_by_params/customers_filtering/{ticket_type}/'
            , warm_start=warm_start, params=params, **kwargs)
        return response

    def external_tickets_ticket_by_sla_customers_filtering(self,
        ticket_type: str, warm_start: bool = False, kwargs: dict = None, **
        params) -> list:
        """Customers Filtering Sla Charge And Resolution
        Args:
            ticket_type (str, required): ticket_type
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        response = self.execute('GET', path=
            f'/external_tickets/ticket_by_sla/customers_filtering/{ticket_type}/'
            , warm_start=warm_start, params=params, **kwargs)
        return response

    def external_tickets_ticket_by_date_customers_filtering(self,
        warm_start: bool = False, kwargs: dict = None, **params) -> list:
        """Customers Filtering History
        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.
        Keyword Args:
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        response = self.execute('GET', path=
            f'/external_tickets/ticket_by_date/customers_filtering/',
            warm_start=warm_start, params=params, **kwargs)
        return response

    def external_tickets_bulk(self, payload: list, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Bulk Read External Tickets
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
        response = self.execute('POST', path=
            f'/external_tickets/bulk/read/', single_page=single_page,
            page_size=page_size, warm_start=warm_start, params=params,
            payload=payload, **kwargs)
        return response

    def external_tickets_create_bulk(self, payload: list,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Bulk Create External Tickets
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
            "uuid_customer": "string", required
            "uuid_virtual_domain": "string", optional
            "uuid_object": "string", optional
            "object": "string", optional
            "metric_type": "string", optional
            "metric": "string", optional
            "external_itsm": "string", required
            "external_ticket": "string", required
            "opening_date": "string", required
            "closing_date": "string", required
            "ticket_type": "None", required
            "mode": "None", required
            "severity": "None", required
            "organization": "string", required
            "responsibility": "None", required
            "stage_start_sla_l1": "number", required
            "working_period_l1": "number", required
            "target_stage_start_sla_l1": "number", required
            "stage_start_sla_l2": "number", required
            "working_period_l2": "number", required
            "target_stage_start_sla_l2": "number", required
            "resolution_sla": "number", required
            "working_period_resolution": "number", required
            "target_period_resolution": "number", required
           }
          ]
        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=
            f'/external_tickets/bulk/create/', single_page=single_page,
            page_size=page_size, params=params, payload=payload, **kwargs)
        return response
