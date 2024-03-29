from main.respository.company_api import CompanyApi
from main.enums.address_enum import RoadAddressEnum, AddressEnum
from main.excel import Excel

if __name__ == '__main__':

    # given
    file_name = '일반음식점 현황_220920_김동건.xlsx'  # 파일 이름
    count_error = 0
    company_column_name = '업소명'
    excel_columns = {
        AddressEnum.ADDRESS_NAME: '지번주소',
        RoadAddressEnum.FULL_NAME: '도로명주소',
        AddressEnum.REGION_3DEPTH_NAME: '법정동',
        AddressEnum.REGION_3DEPTH_H_NAME: '행정동',
    }

    point_columns = {
        AddressEnum.X: "X좌표",
        AddressEnum.Y: "Y좌표",
        RoadAddressEnum.X: "X좌표",
        RoadAddressEnum.Y: "Y좌표"
    }

    code_h_columns = {
        AddressEnum.H_CODE: '행정코드',
    }
    code_b_columns = {
        AddressEnum.B_CODE: '법정코드',
    }

    with Excel(file_name, index_row=1, sheet_name='Sheet1') as excel:
        # search_address = Search(list(excel_columns.keys()) + list(point_columns.keys()))
        # search_address.to_address(excel, SearchType.COLUMNS, '지번주소')
        #
        # # 같은 컬럼 이름이 있으면 .1부터 시작해서 숫자가 더해짐.
        # point_x_list = search_address.get_column_data_from_name(AddressEnum.X)
        # point_y_list = search_address.get_column_data_from_name(AddressEnum.Y)
        # for index, value in enumerate(point_x_list):
        #     if value == '':
        #         point_x_list[index] = search_address.get_column_data_from_name(RoadAddressEnum.X)[index]
        #
        # for index, value in enumerate(point_y_list):
        #     if value == '':
        #         point_y_list[index] = search_address.get_column_data_from_name(RoadAddressEnum.Y)[index]
        #
        # excel.set_column_data_from_name(input_column=point_x_list, column_name=point_columns.get(AddressEnum.X))
        # excel.set_column_data_from_name(input_column=point_y_list, column_name=point_columns.get(AddressEnum.Y))
        #
        # print(search_address.data[RoadAddressEnum.FULL_NAME])
        # print(f'에러가 난 주소는 {count_error}개 입니다.')

        # for i in search_address.data.loc[:, [AddressEnum.X, AddressEnum.Y, ]]:
        #     print(i)

        company_phone_list = excel.get_column_data_from_name('소재지전화')
        company_error_count = 0

        for index, company in enumerate(excel.get_column_data_from_name(company_column_name)):
            # 이미 전화번호가 입력되어 있으면
            if company_phone_list[index] != '':
                company_phone_list[index] = company_phone_list[index]
                continue

            # x, y값이 없으면 전국을 조회하는 거 같다,,
            company_api = CompanyApi(
                company,
                excel.get_column_data_from_name(point_columns.get(AddressEnum.X))[index],
                excel.get_column_data_from_name(point_columns.get(AddressEnum.Y))[index]
            )

            # 유효성 검사
            if company == '':
                company_phone_list[index] = ''
                company_error_count += 1
                continue
            elif company_api.get_list() is None:
                company_phone_list[index] = ''
                company_error_count += 1
                continue
            elif len(company_api.get_list()) == 0:
                company_phone_list[index] = ''
                company_error_count += 1
                continue

            excel_address_name = excel.get_column_data_from_name(excel_columns.get(AddressEnum.ADDRESS_NAME))[index].replace('대전광역시', '대전')
            excel_road_address_name = excel.get_column_data_from_name(excel_columns.get(RoadAddressEnum.FULL_NAME))[index].split(' (')[0].replace('대전광역시', '대전')
            company_address_list = list(map(lambda x: x.address_name, company_api.get_list()))
            company_road_address_list = list(map(lambda x: x.road_address_name, company_api.get_list()))

            # 업체 검색 결과 중 지번주소가 정확할 때
            if excel_address_name in company_address_list:
                company_phone_list[index] = company_api.get_company_from_index(
                    company_address_list.index(excel_address_name)
                ).phone

            # 업체 검색 결과 중 도로명주소가 정확할 때
            elif excel_road_address_name in company_road_address_list:
                company_phone_list[index] = company_api.get_company_from_index(
                    company_road_address_list.index(excel_road_address_name)
                ).phone

            elif len(company_api.get_list()) == 1:
                company_phone_list[index] = company_api.get_company_from_index(0).phone
            else:
                company_phone_list[index] = ''
                company_error_count += 1

        excel.set_column_data_from_name(
            input_column=company_phone_list,
            column_name='소재지전화'
        )

        print(f'에러난 개수는 총 {len(company_phone_list)}개수 중 {company_error_count}개 입니다.')
