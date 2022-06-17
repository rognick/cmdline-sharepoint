import requests

from cmdline_sharepoint.client.client_request_exception import ClientRequestException
from requests import HTTPError

class ClientRequest(object):
    """Client request for SharePoint ODATA/REST service"""

    def __init__(self, context):
        self.context = context
        self.__queries = []
        self.__resultObjects = {}

    def validate_response(self, response):
        try:
            response.raise_for_status()
        except HTTPError as e:
            raise ClientRequestException(*e.args, response=e.response)
