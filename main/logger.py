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
            format = [LoggerFormat.ASCTIME, LoggerFormat.NAME, LoggerFormat.LEVELNAME, LoggerFormat.MESSAGE]

        self.__handler_console = logging.StreamHandler(sys.stdout)
        self.__handler_file = logging.FileHandler(filename=f'{filename}.log')

        self.__logger = logging.getLogger(config.where_function_path(1))
        self.__logger.setLevel(logging.DEBUG)

        self.__level = self.set_level(level)
        self.__format = self.set_format(format)
        self.__filename = self.set_filename(config.path_encoding(f'{config.root_path()}/{filename}'))

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

    def set_level(self, level: LoggerEnum):
        self.__handler_console.setLevel(level.value)
        self.__handler_file.setLevel(level.value)

        self.__add_handler()

        return level

    def set_format(self, format: list[LoggerFormat]):
        format = logging.Formatter(' - '.join(map(lambda x: x.value, format)))

        self.__handler_console.setFormatter(format)
        self.__handler_file.setFormatter(format)

        self.__add_handler()

        return format

    def set_filename(self, name: str):
        name = f'{config.path_encoding(name)}.log'

        self.__handler_file = logging.FileHandler(filename=name)
        self.__handler_file.setFormatter(self.__format)
        self.__handler_file.setLevel(self.__level.value)

        self.__logger.addHandler(self.__handler_file)

        self.__add_handler()

        return name.replace('.log', '')

    def __add_handler(self):
        self.__logger.addHandler(self.__handler_console)
        self.__logger.addHandler(self.__handler_file)


if __name__ == '__main__':
    logger = Logger()
    logger.info('hello info')
    logger.debug('hello debug')
    logger.set_level(LoggerEnum.WARNING)
    logger.critical('input level critical, set level warning')
    logger.debug('input level debug, set level debug')
