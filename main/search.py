from main.excel import *
from main.address.address import *

import pandas as pd

# TODO 주소 못찾으면 콘솔 입력
#  에러 수정
#  주소 잘 입력했는지 검증
#  주소 DB 생성
#  slice_address 리팩토링


class Search:
    def __init__(self, put_columns: list, save_columns: list):
        self.box = pd.DataFrame(columns=put_columns)

    def cutting_data(self, input_data: list):
        self.box.loc[len(self.box.index)] = input_data

    # def search(self, address: Address, count: int = 0)
    #     if int != 0:
    #         print(count, '번째 주소 검색을 다시 시작합니다.')
    #         count += 1
    #
    #     query = input()


def slice_address(address_name: str):
    detail_address = [',', '.', '지하', '층', '호', '상가동', '상가', '(', '***', '인근']
    index_correction = {'층': -1, '호': -3}
    add = address_name
    for detail in detail_address:
        if pandas.isna(add) and add.find(detail) != -1:
            add = add[:add.find(detail) \
                if detail not in index_correction.keys() else add.find(detail) + index_correction[detail]]

    return add


def search_yourself(fail_query: str, fail_address: Address, count: int = 1):
    if fail_address.is_search_type(AddressSearchType.REGION_ADDR, AddressSearchType.ROAD_ADDR):
        return fail_address

    print(f"주소가 검색되지 않았습니다. 정확한 주소를 입력해주세요. ({count} 번째)")
    print('검색한 문자열:', fail_query)
    print('넘기고 싶다면 pass를 입력하세요')
    query = input()

    if query == 'pass' or 0 > count or count >= 3:
        return Address(query='pass')

    search_address = Address(query=query, analyze_type=fail_address.analyze_type)
    return search_address \
        if search_address.is_search_type(AddressSearchType.REGION_ADDR, AddressSearchType.ROAD_ADDR) \
        else search_yourself(query, search_address, count + 1)


if __name__ == '__main__':
    file_name = 'sample.xlsx'
    # file_name = '84. 옥외광고물 허가 신고 현황_4번.xlsx'
    count_error = 0
    excel_columns = {
        AddressEnum.ADDRESS_NAME: '지번주소',
        RoadAddressEnum.ADDRESS_NAME: '도로명주소',
        AddressEnum.REGION_3DEPTH_NAME: '법정동',
        AddressEnum.REGION_3DEPTH_H_NAME: '행정동',
    }

    with Excel(file_name, index_row=1) as excel:
        search = Search(list(excel_columns.keys()), list(excel_columns.values()))

        for i in excel['주소']:
            query = slice_address(i)
            address = search_yourself(i, Address(query=query))

            search.cutting_data([
                address.get_address_name(),
                address.get_road_address_fullname(),
                address.get_address_name(AddressEnum.REGION_3DEPTH_NAME),
                address.get_address_name(AddressEnum.REGION_3DEPTH_H_NAME),
            ])

        # 같은 컬럼 이름이 있으면 .1부터 시작해서 숫자가 더해짐.
        # save
        for key, value in excel_columns.items():
            excel[value] = search.box[key].values

        print(search.box[RoadAddressEnum.ADDRESS_NAME])
        print(f'에러가 난 주소는 {count_error}개 입니다.')