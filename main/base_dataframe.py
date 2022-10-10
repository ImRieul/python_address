from typing import Union, Dict

import pandas
from pandas.core.indexing import _iLocIndexer

from main.row_class import RowClass


class BaseDataFrame:
    rows = RowClass({})

    def __init__(self, dataframe: pandas.DataFrame):
        self._dataframe: pandas.DataFrame = dataframe
        self.rows = RowClass(dataframe.to_dict('list'))

        self.rows_z = 'hello world 1'
        self._r = []

    def row(self) -> dict:
        return self.rows


if __name__ == '__main__':
    df = pandas.DataFrame({'a': [1, 2], 'b': [3, 4]})
    bdf = BaseDataFrame(df)

    # 이렇게 사용할 수 있으면 좋겠다
    # bdf.row(1) = [1, 2, 3]
    #
    # print(bdf.row(1))

    bdf.rows({'h': ['ello', 'world']})

    print(1, bdf.rows)
