import unittest

from main.address.address import *
from main.address.enum import AnalyzeType, AddressType
from error.error_address import *
import setting

query_address = '대전 서구 둔산동 1420'
query_road_address = '대전 서구 둔산로 100'
query_only_address = '대전 서구 둔산동 1546-1'
query_not_exist = '커피한잔할래요'


class AnalyzeTypeTest(unittest.TestCase):
    def test_road_address_is_building_to_same(self):
        query = query_road_address + ' 서울시청'
        address = Address(query=query, analyze_type=AnalyzeType.EXACT)
        self.assertEqual(address.get_search_type(), AddressType.NOT_EXIST)

    def test_road_address_is_building_to_not_same(self):
        query = query_road_address + ' 서울시청'
        address = Address(query=query, analyze_type=AnalyzeType.SIMILAR)
        self.assertEqual(address.get_search_type(), AddressType.ROAD_ADDR)


class SearchTypeTest(unittest.TestCase):
    def test_address(self):
        address = Address(query=query_address)
        self.assertEqual(address.get_search_type(), AddressType.REGION_ADDR)

    def test_only_address(self):
        address = Address(query=query_only_address)
        self.assertEqual(address.get_search_type(), AddressType.REGION_ADDR)

    def test_road_address(self):
        address = Address(query=query_road_address)
        self.assertEqual(address.get_search_type(), AddressType.ROAD_ADDR)

    def test_not_exist(self):
        address = Address(query=query_not_exist)
        self.assertEqual(address.get_search_type(), AddressType.NOT_EXIST)

    def test_empty(self):
        address = Address(query='')
        self.assertEqual(address.get_search_type(), AddressType.BED_REQUEST)


if __name__ == '__main__':
    unittest.main()
