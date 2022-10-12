from __future__ import annotations
import pandas
import platform

import setting
from error.error_excel import *
from main.base_data_frame import BaseDataFrame


# TODO
#   1. getter, setter를 python의 방식대로 수정.
#   2. 엑셀 읽기, 쓰기
#   3. excel_openpyxl.py 지우기

class Excel(BaseDataFrame):
    def __init__(self, name: str, sheet_name: str | None = 0,
                 index_row: int | None = 0, index_col: int | None = 0):
        self.__name = name
        self.__sheet_name = sheet_name
        self.__index_row = index_row - 1 if index_row > 0 else 0
        self.__index_col = index_col - 1 if index_col > 0 else 0
        self.__path = f'{setting.ROOT_PROJECT}\\' if platform.system() == 'Windows' else \
            f'{setting.ROOT_PROJECT}/'
        self.data: pandas.DataFrame = pandas.DataFrame([])
        super().__init__(self.__read_excel())

        self.__read_excel()

    def __enter__(self):
        # return self.data.fillna('')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 행열 위치를 초기화하는 로직 만들 예정 -> 굳이 필요할까..
        # pandas.read_excel(f'{self.__path}{self.__name}')
        self.data.to_excel(f'{self.__path}copy_{self.__name}')

    def __getitem__(self, item):
        pass  # excel[]을 사용하는데 수정 요구가 떠서 없애는 용

    def __read_excel(self) -> pandas.DataFrame:
        return pandas \
            .read_excel(f'{self.__path}{self.__name}',
                        header=self.__index_row,
                        index_col=self.__index_col) \
            .fillna('')


if __name__ == '__main__':
    # xls, xlsx FileNotFoundError
    with Excel('sample.xlsx', index_row=1) as excel:
        pass

    text = 2
    excel2 = Excel('sample.xlsx')
    print(excel2.get_row_data(row_index=text))
