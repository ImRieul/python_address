from __future__ import annotations
import pandas


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
    def __init__(self, dic: dict, index: list = None):
        super(WithDict, self).__init__(dic)
        self._index = index if len(index) == len(list(dic.values())[0]) else [i for i in range(len(list(dic.values())[0]))]
        self._keys = list(dic.keys())

    def __getitem__(self, item):
        if item in self._keys:
            return self.get(item)
        else:
            if isinstance(item, int) and len(self.keys()) >= item:
                return self.get(list(self.keys())[item])
        raise ValueError(f"'{item}' is not in WithDict")

    def __setitem__(self, key, value):
        """
        :param key: 저장할 키
        :param value: 저장할 값
        """
        if self.get(key) is None:
            super(WithDict, self).update({key: value})
            self._keys.append(key)
        else:
            super(WithDict, self).__setitem__(key, value)

    def __repr__(self):
        return pandas.Series(self).to_string()

    def __index__(self):
        return self._index


if __name__ == '__main__':
    df = pandas.DataFrame({'a': [1, 2], 'b': [3, 4], 'c': [5, 6]})
    bdf = BaseDataFrame(df)
    bdf1 = bdf.T

    bdf.row[2] = [12, 45, 56]
    print(bdf.row)
