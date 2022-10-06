import logging
# import logging.config
import sys
import main.config as config

from main.enums.loggerEnum import *

# 아직 깔끔하진 못하다,, 더 간결하고 읽기 쉽게 할 순 없을까?
# TODO
#   __init__ 내용을 간단하게 하기


class Logger:
    def __init__(self,
                 level: LoggerEnum = LoggerEnum.DEBUG,
                 format: list[LoggerEnum] = None,
                 filename: str = 'example'
                 ):

        if format is None:
            self.__format = [LoggerFormat.ASCTIME, LoggerFormat.NAME, LoggerFormat.LEVELNAME, LoggerFormat.MESSAGE]

        # 기본 logger 설정
        self.__logger = logging.getLogger(config.where_function_path(1))
        self.__logger.setLevel(level.value)

        # handler 생성
        self.__handler_console = logging.StreamHandler(sys.stdout)
        self.__handler_file = logging.FileHandler(config.path_encoding(f'{config.root_path()}/{filename}'))

        # handler setting
        self.set_format(self.__format)

    def info(self, message: str):
        self.__logger.info(message)

    def debug(self, message: str):
        self.__logger.debug(message)

    def warning(self, message: str):
        self.__logger.warning(message)

    def critical(self, message: str):
        self.__logger.critical(message)

    def error(self, message: str):
        self.__logger.error(message)

    def set_format(self, format: list[LoggerFormat]):
        formatter = logging.Formatter(' - '.join(map(lambda x: x.value, format)))

        # remove
        if len(self.__logger.handlers) > 0:
            self.__logger.removeHandler(self.__handler_console)
            self.__logger.removeHandler(self.__handler_file)

        # set format
        self.__handler_console.setFormatter(formatter)
        self.__handler_file.setFormatter(formatter)

        # add handler
        self.__logger.addHandler(self.__handler_console)
        self.__logger.addHandler(self.__handler_file)


    def set_filename(self, name: str):
        name = f'{config.path_encoding(name)}.log'

        # remove
        if len(self.__logger.handlers) > 0:
            self.__logger.removeHandler(self.__handler_file)

        # set name
        self.__handler_file.set_name(name)

        # add handler
        self.__logger.addHandler(self.__handler_file)

    def set_level(self, level: LoggerEnum):
        # remove
        if len(self.__logger.handlers) > 0:
            self.__logger.removeHandler(self.__handler_console)
            self.__logger.removeHandler(self.__handler_file)

        # set level
        self.__handler_console.setLevel(level.value)
        self.__handler_file.setLevel(level.value)

        # add handler
        self.__logger.addHandler(self.__handler_console)
        self.__logger.addHandler(self.__handler_file)


if __name__ == '__main__':
    logger = Logger()
    logger.info('hello info')
    logger.debug('hello debug')
    logger.set_level(LoggerEnum.WARNING)
    logger.critical('input level critical, set level warning')
    logger.debug('input level debug, set level debug')
