from typing import Union
import requests
import enum

import setting
from error.error_address import *
from main.address.enum import *


class Address:
    # 초기화 메서드
    def __init__(self, analyze_type: AnalyzeType = AnalyzeType.EXACT, **query):
        self.url = 'https://dapi.kakao.com/v2/local/search/address'
        self.query = query
        self.analyze_type = analyze_type
        self.__data = None  # response
        self.__search_type = AddressSearchType.NOT_EXIST

        # 변수 값 할당 메서드
        self.__response()
        self.__set_search_type()

    def __response(self):
        request_url = '?' + 'analyze_type=' + self.analyze_type.value + '&' \
                      + ''.join([key + '=' + value + '&' for key, value in self.query.items()])[:-1]

        self.__data = requests.get(self.url + request_url, headers={'Authorization': setting.KAKAO_TOKEN}).json()

    def __set_search_type(self):
        if self.__data.get('documents') is None:
            self.__search_type = AddressSearchType.BED_REQUEST
        elif len(self.__data.get('documents')) == 0:
            self.__search_type = AddressSearchType.NOT_EXIST
        elif self.__data.get('documents')[0].get('road_address') is None:
            self.__search_type = AddressSearchType.REGION_ADDR
        elif self.__data.get('documents')[0].get('road_address') is not None:
            self.__search_type = AddressSearchType.ROAD_ADDR

    def is_search_type(self, *types: AddressSearchType):
        return self.__search_type in types

    def get_search_type(self):
        return self.__search_type

    def get_address_name(self, key: Union[AddressEnum, RoadAddressEnum]) -> str:
        if key == RoadAddressEnum.FULL_NAME:
            fullname = f"{self.get_address_name(RoadAddressEnum.ADDRESS_NAME)} " \
                       f"({self.get_address_name(RoadAddressEnum.REGION_3DEPTH_NAME)}"
            fullname += f", {self.get_address_name(RoadAddressEnum.BUILDING_NAME)})" \
                if self.get_address_name(RoadAddressEnum.BUILDING_NAME) != '' else ')'
            return fullname if self.is_search_type(AddressSearchType.ROAD_ADDR) else ''
        if isinstance(key, enum.EnumMeta):  # enum 그대로 들어왔으면
            return ''
        if isinstance(key, AddressEnum):
            return self.__data['documents'][0]['address'][key.value]\
                if self.is_search_type(AddressSearchType.ROAD_ADDR, AddressSearchType.REGION_ADDR) else ''
        elif isinstance(key, RoadAddressEnum):
            return self.__data['documents'][0]['road_address'][key.value]\
                if self.is_search_type(AddressSearchType.ROAD_ADDR) else ''
        else:
            return ''


if __name__ == '__main__':
    address = Address(query='대전 서구 관저로 3-8')
    print(address.get_address_name(AddressEnum.ADDRESS_NAME))
