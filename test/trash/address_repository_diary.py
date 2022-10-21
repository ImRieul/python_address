from main.entity.model.address import Address
from main.entity.dataframe.excel import Excel


def _diary(search: str) -> str:
    address = Address()
    diary = Excel('address_diary.xlsx')

    address.region_1depth_name = [x for x in diary.column['region_1depth_name'] if search.find(x) != -1][0]
    address.region_2depth_name = [x for x in diary.column['region_2depth_name'] if search.find(x) != -1][0]
    legal_dong = [x for x in diary.column['legal_dong'] if search.find(x) != -1]

    # 지번 주소면
    if '' not in legal_dong:
        address.legal_dong = legal_dong[0]
        if search.find('-') == -1:
            lot_numbers = [x for x in search.split(' ') if x.isdigit()]
        else:
            lot_numbers = [x for x in search.split(' ') if x.find('-') == -1][0] \
                .split('-')
            address.lot_sub_number = lot_numbers[1]
        address.lot_main_number = lot_numbers[0]
    # 도로명 주소이면
    else:
        address.road_name = [x for x in diary.column['road_name'] if search.find(x) != -1][0]
        if search.find('번길') == -1:
            road_main_number = [x for x in search.split(' ') if x.isdigit()]
            address.road_main_number = road_main_number[0]
        else:
            road_main_number = [x for x in search.split(' ') if x.find('번길') != -1][0]
            road_sub_number = search.split(' ')[search.split(' ').index(road_main_number) + 1]
            address.road_main_number = road_main_number
            address.road_sub_number = road_sub_number

    return address.road_address if address.road_name is not None else address.lot_address


if __name__ == '__main__':
    address = _diary('대전 서구 한밭대로570번길 12-23')
    print(address)
