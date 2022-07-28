from main import *


# 주소 못찾으면 콘솔 입력
# 에러 수정
# 주소 잘 입력했는지 검증
# 주소 DB 생성
# slice_address 리펙토링


def slice_address(address_name: str):
    detail_address = [',', '.', '지하', '층', '호', '상가동', '상가', '(', '***', '인근']
    index_correction = {'층': -1, '호': -3}
    add = address_name
    for detail in detail_address:
        if add.find(detail) != -1:
            add = add[:add.find(detail) if detail not in index_correction.keys() else add.find(detail)
                                                                                      + index_correction[detail]]

    return add


def search_yourself(fail_address: address.Address):
    print('직접 주소 입력을 시작합니다. 정확한 주소를 입력해주세요')
    query: str = input()
    search_address = address.Address(query=query, analyze_type=fail_address.query['analyze_type'])
    return search_address

# # 행정동
# address_3depth_h_name_col.append(result.address['region_3depth_h_name'])
# h_code_col.append(result.address['h_code'])
#
# # 법정동
# address_3depth_name_col.append(result.address['region_3depth_name'])
# b_code_col.append(result.address['b_code'])

# def cutting_data(response_address: address.Address):
#     if response_address.address['address_name'] is not None:
#         address_name: str = response_address.address['address_name']
#         address_3depth_name: str = response_address.address[]
#
#     road_address_name: str = f"{response_address.road_address['address_name']} "\
#                              f"({response_address.road_address['region_3depth_name']}"
#     road_address_name += f", {response_address.road_address['building_name']})" \
#         if response_address.road_address['building_name'] != '' else ')'
#
#     return {
#         '지번주소': address_name,
#         '도로명주소': road_address_name,
#         '행정동': '',
#         '행정동코드': '',
#         '법정동': '',
#         '법정동코드': ''
#     }


if __name__ == '__main__':
    # file_name = 'sample.xlsx'
    file_name = '84. 옥외광고물 허가 신고 현황_4번.xlsx'
    count_error = 0

    with excel.Excel(file_name, index_row=0) as excel:
        address_col = []  # 지번 주소
        road_address_col = []  # 도로명 주소
        address_3depth_name_col = []  # 법정동
        b_code_col = []  # 법정 코드
        address_3depth_h_name_col = []  # 행정동
        h_code_col = []  # 행정 코드

        for i in excel['표시장소도로명']:
            query = slice_address(i)
            try:
                # 검색
                result = address.Address(query=query)

                # 지번 주소
                address_col_save = result.address['address_name']
                address_col.append(address_col_save)

                # 도로명 주소
                road_address_col_save = f"{result.road_address['address_name']} " \
                                        f"({result.address['region_3depth_name']}"
                road_address_col_save += f", {result.road_address['building_name']})" if result.road_address[
                                                                                             'building_name'] != '' else ')'
                road_address_col.append(road_address_col_save)

                # 행정동
                address_3depth_h_name_col.append(result.address['region_3depth_h_name'])
                h_code_col.append(result.address['h_code'])

                # 법정동
                address_3depth_name_col.append(result.address['region_3depth_name'])
                b_code_col.append(result.address['b_code'])

            # 지번 주소는 있으나 도로명 주소가 없는 경우가 있음, 그럴 땐 지번 주소의 배열만 늘어남.
            # 지번 주소의 배열과 엑셀의 행의 수가 맞지 않으면 에러.
            except TypeError as te:
                print(f'error address : {i}, query value : {query}')
                count_error += 1
                address_col.append('')
                road_address_col.append('')
                address_3depth_h_name_col.append('')
                h_code_col.append('')
                address_3depth_name_col.append('')
                b_code_col.append('')
            except Exception as e:
                count_error += 1
                print(e)

        # 같은 컬럼 이름이 있으면 .1부터 시작해서 숫자가 더해짐.
        excel['지번주소'] = address_col
        excel['도로명주소'] = road_address_col
        excel['행정동'] = address_3depth_h_name_col
        excel['행정동코드'] = h_code_col
        excel['법정동'] = address_3depth_name_col
        excel['법정동코드'] = b_code_col

        print(road_address_col)
        print(f'에러가 난 주소는 {count_error}개 입니다.')

    # print(
    #     slice_address('대전 서구 문정로2번길 51,1층 108호 (탄방동,시티빌3차)')
    # )
