from typing import Union

import pandas

from error.error_base_dataframe import *
from personal import tools


class BaseDataFrame:
    def __init__(self, df_dataframe: pandas.DataFrame):
        self.data: pandas.DataFrame = df_dataframe

    def _append_row(self, input_data: list = None, row_name: str = None) -> list:
        if input_data is None or len(input_data) > self.get_column_index():
            input_data = []
        if row_name is None:
            row_name = str(self.get_row_index())
        self.data.loc[row_name] = input_data
        return self.data.loc[row_name]

    def _append_column(self, input_data: list = None, column_name: str = None) -> list:
        if input_data is None or len(input_data) > self.get_row_index():
            input_data = []
        if column_name is None:
            column_name = self.get_column_index()
        self.data = pandas.concat([self.data, pandas.DataFrame({column_name: input_data})])
        return self.data.get(column_name)

    def _append_row_to_name(self,  row_name: str, input_data: list = None):
        pass

    def _append_rows(self, count: int = 0):
        if count < 0:
            count = 0
        for i in range(count):
            self._append_row()

    def _append_columns(self, count: int = 0):
        if count < 0:
            count = 0
        for i in range(count):
            self._append_column()

    def get_row_index(self) -> int:
        return len(self.data.index)

    def get_column_index(self) -> int:
        return len(self.data.columns)

    def get_rows_name(self) -> list[str]:
        return list(self.data.index)

    def get_columns_name(self) -> list[str]:
        return list(self.data.columns)

    def get_row_index_to_name(self, row_name: str) -> int:
        return self.get_rows_name().index(row_name)

    def get_column_index_to_name(self, column_name: str) -> int:
        return self.get_columns_name().index(column_name)

    def is_row(self, row_name: str = None, row_index: int = None) -> bool:
        if row_name is not None:
            return row_name in self.get_rows_name()
        elif row_index is not None:
            return row_index in range(self.get_row_index())
        else:
            return False

    def is_column(self, column_name: str = None, column_index: int = None) -> bool:
        if column_name is not None:
            return column_name in self.get_columns_name()
        elif column_index is not None:
            return column_index in range(self.get_column_index())
        else:
            return False

    def get_row_data(self, row_name: str = None, row_index: int = None) -> list[str]:
        if self.is_row(row_name=row_name):
            return list(self.data.loc[row_name])
        elif self.is_row(row_index=row_index):
            return list(self.data.iloc[row_index])

    def get_column_data(self, column_name: str = None, column_index: int = None) -> list[str]:
        if self.is_column(column_name=column_name):
            return list(self.data.get(column_name))
        elif self.is_column(column_index=column_index):
            return list(self.data.get(self.data.columns[column_index]))

    def set_row_data(self, input_data: Union[list, str], row_name: str = None, row_index: int = None,
                     column_index: Union[int, str] = 0, over_column: bool = False):
        # column이 초과됐으면 컬럼 생성
        if isinstance(input_data, list) \
                and len(input_data) + column_index > self.get_column_index():
            if over_column:
                self._append_columns(len(input_data) + column_index - self.get_column_index())
            else:
                raise BaseDataFrameSetOverRow

        # 데이터 수정
        if row_name is not None:
            # column_index로 이름 변경
            self.data.loc[row_name] = self._data_insert(self.data.loc[row_name], input_data, column_index) \
                if column_index > 0 else input_data
        elif row_index is not None:
            # column_index로 이름 변경
            self.data.loc[row_index] = self._data_insert(self.data.iloc[row_index], input_data, column_index) \
                if column_index > 0 else input_data
        else:
            self.data.loc[len(self.data.index)] = input_data

    def set_row_data_to_name(self, input_data: list, row_name: str = None,
                             column_index: int = 0, over_column: bool = False):

        input_column_index = len(input_data) + column_index
        if over_column:
            self._append_columns(input_column_index)
        elif input_column_index > self.get_column_index():
            raise BaseDataFrameSetOverRow

        if row_name is None:
            self._append_row(input_data)
        else:
            self.data.loc[row_name] = self._data_insert(self.data.loc[row_name], input_data, column_index) \
                if column_index > 0 else input_data

    def set_row_data_to_index(self, input_data: list, row_index: int = None, column_index: int = 0, over_column: bool = False):
        # 문제점
        # 1. 기능이 많음
        #  a. 새로 row를 만들어서 input_data를 넣음
        #  b. 기존 row를 조회해서 input_data를 넣음
        #  c. 기존 row를 조회하고 원하는 column_index에 원하는만큼의 data를 변경험
        #  d. row_index가 없으면 마지막 줄에 data넣음
        #  e. input_data의 양이 column을 넘으면 넘은 만큼 column 생성

        input_column_index = len(input_data) + column_index

        if input_column_index > self.get_column_index():
            if over_column:
                self._append_columns(input_column_index - self.get_column_index())
            else:
                raise BaseDataFrameSetOverRow

        # row_index 입력 x and 총 row index에 row_index가 포함되면
        if row_index is not None and row_index < self.get_row_index():
            self.data.loc[self.get_rows_name()[row_index]] = self._data_insert(
                self.data.loc[self.get_rows_name()[row_index]], input_data, column_index
            )
        # elif over_column:

        else:
            self.data.loc[self.get_row_index()] = input_data
