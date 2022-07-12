from main import *


def slice_address(address):
    detail_address = [',', '.', '지하', '층', '호', '상가동', '상가', '(', '***']
    index_correction = {'층': -1, '호': -3}
    add = address
    for detail in detail_address:
        if add.find(detail) != -1:
            add = add[:add.find(detail) if detail not in index_correction.keys() else add.find(detail)
                                                                                      + index_correction[detail]]

    return add


if __name__ == '__main__':
    file_name = 'sample.xlsx'
    count_error = 0

    with excel.Excel(file_name, index_row=1) as excel:
        address_col = []  # 지번 주소
        road_address_col = []  # 도로명 주소
        address_3depth_name_col = []  # 법정동
        b_code_col = []  # 법정 코드
        address_3depth_h_name_col = []  # 행정동
        h_code_col = []  # 행정 코드

        for i in excel['가맹점주소']:
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
