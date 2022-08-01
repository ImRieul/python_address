from typing import Any

from address.address import *
from excel import *


# TODO 주소 못찾으면 콘솔 입력
#  에러 수정
#  주소 잘 입력했는지 검증
#  주소 DB 생성
#  slice_address 리펙토링

class Search:
    def __init__(self, box: list):
        self.box = {i: [] for i in box}

    def cutting_data(self, input_data: list):
        for index, value in enumerate(self.box.keys()):
            self.box[value].append(input_data[index])

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


def search_yourself(fail_address: Address, count: int = 3):
    print('주소가 검색되지 않았습니다. 정확한 주소를 입력해주세요')
    print('검색한 문자열:', fail_address.query)
    print('넘기고 싶다면 pass를 입력하세요')
    query = input()

    if query == 'pass' or 0 > count or count > 3:
        return Address(query='pass')

    search_address = Address(query=query, analyze_type=fail_address.analyze_type)
    return search_address \
        if search_address.is_search_type(AddressSearchType.REGION_ADDR, AddressSearchType.ROAD_ADDR) \
        else search_yourself(search_address, count - 1)


if __name__ == '__main__':
    file_name = 'sample.xlsx'
    # file_name = '84. 옥외광고물 허가 신고 현황_4번.xlsx'
    count_error = 0

    with Excel(file_name, index_row=2) as excel:

        search = Search([
            AddressEnum.ADDRESS_NAME.value,  # 지번 주소
            RoadAddressEnum.ADDRESS_NAME.value,  # 도로명 주소
            AddressEnum.REGION_3DEPTH_NAME.value,  # 법정동
            AddressEnum.REGION_3DEPTH_H_NAME.value,  # 행정동
        ])

        for i in excel['가맹점주소']:
            query = slice_address(i)
            address = Address(query=query)

            search.cutting_data([address.get_address_name(),
                                 address.get_road_address_fullname(),
                                 address.get_address_name(AddressEnum.REGION_3DEPTH_NAME)])
                                 address.get_address_name(AddressEnum.REGION_3DEPTH_H_NAME)])

        #     try:
        #         # 검색
        #         result = address.Address(query=query)
        #
        #         address_col.append(result.get_address_name())
        #         road_address_col.append(result.get_road_address_fullname())
        #         address_3depth_h_name_col.append(result.get_address_name(AddressEnum.REGION_3DEPTH_H_NAME))
        #         h_code_col.append(result.get_address_name(AddressEnum.H_CODE))
        #         address_3depth_name_col.append(result.get_address_name(AddressEnum.REGION_3DEPTH_NAME))
        #         b_code_col.append(result.get_address_name(AddressEnum.B_CODE))
        #
        #     # 지번 주소는 있으나 도로명 주소가 없는 경우가 있음, 그럴 땐 지번 주소의 배열만 늘어남.
        #     # 지번 주소의 배열과 엑셀의 행의 수가 맞지 않으면 에러.
        #     except TypeError as te:
        #         print(f'error address : {i}, query value : {query}')
        #         count_error += 1
        #         address_col.append('')
        #         road_address_col.append('')
        #         address_3depth_h_name_col.append('')
        #         h_code_col.append('')
        #         address_3depth_name_col.append('')
        #         b_code_col.append('')
        #     except Exception as e:
        #         count_error += 1
        #         print(e)
        #
        # # 같은 컬럼 이름이 있으면 .1부터 시작해서 숫자가 더해짐.
        # # save
        # excel['지번주소'] = address_col
        # excel['도로명주소'] = road_address_col
        # excel['행정동'] = address_3depth_h_name_col
        # excel['행정동코드'] = h_code_col
        # excel['법정동'] = address_3depth_name_col
        # excel['법정동코드'] = b_code_col
        #
        # print(road_address_col)
        # print(f'에러가 난 주소는 {count_error}개 입니다.')

    # print(
    #     slice_address('대전 서구 문정로2번길 51,1층 108호 (탄방동,시티빌3차)')
    # )
