from __future__ import annotations

from typing import Any

from main.excel import *
from main.enum.search_enum import *
from error.error_search import *

import pandas as pd

# TODO 주소 못찾으면 콘솔 입력 V
#  에러 수정
#  주소 잘 입력했는지 검증
#  주소 DB 생성
#  slice_address 리팩토링


class Search(BaseDataFrame):
    def __init__(self, put_columns: list):
        super().__init__(pd.DataFrame(columns=put_columns))
        self.put_columns = put_columns

    def append_row(self, input_data: Union[list, str]):
        if isinstance(input_data, list) and len(self.data.columns) != len(input_data):
            raise SearchNotEqualColumnLength(input_data, self.data.columns)
        self.data.loc[len(self.data.index)] = input_data

    def append_column(self, input_data: dict[Any: list], column_name: str = None):
        append_index = list(self.data.columns).index(column_name) \
            if column_name is not None and list(self.data.columns).index(column_name) != -1 \
            else len(self.data.columns)

        for key, value in input_data.items():
            if len(self.data.index) != len(value):
                raise SearchNotEqualRowLength(input_data, self.data)
            self.data.insert(append_index, key, value)

    def to_address(self, excel: Excel, search_type: SearchType, query):
        if search_type == SearchType.COLUMNS:
            for index, value in enumerate(excel.get_column_data(query)):
                if pandas.isna(value):
                    print(f'검색에 NaN 값이 들어왔습니다. {index+1} 번째 row')
                    self.append_row('')
                    continue

                query = slice_address(value)
                address = search_yourself(value, Address(query=query))

                self.append_row([address.get_address_name(i) for i in self.put_columns])
        elif search_type == SearchType.ROW:
            for index, value in enumerate(excel.get_row_data(query)):
                if pandas.isna(value):
                    print(f"검색에 NaN 값이 들어왔습니다. {index+1} 번째 column")

    def to_excel(self, excel: Excel, column_search, data_excel: Excel):
        for i, v in enumerate(excel.get_column_data(column_search)):
            if pandas.isna(v):
                print(f"검색에 NaN 값이 들어왔습니다.")
                self.append_row(self.put_columns)
                continue

            self.append_row(data_excel.data.loc[v])

    def check_column(self, excel: Excel):
        pass

    def save(self):
        # 변수에 저장하려는 excel 등을 넣어서 연결..?
        pass


def slice_address(address_name: str):
    detail_address = [',', '.', '지하', '층', '호', '상가동', '상가', '(', '***', '인근']
    index_correction = {'층': -1, '호': -3}
    add = address_name
    for detail in detail_address:
        if not pandas.isna(add) and add.find(detail) != -1:
            add = add[:add.find(detail) \
                if detail not in index_correction.keys() else add.find(detail) + index_correction[detail]]

    return add


def search_yourself(fail_query: str, fail_address: Address, count: int = 1):
    if fail_address.is_search_type(AddressDataType.REGION_ADDR, AddressDataType.ROAD_ADDR, AddressDataType.ALL_ADDR):
        return fail_address

    print(f"주소가 검색되지 않았습니다. 정확한 주소를 입력해주세요. ({count} 번째)")
    print('검색한 문자열:', fail_query)
    print('넘기고 싶다면 pass를 입력하세요')
    query = input()

    if query == 'pass' or 0 > count or count >= 3:
        return Address(query='pass')

    search_address = Address(query=query, analyze_type=fail_address.analyze_type)
    return search_address \
        if search_address.is_search_type(AddressDataType.REGION_ADDR, AddressDataType.ROAD_ADDR) \
        else search_yourself(query, search_address, count + 1)


if __name__ == '__main__':
    file_name = '27. 0세아 전용어린이집 지원현황_11번.xlsx'
    count_error = 0
    excel_columns = {
        AddressEnum.ADDRESS_NAME: '지번주소',
        RoadAddressEnum.FULL_NAME: '도로명주소',
        AddressEnum.REGION_3DEPTH_NAME: '법정동',
        AddressEnum.REGION_3DEPTH_H_NAME: '행정동',
    }

    code_h_columns = {
        AddressEnum.H_CODE: '행정코드',
    }
    code_b_columns = {
        AddressEnum.B_CODE: '법정코드',
    }

    with Excel(file_name, index_row=3, sheet_name='Sheet1') as excel:
        search_address = Search(list(excel_columns.keys()))
        search_address.to_address(excel, SearchType.COLUMNS, '주소')

        # 같은 컬럼 이름이 있으면 .1부터 시작해서 숫자가 더해짐.
        for key, value in excel_columns.items():
            excel[value] = search_address.data[key].values

        print(search_address.data[RoadAddressEnum.FULL_NAME])
        print(f'에러가 난 주소는 {count_error}개 입니다.')

        search_h_code = Search(list(code_h_columns.keys()))
        search_b_code = Search(list(code_b_columns.keys()))
