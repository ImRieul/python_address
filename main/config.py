import os
import platform
import sys


def path_encoding(path: str) -> str:
    """
    윈도우와 맥의 디렉토리 구분이 다르기에 맞춰주는 함수
    window = \, mac = /
    """
    if platform.system() == "Windows":
        return path.replace("/", "\\")
    elif platform.system() == "Darwin":
        return path.replace("\\", "/")
    return path


# ROOT_PATH = '/'.join(
#     os.path.dirname(__file__) \
#         .split('/')[:len(os.path.dirname(__file__).split('/')) - 1]
# )


def root_path() -> str:
    if platform.system() == "Windows":
        return '\\'.join(
            os.path.dirname(__file__) \
                .split('\\')[:len(os.path.dirname(__file__).split('\\')) - 1]
        )
    elif platform.system() == "Darwin":
        return '/'.join(
            os.path.dirname(__file__) \
                .split('/')[:len(os.path.dirname(__file__).split('/')) - 1]
        )

    return ''


def where_function_path(deep_level: int = 1) -> str:
    if not isinstance(deep_level, int):
        raise ValueError('where_function_path need to have parameter type int')
    try:
        return sys._getframe(deep_level).f_code.co_name
    except ValueError as value_error:
        return sys._getframe(1).f_code.co_name  # where_function_path를 호출한 함수


if __name__ == '__main__':
    print(1, root_path())
    print(2, __file__)
    print(3, os.path.dirname(__file__))
    print(4, path_encoding('C:/programming/find_address/main/config.py'))
    print(5, where_function_path(2))
