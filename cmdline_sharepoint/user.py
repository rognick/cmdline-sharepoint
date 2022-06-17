
import re, argparse, logging

class User(object):
    def __init__(self, value):
        logging.info("Init User")
        pattern = re.compile("(.+):(.+)")
        match = pattern.match(value)
        if not match:
            logging.error("%s is an invalid username or password format [ex:username:password]" % value)
            raise argparse.ArgumentTypeError("%s is an invalid username or password format [ex:username:password]" % value)
        if (' ' in value):
            logging.error("%s is space in username or password" % value)
            raise argparse.ArgumentTypeError("%s is space in username or password" % value)
        sout=value.split(':')
        self.__username=sout[0]
        self.__password=sout[1]

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password
