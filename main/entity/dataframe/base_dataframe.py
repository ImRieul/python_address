from __future__ import annotations

from typing import Union

import pandas
import pandas.core.indexing
from enum import Enum
from main.personal import tools


# TODO
#   1. dict <-> dataframe은 dataframe만 사용하는 것보다 리소스 소모가 크다 dataframe로만 원하는 기능을 구현할 수 있는지 알아보자
class BaseDataFrame:
    def __init__(self,
                 data=None,
                 index=None,
                 columns=None,
                 data_type=None,
                 copy: bool | None = None,
                 ):
        self._dataframe = pandas.DataFrame(data, index, columns, data_type, copy)
        self._row: WithDict = WithDict(self._dataframe.T.to_dict('list'), list(self._dataframe.columns))
        self._column: WithDict = WithDict(self._dataframe.to_dict('list'), list(self._dataframe.index))

    @property
    def row(self) -> dict:
        self._update()
        return self._row

    @property
    def column(self) -> dict:
        self._update()
        return self._column

    def _update(self):
        update_row = pandas.DataFrame.from_dict(self._row, orient='index', columns=self._row.__index__())
        update_column = pandas.DataFrame(self._column, index=self._column.__index__())

        if not self._dataframe.equals(update_row):
            self._dataframe = update_row
        elif not self._dataframe.equals(update_column):
            self._dataframe = update_column

    def __call__(self):
        self._update()
        return self._dataframe

    def __repr__(self) -> str:
        self._update()
        return self._dataframe.to_string()

    @property
    def T(self) -> pandas.DataFrame:
        self._update()
        return self._dataframe.transpose()


class WithDict(dict):
    def __init__(self, dic: dict[str, list], index: list = None):
        super(WithDict, self).__init__(dic)

        if len(dic.values()) == 0:
            self._index = []
        elif index is not None and len(index) == len(list(dic.values())[0]):
            self._index = index
        else:
            self._index = [i for i in range(len(list(dic.values())[0]))]
        self._keys = list(dic.keys())

    def __getitem__(self, item: Union[str, int]) -> dict[str, list]:
        """
        기존 dict을 계량했습니다. .get() 메서드를 index로 조회할 수도 있게 변경합니다.
        fix dict because search to index

        :param item: 정확한 Key or index
        :return: Value
        """

        result = []

        if item in self._keys:
            self._check_index()
            result = self.get(item)
        elif isinstance(item, int) and len(self.keys()) >= item:
            self._check_index()
            result = self.get(list(self.keys())[item])

        # 값들의 list 길이가 서로 다를 경우
        if len(tools.list_max(self.values())) > len(result):
            result += ['' for i in range(len(result), len(tools.list_max(self.values())))]

        if len(result) == 0:
            raise ValueError(f"'{item}' is no in WithDict")
        else:
            return result

    def __setitem__(self, key, value):
        """
        :param key: Key with save, key only str
        :param value: Value with save
        """
        if self.get(key) is None:
            super(WithDict, self).update({key: value})
            self._keys.append(key)
        elif isinstance(key, str):
            super(WithDict, self).__setitem__(key, value)

    def __repr__(self):
        return pandas.Series(self).to_string()

    def __index__(self) -> list:
        self._check_index()
        return self._index

    def _check_index(self):
        max_values = tools.list_max(list(self.values()))

        if len(max_values) > len(self._index):
            self._index.extend([i for i in range(len(self._index), len(max_values))])


if __name__ == '__main__':
    df = pandas.DataFrame({'a': [1, 2], 'b': [3, 4], 'c': [5, 6]})
    bdf = BaseDataFrame(df)
    bdf1 = bdf.T

    bdf.row[2] = [12, 45, 56]
    print(bdf.row)
