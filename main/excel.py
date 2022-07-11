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
        self.__path = f'{setting.ROOT_PROJECT}\\' if platform.system() == 'Windows' else \
            f'{setting.ROOT_PROJECT}/'
        self.sheet = None

        self.__read_excel()

    def __enter__(self):
        return self.sheet

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 행열 위치를 초기화하는 로직 만들 예정
        # pandas.read_excel(f'{self.__path}{self.__name}')
        self.sheet.to_excel(f'{self.__path}copy_{self.__name}')

    def __read_excel(self):
        if self.__sheet_name is None:
            self.sheet = pandas.read_excel(f'{self.__path}{self.__name}',
                                           header=self.__index_row,
                                           index_col=self.__index_col)
        else:
            self.sheet = pandas.read_excel(f'{self.__path}{self.__name}',
                                           sheet_name=self.__sheet_name,
                                           header=self.__index_row,
                                           index_col=self.__index_col)


if __name__ == '__main__':
    # xls, xlsx FileNotFoundError
    with Excel('sample.xlsx', index_row=1) as excel:
        print(excel['코드'])
