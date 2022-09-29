from enum import Enum


class LoggerEnum(Enum):
    """
    CRITICAL = 50\n
    ERROR = 40\n
    WARNING = 30\n
    INFO = 20\n
    DEBUG = 10\n
    NOTSET = 0\n
    """
    CRITICAL = 50
    ERROR = 40
    WARNING = 30
    INFO = 20
    DEBUG = 10
    NOTSET = 0

class LoggerFormat(Enum):
    ASCTIME = '%(asctime)s'
    NAME = '%(name)s'
    LEVELNAME = '%(levelname)s'
    MESSAGE = '%(message)s'