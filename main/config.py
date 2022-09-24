import os

ROOT_PATH = '/'.join(
    os.path.dirname(__file__) \
        .split('/')[:len(os.path.dirname(__file__).split('/')) - 1]
)
