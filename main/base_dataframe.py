from typing import Union, Dict

import pandas
from pandas.core.indexing import _iLocIndexer

from main.row_class import RowClass


class BaseDataFrame:
    def __init__(self, dataframe: pandas.DataFrame):
        self.__dataframe: pandas.DataFrame = dataframe
        self.__rows = []
        self.setting_row()

    def setting_row(self):
        for i in self.__dataframe.iloc:
            self.__rows.append(RowClass(i))

    @property
    def row(self) -> list[RowClass]:
        return self.__rows

    # @row.setter
    # def row(self, value: Dict[int, list]):
    #     column_index = list(value.keys())[0]
    #     rows_data = list(value.values())
    #
    #     self.__dataframe.iloc[column_index] = rows_data

    @row.setter
    def row(self, value):
        self.__dataframe.iloc[value[0]] = value[1]


if __name__ == '__main__':
    df = pandas.DataFrame({'a': [1, 2], 'b': [3, 4]})
    bdf = BaseDataFrame(df)

    # bdf.row = 1, [22, 44]
    print(bdf.row)
    bdf.row(1) = [22, 44]
    print(bdf.row[1])

