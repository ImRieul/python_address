import logging
import logging.config
import os.path
import sys
import config

from main.enums.loggerEnum import *


class Logger:
    def __init__(self):
        self.path = config.root_path()
        self.__level = LoggerEnum.DEBUG
        self.__format = [LoggerFormat.ASCTIME, LoggerFormat.NAME, LoggerFormat.LEVELNAME, LoggerFormat.MESSAGE]
        self.__filename = config.path_encoding(self.path + "/example")

        self.logger = logging.getLogger(config.where_function_path(2))  # 이후 self.__logger로 이름 변경
        self.handler = logging.StreamHandler()
        # self.file_handler = logging.FileHandler(f'{self.__filename}.log')
        self.set_filename(self.__filename)

        # logging.basicConfig(level=self.__level.value, format=' - '.join(map(lambda x: x.value, self.__format)), filename=f'{self.__filename}.log')

        self.set_level(self.__level)
        self.set_format(self.__format)

    def info(self, message: str):
        self.logger.info(message)

    def debug(self, message: str):
        self.logger.debug(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def critical(self, message: str):
        self.logger.critical(message)

    def error(self, message: str):
        self.logger.error(message)

    def set_level(self, level: LoggerEnum):
        self.__level = level
        self.handler.setLevel(self.__level.value)
        self.logger.addHandler(self.handler)

    def set_format(self, format: list[LoggerFormat]):
        self.__format = format
        self.handler.setFormatter(' - '.join(map(lambda x: x.value, self.__format)))
        self.logger.addHandler(self.handler)

    def set_filename(self, name: str):
        result = logging.FileHandler(filename=f'{config.path_encoding(name)}.log')
        result.setLevel(self.__level.value)
        result.setFormatter(' - '.join(map(lambda x: x.value, self.__format)))
        self.logger.addHandler(result)

    # def __set_basic_config(self,
    #                        level: LoggerEnum = LoggerEnum.DEBUG,
    #                        filename: str = None,
    #                        format: str = None):
    #
    #     logging.basicConfig(level=level.value,
    #                         filename=filename,
    #                         format=format,
    #                         encoding='utf-8')


if __name__ == '__main__':
    logger = Logger()
    logger.info('hello info')
    logger.debug('hello debug')
    logger.set_level(LoggerEnum.WARNING)
    logger.critical('input level critical, set level warning')
    logger.debug('input level debug, set level debug')
