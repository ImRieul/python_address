from main import *


def slice_address(address):
    cut_detail_address = address.split(',')[0].split('.')[0]  # 상세주소 자르기
    cut_detail_address2 = cut_detail_address[:cut_detail_address.find('층') - 1] if cut_detail_address.find('층') != -1 \
        else cut_detail_address  # 상세주소 자르기, ","로 구분이 안 되어있을 경우
    return split1[:split1.find('층') - 1 if split1.find('층') != -1 else len(split1)].split('(')[0]


if __name__ == '__main__':
    file_name = 'sample.xlsx'
    with excel.Excel(file_name, index_row=1) as excel:
        road_col = []
        for i in excel['가맹점주소']:
            query = slice_address(i)
            try:
                result = address.Address(query=query)
                road_col_save = f"{result.road_address['address_name']} " \
                                f"{result.address['region_3depth_name']}" \
                                f" {result.road_address['building_name']}" if result.road_address['building_name'] != '' else ''

                road_col.append(road_col_save)
            except TypeError as te:
                print(f'error address : {i}, query value : {query}')
                road_col.append('')
            except Exception as e:
                print(e)

        print(road_col)
