import setting
from main.entity.model.address import Address
from main.enums.address_enum import AnalyzeType, AddressDataType
from main.respository.base_repository import BaseRepository
from main.personal import tools
from main.entity.dataframe.excel import Excel


class AddressRepository(BaseRepository):
    def __init__(self,
                 analyze_type: AnalyzeType = AnalyzeType.EXACT,
                 ):
        url = 'https://dapi.kakao.com/v2/local/search/address'
        super(AddressRepository, self).__init__(url)
        self._analyze_type = analyze_type
        self._address = Address()

    def _search(self, query: dict, **headers):
        if query.get('analyze_type') is None:
            query.update({'analyze_type': AnalyzeType.EXACT.value})
        else:
            query.update({'analyze_type': query['analyze_type'].value})

        headers.update({'Authorization': setting.KAKAO_TOKEN})
        super(AddressRepository, self).get(query, headers)
        self._logger.info(f'search result : {self._response}')

    def slice_address(self, address_name: str):
        pass

    # first
    def _record(self, search: str) -> str:
        record = Excel('address_record.xlsx')
        if search in record.column['search']:
            index = record.column['search'].index(search)
            lot_address = record.column['lot_address'][index]
            load_address = record.column['load_address'][index]

            return load_address if load_address != '' else lot_address

    # second
    def _diary(self, search: str) -> str:
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

    def _record_save(self, address: Address):
        record = Excel('address_record.xlsx')
        record.column['lot_address'].append(address.lot_address)
        record.column['load_address'].append(address.lot_address)

        record.save(copy=False)

    def find_by_search(self, search: str, **headers) -> Address:
        query = {'query': search}

        self._search(query, **headers)

        if self._address.data_type not in [AddressDataType.NOT_EXIST]:
            return self._address

        result_address = Address()

        if self._status != 200 \
                or self._body.get('documents') is None \
                or len(self._body.get('documents')[0]) == 0:
            return result_address

        response_address = self._body.get('documents')[0].get('address')
        response_road_address = self._body.get('documents')[0].get('road_address')

        if response_address is not None:
            result_address.region_1depth_name = response_address.get('region_1depth_name')
            result_address.region_2depth_name = response_address.get('region_2depth_name')
            result_address.legal_dong = response_address.get('region_3depth_name')
            result_address.dong_of_administration = response_address.get('region_3depth_h_name')
            result_address.lot_main_number = response_address.get('main_address_no')
            result_address.lot_sub_number = response_address.get('sub_address_no')
            result_address.code_legal = response_address.get('b_code')
            result_address.code_admin = response_address.get('h_code')
            result_address.is_mountain = response_address.get('mountain_yn')
            result_address.x = response_address.get('x')
            result_address.y = response_address.get('y')

        if response_road_address is not None:
            result_address.region_1depth_name = response_road_address.get('region_1depth_name')
            result_address.region_2depth_name = response_road_address.get('region_2depth_name')
            result_address.legal_dong = response_road_address.get('region_3depth_name')
            result_address.road_name = response_road_address.get('road_name')
            result_address.road_main_number = response_road_address.get('main_building_no')
            result_address.road_sub_number = response_road_address.get('sub_building_no')
            result_address.building_name = response_road_address.get('building_name')
            result_address.postal_code = response_road_address.get('zone_no')
            result_address.is_underground = response_road_address.get('underground_yn')
            result_address.x = response_road_address.get('x')
            result_address.y = response_road_address.get('y')

        self._address = result_address

        return result_address


if __name__ == '__main__':
    address = AddressRepository()
    print(address.find_by_search('배재로 128'))
