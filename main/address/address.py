import setting
import requests
from error.error_address import *
from main.address.enum import AnalyzeType, AddressType


class Address:
    # 초기화 메서드
    def __init__(self, analyze_type: AnalyzeType = AnalyzeType.EXACT, **query):
        self.url = 'https://dapi.kakao.com/v2/local/search/address'
        self.query = query
        self.analyze_type = analyze_type
        self.__data = None  # response
        self.__search_type = AddressType.NOT_EXIST  # 지번 주소만 있는지, 도로명 주소도 있는지 여부
        # 위에 변수들은 나중에 get 메서드를 사용하도록 해야겠다.

        # 변수 값 할당 메서드
        self.__response()
        self.__set_search_type()

    def __response(self):
        request_url = '?' + 'analyze_type=' + self.analyze_type.value + '&' \
                      + ''.join([key + '=' + value + '&' for key, value in self.query.items()])[:-1]

        self.__data = requests.get(self.url + request_url, headers={'Authorization': setting.KAKAO_TOKEN}).json()

    def __set_search_type(self):
        if self.__data.get('documents') is None:
            self.__search_type = AddressType.BED_REQUEST
        elif len(self.__data.get('documents')) == 0:
            self.__search_type = AddressType.NOT_EXIST
        elif self.__data.get('documents')[0]['address_type'] == 'REGION_ADDR':
            self.__search_type = AddressType.REGION_ADDR
        elif self.__data.get('documents')[0]['address_type'] == 'ROAD_ADDR':
            self.__search_type = AddressType.ROAD_ADDR

    def get_search_type(self):
        return self.__search_type

    # 지번 주소 전부
    def get_address_name(self, key: str = 'address_name'):
        return self.__data['documents'][0]['address'][key] if self.__search_type != AddressType.NOT_EXIST else ''

    # 도로명 주소 전부
    def get_road_address_name(self, key: str = 'address_name'):
        return self.__data['documents'][0]['road_address'][key] if self.__search_type == AddressType.ROAD_ADDR else ''

    def get_road_address_fullname(self):
        fullname = f"{self.get_road_address_name()} " \
                   f"({self.get_road_address_name('region_3depth_name')}"
        fullname += f", {self.get_road_address_name('building_name')})" \
            if self.get_road_address_name('building_name') != '' else ')'
        return fullname


if __name__ == '__main__':
    address = Address(query='대전 서구 관저로 3-8')
    print(address.get_address_name())
    print(address.get_road_address_name())
    print(address.get_road_address_fullname())
