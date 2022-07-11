from main import *


def slice_address(address):
    cut_comma_dot = address.split(',')[0].split('.')[0]  # 상세주소 자르기
    # cut_detail = cut_comma_dot[:cut_comma_dot.find('층') - 1] if cut_comma_dot.find('층') != -1 \
    #     else cut_comma_dot  # 상세주소 자르기, ","로 구분이 안 되어있을 경우
    detail_address = [',', '.', '지하', '층', '***', '상가동', '(']
    detail_address_set = []
    for detail in detail_address:
        if address.find(detail) != -1:
            pass
            # address[:address.find(detail) if ]

    cut_detail = cut_comma_dot[:cut_comma_dot.find('지하') if cut_comma_dot.find('지하') != -1 else cut_comma_dot.find('층') -1 if cut_comma_dot.find('층') != -1 else len(cut_comma_dot)]
    return cut_detail.split('(')[0]


if __name__ == '__main__':
    file_name = 'sample.xlsx'
    with excel.Excel(file_name, index_row=1) as excel:
        road_col = []
        count_error = 0
        for i in excel['가맹점주소']:
            query = slice_address(i)
            try:
                result = address.Address(query=query)
                road_col_save = f"{result.road_address['address_name']} " \
                                f"{result.address['region_3depth_name']}" \
                                f" {result.road_address['building_name']}" if result.road_address[
                                                                                  'building_name'] != '' else ''

                road_col.append(road_col_save)
            except TypeError as te:
                print(f'error address : {i}, query value : {query}')
                count_error += 1
                road_col.append('')
            except Exception as e:
                print(e)

        print(road_col)
        print(f'에러가 난 주소는 {count_error}개 입니다.')
