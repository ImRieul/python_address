import unittest
from unittest.mock import patch
from main.search import *


# search_yourself
class SearchYourself(unittest.TestCase):
    def test_exist(self):
        query = '대전 서구 둔산로 100'
        with patch('builtins.input', side_effect=[query]):
            search_address = search_yourself(address.Address())

        self.assertEqual(query, search_address.get_road_address_name())

    def test_not_exist(self):
        query = '커피한잔할래요'
        with patch('builtins.input', side_effect=[query]):
            search_address = search_yourself(address.Address())
        self.assertEqual('', search_address.get_road_address_name())

    def test_param_type_error(self):
        query = '대전 서구 둔산로 100'
        with patch('builtins.input', side_effect=[query]):
            with self.assertRaises(AttributeError):
                search_yourself('hello')


if __name__ == '__main__':
    unittest.main()
