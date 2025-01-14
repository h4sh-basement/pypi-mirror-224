import logging


version = '0.0.14' 
author = 'mjjo'
description = 'This library is designed to correct dates in building permit records'
license = 'MIT'

def __version__():
    return version

def __author__():
    return author

def __description__():
    return description

def __license__():
    return license


class Log:

    def __init__(
        self, 
        name: str
    ):
        self.log = logging.getLogger(name)
        self.log.propagate = True
        self.formatter = logging.Formatter("%(asctime)s | [%(levelname)s] | %(message)s",
                              "%Y-%m-%d %H:%M:%S")
        self.levels = {
            "DEBUG" : logging.DEBUG,
            "INFO" : logging.INFO,
            "WARNING" : logging.WARNING,
            "ERROR" : logging.ERROR,
            "CRITICAL" : logging.CRITICAL
        }
    
    def stream_handler(
        self,
        level: str
    ):
        if len(self.log.handlers) > 0:
            return self.log # Logger already exists
        else:
            """
            level :
            > "DEBUG" : logging.DEBUG , 
            > "INFO" : logging.INFO , 
            > "WARNING" : logging.WARNING , 
            > "ERROR" : logging.ERROR , 
            > "CRITICAL" : logging.CRITICAL , 
            """
            self.log.setLevel(self.levels[level])
            streamHandler = logging.StreamHandler()
            streamHandler.setFormatter(self.formatter)
            self.log.addHandler(streamHandler)
            return self.log
