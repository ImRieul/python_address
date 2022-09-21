from main.company_api import CompanyApi
from main.enums.address_enum import RoadAddressEnum, AddressEnum
from main.enums.search_enum import SearchType
from main.excel import Excel
from main.search import Search

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
        search_address = Search(list(excel_columns.keys()) + list(point_columns.keys()))
        search_address.to_address(excel, SearchType.COLUMNS, '소재지(도로명)')

        # 같은 컬럼 이름이 있으면 .1부터 시작해서 숫자가 더해짐.
        for key, value in excel_columns.items():
            # excel.data[value] = search_address.data[key].values
            excel.set_column_data_from_name(
                input_column=search_address.get_column_data_from_name(key),
                column_name=value
            )

        point_x_list = search_address.get_column_data_from_name(AddressEnum.X)
        point_y_list = search_address.get_column_data_from_name(AddressEnum.Y)
        for index, value in enumerate(point_x_list):
            if value == '':
                point_x_list[index] = search_address.get_column_data_from_name(RoadAddressEnum.X)[index]

        for index, value in enumerate(point_y_list):
            if value == '':
                point_y_list[index] = search_address.get_column_data_from_name(RoadAddressEnum.Y)[index]

        excel.set_column_data_from_name(input_column=point_x_list, column_name=point_columns.get(AddressEnum.X))
        excel.set_column_data_from_name(input_column=point_y_list, column_name=point_columns.get(AddressEnum.Y))

        print(search_address.data[RoadAddressEnum.FULL_NAME])
        print(f'에러가 난 주소는 {count_error}개 입니다.')

        # for i in search_address.data.loc[:, [AddressEnum.X, AddressEnum.Y, ]]:
        #     print(i)

        company_phone_list = excel.get_column_data_from_name('소재지전화')

        for index, company in enumerate(excel.get_column_data_from_name(company_column_name)):
            if company_phone_list[index] != '' or company_phone_list[index] is None:
                continue

            company_api = CompanyApi(
                company,
                excel.get_column_data_from_name(point_columns.get(AddressEnum.X))[index],
                excel.get_column_data_from_name(point_columns.get(AddressEnum.Y))[index]
            )
            if company == '':
                company_phone_list[index] = ''
            elif len(company_api.get_company_list()) > 1:
                print(company_api.get_company_list_name())
                input_index: int = int(input('올바른 검색 결과의 index를 입력해주세요'))

                company_phone_list[index] = company_api.get_company_from_index(input_index).phone
            elif len(company_api.get_company_list()) == 0:
                company_phone_list[index] = ''
            elif len(company_api.get_company_list()) == 1:
                company_phone_list[index] = company_api.get_company_from_index(0).phone

        excel.set_column_data_from_name(
            input_column=company_phone_list,
            column_name='소재지전화'
        )

