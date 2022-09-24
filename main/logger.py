import logging
import os.path
import sys
import config

from main.enums.loggerEnum import LoggerEnum


class Logger:
    def __init__(self, path: str = None):
        self.path = path
        self.base = logging.getLogger(self.__directory())

        logging.basicConfig(
            level=logging.INFO,
            filename=f'{config.ROOT_PATH}/example.log',
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

    def __directory(self) -> str:
        active_module = sys._getframe(1).f_code.co_name \
            if sys._getframe(2).f_code.co_name == '<module>' \
            else sys._getframe(2).f_code.co_name

        return active_module \
            if self.path is None \
            else f'{self.path.replace(config.ROOT_PATH, "")} - function<{active_module}>'

    def info_log(self, message: str):
        self.base.info(message)


if __name__ == '__main__':
    Logger(__file__).info_log('hello logger')

    print(3, os.path.basename(__file__))
    print(4, os.path.dirname(__file__))
    print(8, config.ROOT_PATH)
