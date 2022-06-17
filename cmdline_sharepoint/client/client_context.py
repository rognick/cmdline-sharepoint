import requests
from requests import HTTPError

from cmdline_sharepoint.client.client_runtime_context import ClientRuntimeContext
from cmdline_sharepoint.client.context_web_information import ContextWebInformation
from cmdline_sharepoint.odata.json_light_format import JsonLightFormat
from cmdline_sharepoint.odata.odata_metadata_level import ODataMetadataLevel
from cmdline_sharepoint.utilities.request_options import RequestOptions

class ClientContext(ClientRuntimeContext):
    """SharePoint client context"""

    def __init__(self, url, auth_context):
        super(ClientContext, self).__init__(url + "/_api/", auth_context)
        self.__web = None
        self.__site = None
        self.contextWebInformation = None
        self.json_format = JsonLightFormat(ODataMetadataLevel.Verbose)

    def request_form_digest(self):
        """Request Form Digest"""
        request = RequestOptions(self.service_root_url + "contextinfo")
        self.authenticate_request(request)
        request.set_headers(self.json_format.build_http_headers())
        response = requests.post(url=request.url,
                                 headers=request.headers,
                                 auth=request.auth)

        self.pending_request.validate_response(response)

        payload = response.json()
        if self.json_format.metadata == ODataMetadataLevel.Verbose:
            payload = payload['d']['GetContextWebInformation']
        self.contextWebInformation = ContextWebInformation()
        self.contextWebInformation.from_json(payload)
