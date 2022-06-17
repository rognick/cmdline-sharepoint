
import os, json, requests
import time, datetime
import cmdline_sharepoint.logger

from cmdline_sharepoint.auth.authentication_context import AuthenticationContext
from cmdline_sharepoint.client.client_context import ClientContext
from cmdline_sharepoint.utilities.request_options import RequestOptions
from os.path import basename

start_time = time.time()

class Sharepoint(cmdline_sharepoint.logger.LoggerContext, object):
    def __init__ (self):
        super(Sharepoint, self).__init__()

    def upload_binary_file(self, file_path, ctx_auth, folder_url):
        """Attempt to upload a binary file to SharePoint"""
        logger = self.logger(self.upload_binary_file.__name__)
        logger.debug('called')
        logger.debug("Attempt to upload a binary file to SharePoint...")
        logger.debug(self.url)

        base_url = self.url
        file_name = basename(file_path)
        files_url ="{0}/_api/web/GetFolderByServerRelativeUrl('{1}')/Files/add(url='{2}', overwrite=true)"
        full_url = files_url.format(base_url, folder_url, file_name)

        logger.debug(full_url)

        options = RequestOptions(base_url)
        context = ClientContext(base_url, ctx_auth)
        context.request_form_digest()

        options.set_header('Accept', 'application/json; odata=verbose')
        options.set_header('Content-Type', 'application/octet-stream')
        options.set_header('Content-Length', str(os.path.getsize(file_path)))
        options.set_header('X-RequestDigest', context.contextWebInformation.form_digest_value)
        options.method = 'POST'

        with open(file_path, 'rb') as outfile:
            logger.debug("=>>>> Start uploaded")

            # instead of executing the query directly, we'll try to go around
            # and set the json data explicitly
            context.authenticate_request(options)
            data = requests.post(url=full_url, data=outfile, headers=options.headers, auth=options.auth)

            if data.status_code == 200:
                # our file has uploaded successfully
                # let's return the URL
                base_site = data.json()['d']['Properties']['__deferred']['uri'].split("/sites")[0]
                relative_url = data.json()['d']['ServerRelativeUrl'].replace(' ', '%20')

                return base_site + relative_url
            else:
                logger.error("Error our file not has uploaded :(")
                logger.error(data.json())
                return data.json()['error']

    def upload_file(self, user, url, upload_file_path, sites_folder_url):
        logger = self.logger(self.upload_file.__name__)
        logger.debug('called')
        self.url = url
        ctx_auth = AuthenticationContext(url=url)
        if ctx_auth.acquire_token_for_user(username=user.username, password=user.password):
            if ctx_auth.get_last_error():
                logger.error(ctx_auth.get_last_error())
                exit(1)
            else:
                # ctx = ClientContext(url, ctx_auth)
                file_shaerpoint_url = self.upload_binary_file(upload_file_path, ctx_auth, sites_folder_url)
                print("Uploaded file URL: ", file_shaerpoint_url)
        else:
            logger.error(ctx_auth.get_last_error())
            exit(1)

        logger.debug("--- %.4f seconds ---" % (time.time() - start_time))
