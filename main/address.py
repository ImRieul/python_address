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

        # 변수 값 할당 메서드
        self.__check_analyze_type()
        self.__get_data()
        self.__get_address()

    # Enum으로 analyze_type을 받기 위해
    def __check_analyze_type(self):
        analyze_type = 'analyze_type'
        if not isinstance(self.query.get(analyze_type), AnalyzeType):
            raise AddressAnalyzeTypeError
        elif self.query.get(analyze_type) is None:
            self.query[analyze_type] = AnalyzeType.EXACT.value
        else:
            self.query[analyze_type] = self.query[analyze_type].value

    def __get_data(self):
        request_url = '?' + ''.join([i + '=' + self.query[i] + '&' for i in self.query])[:-1]
        self.data = requests.get(self.url + request_url, headers={'Authorization': setting.KAKAO_TOKEN})
        # return self.data

    def __get_address(self):
        try:
            if len(self.data.json()['documents']) != 0:  # 값을 찾았을 때
                self.address = self.data.json()['documents'][0]['address']
                self.road_address = self.data.json()['documents'][0]['road_address']
        except Exception as e:
            pass


class AnalyzeType(Enum):
    EXACT = 'exact'
    SIMILAR = 'similar'
