from __future__ import annotations
import pandas
import platform

import setting
from error.error_excel import *


# 만들고 싶은 기능
# 엑셀 읽기, 쓰기
class Excel:
    def __init__(self, name: str, sheet_name: str | None = None,
                 index_row: int | None = 0, index_col: int | None = 0):
        self.__name = name
        self.__sheet_name = sheet_name
        self.__index_row = index_row - 1 if index_row > 0 else 0
        self.__index_col = index_col - 1 if index_col > 0 else 0
        self.__path = f'{setting.ROOT_PROJECT}\\' if platform.system() == 'Windows' else \
            f'{setting.ROOT_PROJECT}/'
        self.sheet = None

        self.__read_excel()

    def __enter__(self):
        return self.sheet.fillna('')

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 행열 위치를 초기화하는 로직 만들 예정 -> 굳이 필요할까..
        # pandas.read_excel(f'{self.__path}{self.__name}')
        self.sheet.to_excel(f'{self.__path}copy_{self.__name}')

    def __getitem__(self, item):
        pass  # excel[]을 사용하는데 수정 요구가 떠서 없애는 용

    def __read_excel(self):
        if self.__sheet_name is None:
            self.sheet = pandas \
                .read_excel(f'{self.__path}{self.__name}',
                            header=self.__index_row,
                            index_col=self.__index_col) \
                .fillna('')
        else:
            self.sheet = pandas \
                .read_excel(f'{self.__path}{self.__name}',
                            sheet_name=self.__sheet_name,
                            header=self.__index_row,
                            index_col=self.__index_col) \
                .fillna('')

    def get_index_row(self):
        return self.__index_row + 1

    def get_index_col(self):
        return self.__index_col + 1

    def get_row_data(self, row_name):
        if row_name in self.sheet.index:
            row_index = list(self.sheet.index).index(row_name) + 1
            return dict(self.sheet.loc[row_index])
        else:
            raise ExcelNotFindRowIndex

    def get_column_data(self, column_name):
        if column_name in self.sheet.columns:
            return dict(self.sheet.get(column_name))
        else:
            raise ExcelNotFindColumnIndex

    def get_columns(self):
        return list(self.sheet.columns)

    def set_column(self):
        pass


if __name__ == '__main__':
    # xls, xlsx FileNotFoundError
    with Excel('sample.xlsx', index_row=1) as excel:
        pass

    text = 2
    excel2 = Excel('sample.xlsx')
    print(dict(excel2.get_row_data(text)))
