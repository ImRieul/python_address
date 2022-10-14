from typing import Union

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


class Excel(BaseDataFrame):
    def __init__(self, excel_config: ExcelConfig):
        super().__init__(excel_config.dataframe)
        self._config = excel_config

    def save(self):
        self._dataframe.to_excel(self._config.root_file_name.replace('.', '_copy.'))


if __name__ == '__main__':
    excel_config = ExcelConfig('sample.xlsx')
    excel = Excel(excel_config)

    print(excel)
    print(excel.column['주소'])
    excel.column['주소'] = tools.list_insert(excel.column['주소'], ['대전 서구 둔산로 10000'], 1, True)
    excel.save()
