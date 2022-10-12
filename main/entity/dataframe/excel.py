from typing import Union

import pandas

import config
from main.entity.dataframe.base_dataframe import BaseDataFrame


class ExcelConfig:
    def __init__(self,
                 file_name: str,
                 sheet_name: Union[str, int] = 0,
                 standard_row: int = 1,
                 standard_column: int = 1,
                 ):

        self._file_name = file_name
        self._sheet_name = sheet_name
        self._standard_row = standard_row - 1 if standard_row > 1 else 0
        self._standard_column = standard_column - 1 if standard_column > 1 else 0
        self._dataframe = pandas.read_excel(io=config.root_path(self._file_name),
                                            sheet_name=sheet_name,
                                            header=self._standard_row,
                                            index_col=self._standard_column,
                                            ).fillna('')

    @property
    def file_name(self) -> str:
        return self._file_name

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

    @property
    def config(self):
        return self._config
    
    @config.setter
    def config(self, value: ExcelConfig):
        self._config = value
        super(Excel, self).__init__(self._config)


        

if __name__ == '__main__':
    excel_config = ExcelConfig('sample.xlsx')
    excel = Excel(excel_config)

    print(excel)
    print(excel.column['업체명'])
