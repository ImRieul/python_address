from typing import Mapping, overload, Iterable

from main.entity.dataframe.base_dataframe import WithDict


class DictTest(dict):
    def __init__(self, dic: dict):
        super(DictTest, self).__init__(dic)

    def __getitem__(self, item):
        print('call getitem', item)
        print(self)
        return super(DictTest, self).__getitem__(item)

    def __setitem__(self, key, value):
        print('call setitem', key, value)
        super(DictTest, self).__setitem__(key, value)


if __name__ == '__main__':
    # dic = DictTest({'a': [1, 2], 'b': [3, 4]})
    dic = WithDict({'a': [1, 2], 'b': [3, 4]})
    dic['a'].append(3)
    print(dic.__index__())