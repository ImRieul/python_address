import logging
import sys

from test.trash.logging_test import logging_share_test

if __name__ == '__main__':
    # format = "%(asctime)s [%(levelname)s] %(message)s"
    # handler = logging.StreamHandler()
    # handler.setLevel(logging.WARNING)

    logging_share_test()

    print(logging.root.level, logging.INFO)