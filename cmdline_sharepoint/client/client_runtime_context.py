from cmdline_sharepoint.client.client_request import ClientRequest


class ClientRuntimeContext(object):
    """SharePoint client context"""

    def __init__(self, url, auth_context):
        self.__service_root_url = url
        self.__auth_context = auth_context
        self.__pending_request = None
        self.json_format = None

    def authenticate_request(self, request):
        self.__auth_context.authenticate_request(request)

    @property
    def pending_request(self):
        if not self.__pending_request:
            self.__pending_request = ClientRequest(self)
        return self.__pending_request

    @property
    def service_root_url(self):
        return self.__service_root_url
