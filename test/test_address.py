import unittest

from main.address import Address
import setting


class AddressGetTest(unittest.TestCase):
    # test 진행할 함수 앞에 test를 붙여야 함
    # 2xx
    def test_OK(self):  # 200
        address = Address(query='대전 서구 둔산로 100')
        self.assertEqual(address.data.status_code, 200)

    def test_not_find(self):  # 200, 값을 찾을 수 없는 경우
        address = Address(query='커피한잔할래요')
        self.assertEqual(len(address.data.json().get('documents')), 0)

    # 4xx
    def test_empty(self):  # 400, bed request
        address = Address()
        self.assertEqual(address.data.status_code, 400)


class AddressGetAddressTest(unittest.TestCase):
    def test_address_name(self):
        query = '대전 서구 둔산동 1420'
        address = Address(query=query)
        self.assertEqual(address.address['address_name'], query)

    def test_road_address_name(self):
        query = '대전 서구 둔산로 100'
        address = Address(query=query)
        self.assertEqual(address.road_address['address_name'], query)

    def test_not_find(self):
        query = '커피한잔할래요'
        address = Address(query=query)
        self.assertEqual(address.address, None)

    def test_empty(self):  # 400, bed, request
        address = Address()
        self.assertEqual(address.address, None)


if __name__ == '__main__':
    unittest.main()
