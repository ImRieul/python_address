from typing import Union

import pandas

from error.error_base_dataframe import *


class BaseDataFrame:
    def __init__(self, df_dataframe: pandas.DataFrame):
        self.data: pandas.DataFrame = df_dataframe

    def _append_over_column(self, over_row: int) -> None:
        over_data = pandas.DataFrame(
            {f"row_index_{i}": [] for i in (range(self.get_row_index(), self.get_row_index() + over_row))}
        )
        self.data = pandas.concat([self.data, over_data])

    def _data_slice(self, list_base: list, list_update: list, start_index: int = 0) -> list:
        if start_index > 0:
            return list_base[:start_index] + list_update + list_base[start_index + len(list_update)]
        else:
            return list_update

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
                self._append_over_column(len(input_data) + column_index - self.get_column_index())
            else:
                raise BaseDataFrameSetOverRow

        # 데이터 수정
        if row_name is not None:
            # column_index로 이름 변경
            self.data.loc[row_name] = self._data_slice(self.data.loc[row_name], input_data, column_index) \
                if column_index > 0 else input_data
        elif row_index is not None:
            # column_index로 이름 변경
            self.data.loc[self.get_rows_name()[row_index]] = self._data_slice(self.data.iloc[row_index], input_data, column_index) \
                if column_index > 0 else input_data
        else:
            self.data.loc[len(self.data.index)] = input_data

    # def set_row_data_to_index(self, input_data: Union[list, str], row_index: int = None, column_index: int = 0, over_column: bool = False):