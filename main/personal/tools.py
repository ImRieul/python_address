import os.path

import pandas


def list_flat(list_mix: list, this: list = None) -> list:
    if not isinstance(this, list):
        this = []
    for i in list_mix:
        if isinstance(i, list):
            this += i
        else:
            this.append(i)

    return this


def list_insert(data: list, insert_data: list, start_index: int = None) -> list:
    if start_index is None:
        start_index = len(data)
    data.insert(start_index, insert_data)
    return list_flat(data)


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


def dataframe_change_column_index(df: pandas.DataFrame, columns: list = None, index: list = None):
    change_df = pandas.DataFrame(
        pandas.DataFrame(df.to_dict('index')).to_dict('list')
    )

    change_df.columns = df.index if columns is None else columns
    change_df.index = df.columns if index is None else index

    return change_df
