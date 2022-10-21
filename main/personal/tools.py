import os.path
from typing import Union

import pandas

dict_values = type({}.values())


def list_flat(list_mix: list, this: list = None) -> list:
    if not isinstance(this, list):
        this = []
    for i in list_mix:
        if isinstance(i, list):
            this += i
        else:
            this.append(i)

    return this


def list_insert(data: list, insert_data: list, start_index: int = None, delete: bool = False) -> list:
    if start_index is None:
        start_index = len(data)

    for index, value in enumerate(insert_data):
        if delete:
            data.pop(start_index + index)
        data.insert(start_index + index, value)

    return list_flat(data)


def list_max(lists: Union[list[list], dict_values]):
    if isinstance(lists, dict_values):
        lists = list(lists)
    rank_len = list(map(lambda x: len(x), lists))
    first_list_index = 0
    first_list_len = rank_len[first_list_index]
    for index, value in enumerate(rank_len):
        if first_list_len < value:
            first_list_index = index

    return lists[first_list_index]


def dict_in_dict(lower: dict, upper: dict) -> bool:
    lower = {key: value for key, value in lower.items()}

    for key, value in upper.items():
        if lower.get(key) is None:
            return False
        if lower.pop(key) != value:
            return False

        if len(lower) == 0:
            return True

    if len(lower) > 0:
        return False

    return True


def replace(data: str, old_list: list, new_list) -> str:
    """
    문자열에 바꾸고 싶을 문자를 한꺼번에 두기 위해 만들었습니다.
    :param data: 기준이 되는 문자열
    :param old: 바꾸고 싶은 문자들
    :param new: 바꿀 문자
    :return:
    """
    if not isinstance(data, str):
        return ''

    for index, old in enumerate(old_list):
        data.replace(old, new_list[index])

    return data


def str_cutting(data: str, cut_len, **option) -> str:
    if option.get('split') is None:
        option['split'] = ''
    split_str = str.split(' ')

