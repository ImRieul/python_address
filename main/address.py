from enum import Enum

import setting
import requests
from error.error_address import *


class Address:
    # 초기화 메서드
    def __init__(self, **query):
        self.url = 'https://dapi.kakao.com/v2/local/search/address'
        self.query = query
        self.query['analyze_type'] = AnalyzeType.EXACT if self.query.get('analyze_type') is None else self.query.get('analyze_type')
        self.data = None  # response
        self.address = None  # 지번 주소
        self.road_address = None  # 도로명 주소
        self.type = AddressType.NOT_EXIST  # 지번 주소만 있는지, 도로명 주소도 있는지 여부
        # 위에 변수들은 나중에 get 메서드를 사용하도록 해야겠다.

        # 변수 값 할당 메서드
        self.__check_analyze_type()
        self.__set_data()
        self.__set_address()
        self.__set_type()

    # Enum으로 analyze_type을 받기 위해
    def __check_analyze_type(self):
        analyze_type = 'analyze_type'
        if not isinstance(self.query.get(analyze_type), AnalyzeType):
            raise AddressAnalyzeTypeError
        elif self.query.get(analyze_type) is None:
            self.query[analyze_type] = AnalyzeType.EXACT
        else:
            self.query[analyze_type] = self.query[analyze_type]

    def __set_data(self):
        request_url = '?'
        for key, value in self.query.items():
            request_url += f"{key}="
            if isinstance(value, AnalyzeType):
                request_url += f"{value.value}&"
            else:
                request_url += f"{value}&"
        self.data = requests.get(self.url + request_url[:-1], headers={'Authorization': setting.KAKAO_TOKEN}).json()

    def __set_address(self):
        try:
            if len(self.data['documents']) != 0:  # 값을 찾았을 때
                self.address = self.data['documents'][0]['address']
                self.road_address = self.data['documents'][0]['road_address']
        except Exception as e:
            pass

    def __set_type(self):
        if self.data.get('documents') is None:
            self.type = AddressType.BED_REQUEST
        elif len(self.data.get('documents')) == 0:
            self.type = AddressType.NOT_EXIST
        elif self.data['documents'][0]['address_type'] == 'REGION_ADDR':
            self.type = AddressType.REGION_ADDR
        elif self.data['documents'][0]['address_type'] == 'ROAD_ADDR':
            self.type = AddressType.ROAD_ADDR

    # 지번 주소 전부
    def get_address_name(self, key: str = 'address_name'):
        return self.data['documents'][0]['address'][key] if self.type != AddressType.NOT_EXIST else ''

    # 도로명 주소 전부
    def get_road_address_name(self, key: str = 'address_name'):
        return self.data['documents'][0]['road_address'][key] if self.type == AddressType.ROAD_ADDR else ''


class AnalyzeType(Enum):
    EXACT = 'exact'
    SIMILAR = 'similar'


class AddressType(Enum):
    REGION_ADDR = 'region_addr'
    ROAD_ADDR = 'road_address'
    BED_REQUEST = 'bed_request'
    NOT_EXIST = None


if __name__ == '__main__':
    address = Address(query='대전 서구 관저로 3-8')
    print(address.road_address)
    print(address.address)
