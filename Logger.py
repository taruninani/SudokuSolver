from enum import Enum

class LOGLEVEL(Enum):
    DEBUG=1
    INFO=2
    WARN=3
    ERROR=4

class Logger(object):

    def info(self,string):
        print(string)

    def error(self,string):
        print(string)

    def warn(self,string):
        print(string)
