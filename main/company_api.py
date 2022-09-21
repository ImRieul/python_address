from __future__ import annotations

import requests

import setting
from main.enums.company_enum import CompanyResultType


# from main.enum.company_enum import CompanyEnum


class CompanyApi:
    def __init__(self, name: str, x: str, y: str, **query):
        self.url = 'https://dapi.kakao.com/v2/local/search/keyword'
        self.query = query
        self.__data = self.__response(name, x, y)
        self.__company_result_type = self.__set_company_result_type()
        self.__list = self.__set_company_list()

    def __response(self, name, x, y) -> dict:
        if self.query.get('query') is not None:
            del (self.query['query'])
        if self.query.get('radius') is None:
            self.query['radius'] = '50'

        request_url = '?' + 'query=' + name + '&' + \
                      'x=' + x + '&' + \
                      'y=' + y + '&' + \
                      ''.join([key + '=' + value + '&' for key, value in self.query.items()])[:-1]

        return requests.get(self.url + request_url,
                            headers={'Authorization': setting.KAKAO_TOKEN}).json()

    def __set_company_result_type(self) -> CompanyResultType:
        if self.__data.get('documents') is None:
            return CompanyResultType.FAIL
        elif len(self.__data.get('documents')) > 0:
            return CompanyResultType.SUCCESS
        return CompanyResultType.FAIL

    def __set_company_list(self) -> list[Company]:
        if self.is_company_result_type(CompanyResultType.SUCCESS):
            return list(map(lambda param: Company(
                address_name=param.get("address_name"),
                category_group_code=param.get('category_group_code'),
                category_group_name=param.get('category_group_name'),
                category_name=param.get('category_name'),
                distance=param.get('distance'),
                id=param.get('id'),
                phone=param.get('phone'),
                place_name=param.get('place_name'),
                place_url=param.get('place_url'),
                road_address_name=param.get('road_address_name'),
                x=param.get('x'),
                y=param.get('y')
            ), self.__data.get('documents')))

    def get_company_result_type(self) -> CompanyResultType:
        return self.__company_result_type

    def is_company_result_type(self, *types: CompanyResultType) -> bool:
        return self.__company_result_type in types

    def get_company_list(self) -> list[Company]:
        return self.__list

    def get_company_list_name(self) -> list:
        return list(map(lambda x: x.place_name, self.__list))

    def get_company_from_index(self, index: int) -> Company:
        return self.__list[index] \
            if index < len(self.__list) \
            else []


class Company:
    def __init__(self,
                 address_name: str | None,
                 category_group_code: str | None,
                 category_group_name: str | None,
                 category_name: str | None,
                 distance: str | None,
                 id: str | None,
                 phone: str | None,
                 place_name: str | None,
                 place_url: str | None,
                 road_address_name: str | None,
                 x: str | None,
                 y: str | None
                 ):
        self.address_name = address_name
        self.category_group_code = category_group_code
        self.category_group_name = category_group_name
        self.category_name = category_name
        self.distance = distance
        self.id = id
        self.phone = phone
        self.place_name = place_name
        self.place_url = place_url
        self.road_address_name = road_address_name
        self.x = x
        self.y = y


if __name__ == '__main__':
    company_api = CompanyApi("대전광역시청", "127.384633005948", "36.3503849976553")
    print(list(map(lambda x: x.phone, company_api.get_company_list())))
