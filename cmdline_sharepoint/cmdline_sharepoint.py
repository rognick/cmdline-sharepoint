__version__ = "1.1"

import sys, os, argparse
import cmdline_sharepoint.logger

from .sharepoint import Sharepoint
from .user import User

def check_file_exists(value):
    if not os.path.isfile(value):
        raise argparse.ArgumentTypeError("%s file not exists" % value)
    return value

class RNSharepoint(cmdline_sharepoint.logger.LoggerContext):
    def __init__(self):
        super(RNSharepoint, self).__init__()

    def main(self):
        logging = self.logger(self.main.__name__)
        print("Executing SharePoint version %s." % __version__)

        try:
            parser = argparse.ArgumentParser(description="I want your name, the SharePoint folder url, and the file path you want to upload file")
            parser.add_argument('-u', '--user', type=User, help='username:password for login in SharePoint', required=True)
            parser.add_argument('-f', '--upload_file', type=check_file_exists, help='File path to be uploaded', required=True, metavar="FILE")
            parser.add_argument('-d', '--absolute_url', help = 'An absolute URL defines the exact location of the folder in SharePoint', required=True)
            args = parser.parse_args()
            logging.debug ("List of argument strings: %s" % args)

        except ImportError:
            args = None

        user = args.user
        upload_file = args.upload_file

        try:
            from urlparse import urlparse, parse_qs  # Python 2.X
        except ImportError:
            from urllib.parse import urlparse, parse_qs # Python 3+

        url_parsed = urlparse(args.absolute_url)
        sites_folder_url = parse_qs(url_parsed.query)['id'][0]
        split_url = url_parsed.path

        while (os.path.basename(os.path.split(split_url)[0]) != 'sites'):
            split_url = os.path.split(split_url)[0]
            if split_url == '/':
                logging.error("Error on server relative url")
                exit(1)


        server_relative_url = url_parsed.scheme + '://' + url_parsed.netloc + split_url

        logging.debug ("credentials: %s  %s", user.username, user.password)
        logging.debug ("filename is %s", upload_file)
        logging.debug ("sites_folder_url is %s", sites_folder_url)
        logging.debug ("url is %s", server_relative_url)

        sharepoint = Sharepoint()
        sharepoint.upload_file(user, server_relative_url, upload_file, sites_folder_url)
