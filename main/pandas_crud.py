from typing import Union

import pandas


class BaseDataFrame:
    def __init__(self, df_dataframe: pandas.DataFrame):
        self.data: pandas.DataFrame = df_dataframe

    def __read(self) -> pandas.DataFrame:
        pass

    def get_row_index(self) -> int:
        return len(self.data.index)

    def get_column_index(self) -> int:
        return len(self.data.columns)

    def get_rows_name(self) -> list[str]:
        return list(self.data.index)

    def get_columns_name(self) -> list[str]:
        return list(self.data.columns)

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

    def set_row_data(self, input_data: Union[list, str], row_index_name: str = None):
        if row_index_name is None:
            self.data.loc[len(self.data.index)] = input_data
        else:
            self.data.loc[row_index_name] = input_data
