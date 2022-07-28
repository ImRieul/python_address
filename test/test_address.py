import unittest

from main.address import *
from error.error_address import *
import setting


class CheckAnalyzeType(unittest.TestCase):
    def test_address_analyze_type_error(self):
        query = '대전 서구 둔산로 100'
        analyze = 'exact'
        with self.assertRaises(AddressAnalyzeTypeError):
            Address(query=query, analyze_type=analyze)

    def test_exact(self):
        query = '대전 서구 둔산로 100 서울시청'
        analyze_type = AnalyzeType.EXACT
        address = Address(query=query, analyze_type=analyze_type)
        self.assertEqual(address.type, AddressType.NOT_EXIST)

    def test_similar(self):
        query = '대전 서구 둔산로 100 서울시청'
        analyze_type = AnalyzeType.SIMILAR
        address = Address(query=query, analyze_type=analyze_type)
        self.assertEqual(len(address.data.get('documents')), 1)


class GetTest(unittest.TestCase):
    # test 진행할 함수 앞에 test를 붙여야 함
    # 2xx
    def test_OK(self):  # 200
        query = '대전 서구 둔산로 100'
        address = Address(query='대전 서구 둔산로 100')
        self.assertEqual(address.get_road_address_name(), query)

    def test_OK_not_find(self):  # 200, 값을 찾을 수 없는 경우
        address = Address(query='커피한잔할래요')
        self.assertEqual(address.type, AddressType.NOT_EXIST)

    # 4xx
    def test_bed_request(self):  # 400, bed request
        address = Address()
        self.assertEqual(address.type, AddressType.BED_REQUEST)


class GetAddressTest(unittest.TestCase):
    def test_address_name(self):
        query = '대전 서구 둔산동 1420'
        address = Address(query=query)
        self.assertEqual(address.get_address_name(), query)

    def test_road_address_name(self):
        query = '대전 서구 둔산로 100'
        address = Address(query=query)
        self.assertEqual(address.get_road_address_name(), query)

    def test_not_find(self):
        query = '커피한잔할래요'
        address = Address(query=query)
        self.assertEqual(address.address, None)

    def test_empty(self):  # 400, bed, request
        address = Address()
        self.assertEqual(address.type, AddressType.BED_REQUEST)

# class AddressExistAddress(unittest.TestCase):


if __name__ == '__main__':
    unittest.main()
