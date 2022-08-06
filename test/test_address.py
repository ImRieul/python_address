import unittest

from main.address.address import *
from main.address.address_enum import *
from error.error_address import *
import setting

query_address = '대전 서구 둔산동 1420'
query_road_address = '대전 서구 둔산로 100'
query_only_address = '대전 서구 둔산동 1546-1'
query_not_exist = '커피한잔할래요'


class AnalyzeTypeTest(unittest.TestCase):
    def test_road_address_is_building_to_same(self):
        # given
        query = query_road_address + ' 서울시청'

        # when
        address = Address(query=query, analyze_type=AnalyzeType.EXACT)

        # then
        self.assertEqual(address.get_search_type(), AddressDataType.NOT_EXIST)

    def test_road_address_is_building_to_not_same(self):
        # given
        query = query_road_address + ' 서울시청'

        # when
        address = Address(query=query, analyze_type=AnalyzeType.SIMILAR)

        # then
        self.assertEqual(AddressDataType.ALL_ADDR, address.get_search_type())


class GetSearchTypeTest(unittest.TestCase):
    def test_address(self):
        # given
        address = Address(query=query_address)

        # when
        search_type = address.get_search_type()

        # then
        self.assertEqual(AddressDataType.ALL_ADDR, search_type)

    def test_only_address(self):
        # given
        address = Address(query=query_only_address)

        # when
        search_type = address.get_search_type()

        # then
        self.assertEqual(search_type, AddressDataType.REGION_ADDR)

    def test_road_address(self):
        # given
        address = Address(query=query_road_address)

        # when
        search_type = address.get_search_type()

        # then
        self.assertEqual(AddressDataType.ALL_ADDR, search_type)

    def test_not_exist(self):
        # given
        address = Address(query=query_not_exist)

        # when
        search_type = address.get_search_type()

        # then
        self.assertEqual(search_type, AddressDataType.NOT_EXIST)

    def test_empty(self):
        # given
        address = Address(query='')

        # when
        search_type = address.get_search_type()

        # then
        self.assertEqual(search_type, AddressDataType.BED_REQUEST)


class GetAddresssNameTest(unittest.TestCase):
    # x, y 좌표는 변환 과정에서 오차가 나는듯 하다
    def test_address_name(self):
        # given
        address = Address(query=query_address)

        # when
        search_data = {i.value: address.get_address_name(i) for i in list(AddressEnum)[:-2]}

        # then
        self.assertEqual(search_data, {
                             "address_name": "대전 서구 둔산동 1420",
                             "b_code": "3017011200",
                             "h_code": "3017063000",
                             "main_address_no": "1420",
                             "mountain_yn": "N",
                             "region_1depth_name": "대전",
                             "region_2depth_name": "서구",
                             "region_3depth_h_name": "둔산1동",
                             "region_3depth_name": "둔산동",
                             "sub_address_no": ""
                         })

    def test_road_address_name(self):
        # given
        address = Address(query=query_road_address)

        # when
        search_data = {i.value: address.get_address_name(i) for i in list(RoadAddressEnum)[:-3]}

        # then
        self.assertEqual(search_data,
                         {
                             "address_name": "대전 서구 둔산로 100",
                             "building_name": "대전광역시청",
                             "main_building_no": "100",
                             "region_1depth_name": "대전",
                             "region_2depth_name": "서구",
                             "region_3depth_name": "둔산동",
                             "road_name": "둔산로",
                             "sub_building_no": "",
                             "underground_yn": "N",
                             "zone_no": "35242"
                         })

    def test_road_address_fullname(self):
        # given
        address = Address(query=query_road_address)

        # when
        address_fullname = address.get_address_name(RoadAddressEnum.FULL_NAME)

        # then
        self.assertEqual(address_fullname, query_road_address + ' (둔산동, 대전광역시청)')


if __name__ == '__main__':
    unittest.main()
