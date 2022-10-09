from typing import Union, Dict

import pandas
from pandas.core.indexing import _iLocIndexer

from main.row_class import RowClass


class BaseDataFrame:
    rows = RowClass({})

    def __init__(self, dataframe: pandas.DataFrame):
        self.__dataframe: pandas.DataFrame = dataframe
        self.rows = RowClass(dataframe.to_dict('list'))
        self.rows_z = 'hello world 1'

    def row(self, value: Union[int, str]) -> list[RowClass]:
        if isinstance(value, int):
            return self.__dataframe.iloc[value]
        elif isinstance(value, str):
            return self.__dataframe.loc[value]
        return []

    # @row.setter
    # def row(self, value: Dict[int, list]):
    #     column_index = list(value.keys())[0]
    #     rows_data = list(value.values())
    #
    #     self.__dataframe.iloc[column_index] = rows_data

    # @row.setter
    # def row(self, value):
    #     self.__dataframe.iloc[value[0]] = value[1]


if __name__ == '__main__':
    df = pandas.DataFrame({'a': [1, 2], 'b': [3, 4]})
    bdf = BaseDataFrame(df)

    # 이렇게 사용할 수 있으면 좋겠다
    # bdf.row(1) = [1, 2, 3]
    # print(bdf.row(1))

    bdf.rows({'h': ['ello', 'world']})

    print(1, bdf.rows)
