import os.path


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
