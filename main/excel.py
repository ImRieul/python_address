from __future__ import annotations

import pandas
import platform

import setting


# 만들고 싶은 기능
# 엑셀 읽기, 쓰기
class Excel:
    def __init__(self, name: str, sheet_name: str | None = None,
                 index_row: int | None = 0, index_col: int | None = 0):
        self.__name = name
        self.__sheet_name = sheet_name
        self.__index_row = index_row
        self.__index_col = index_col
        self.sheet = None

        self.__read_excel()

    def __read_excel(self):
        platform_path = f'{setting.ROOT_PROJECT}\\{self.__name}' if platform.system() == 'Windows' else\
                        f'{setting.ROOT_PROJECT}/{self.__name}'

        if self.__sheet_name is None:
            self.sheet = pandas.read_excel(platform_path,
                                           header=self.__index_row,
                                           index_col=self.__index_col)
        else:
            self.sheet = pandas.read_excel(platform_path,
                                           sheet_name=self.__sheet_name,
                                           header=self.__index_row,
                                           index_col=self.__index_col)


if __name__ == '__main__':
    # xls, xlsx FileNotFoundError
    excel = Excel('sample.xlsx', index_row=1)
    print(excel.sheet)
