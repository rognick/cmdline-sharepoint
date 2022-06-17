from cmdline_sharepoint.auth.base_authentication_context import BaseAuthenticationContext
from cmdline_sharepoint.auth.saml_token_provider import SamlTokenProvider


class AuthenticationContext(BaseAuthenticationContext):
    """Authentication context for SharePoint Online/One Drive"""

    def __init__(self, url):
        super(AuthenticationContext, self).__init__()
        self.url = url
        self.provider = None

    def acquire_token_for_user(self, username, password):
        """Acquire token via user credentials"""
        self.provider = SamlTokenProvider(self.url, username, password)
        return self.provider.acquire_token()

    def authenticate_request(self, request_options):
        """Authenticate request"""
        if isinstance(self.provider, SamlTokenProvider):
            request_options.set_header('Cookie', self.provider.get_authentication_cookie())
        else:
            raise ValueError('Unknown authentication provider')

    def get_auth_url(self, redirect_url):
        return ""

    def get_last_error(self):
        return self.provider.get_last_error()
