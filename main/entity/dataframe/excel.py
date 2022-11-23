from typing import Union

import numpy as np
import pandas

import config
from main.entity.dataframe.base_dataframe import BaseDataFrame
from main.personal import tools


# TODO
#   1. file이 없으면?
class ExcelConfig:
    def __init__(self,
                 file_name: str,
                 sheet_name: Union[str, int] = 0,
                 standard_row: int = 1,
                 standard_column: int = 1,
                 ):
        self._file_name = file_name
        self._root_file_name = config.root_path(file_name)
        self._sheet_name = sheet_name
        self._standard_row = standard_row - 1 if standard_row > 1 else 0
        self._standard_column = standard_column - 1 if standard_column > 1 else 0
        self._dataframe = pandas.read_excel(io=self._root_file_name,
                                            sheet_name=sheet_name,
                                            header=self._standard_row,
                                            index_col=self._standard_column,
                                            ).fillna('')

    @property
    def file_name(self) -> str:
        return self._file_name

    @property
    def root_file_name(self) -> str:
        return self._root_file_name

    @property
    def sheet_name(self) -> Union[str, int]:
        return self._sheet_name

    @property
    def standard_row(self) -> int:
        return self._standard_row + 1

    @property
    def standard_column(self) -> int:
        return self._standard_column + 1

    @property
    def dataframe(self) -> pandas.DataFrame:
        return self._dataframe

    @dataframe.setter
    def dataframe(self, value):
        self._dataframe = value


class Excel(BaseDataFrame):
    def __init__(self, config: Union[ExcelConfig, str]):
        if isinstance(config, str):
            config = ExcelConfig(config)

        # excel_config.dataframe.column = list(map(
        #     lambda param: param[0] if pandas.isna(param[1]) else param[1], enumerate(excel_config.dataframe.columns)
        # ))

        # index(row)가 nan인 경우 순서대로 index 삽입, excel에서 row를 입력하지 않는 경우가 있는데, 계속 경고가 떠서 만들었습니다.
        if np.NaN in config.dataframe.index:
            config.dataframe.index = list(map(
                lambda param: param[0] if pandas.isna(param[1]) else param[1], enumerate(config.dataframe.index)
            ))

        super().__init__(config.dataframe)

        self._config = config

    def save(self, copy: bool = True):
        if not copy:
            self._dataframe.to_excel(self._config.root_file_name)
        else:
            self._dataframe.to_excel(self._config.root_file_name.replace('.', '_copy.'))

    # 테스트 코드 필요
    def column_with_index(self, column_name) -> list[tuple]:
        return [(i, x) for i, x in enumerate(self.column[column_name])]

    # 테스트 코드 필요
    def row_with_index(self, row_name) -> list[tuple]:
        return [(i, x) for i, x in enumerate(self.row[row_name])]


if __name__ == '__main__':
    excel_config = ExcelConfig('sample.xlsx')
    excel = Excel(excel_config)

    print(excel)
    print(excel.column['주소'])
    excel.column['주소'] = tools.list_insert(excel.column['주소'], ['대전 서구 둔산로 10000'], 1, True)
    excel.save()
