import unittest
from main.personal.tools import *


class ListFlat(unittest.TestCase):
    def test_only_list(self):
        # given
        mix_list = [[1, 2], [3, 4]]

        # when
        flat = list_flat(mix_list)

        # then
        self.assertEqual([1, 2, 3, 4], flat)

    def test_list_and_str(self):
        # given
        mix_list_and_str = [[1, 2], '3', '4']

        # when
        flat = list_flat(mix_list_and_str)

        # then
        self.assertEqual([1, 2, '3', '4'], flat)

    def test_list_in_list(self):
        # given
        mix_list_in_list = [[1, 2], [[3]], 4]

        # when
        flat = list_flat(mix_list_in_list)

        # then
        self.assertEqual([1, 2, [3], 4], flat)


class ListInsert(unittest.TestCase):
    def test_empty_data(self):
        # given
        empty_data = []
        insert_data = [1, 2, 3]

        # when
        insert = list_insert(empty_data, insert_data)

        # then
        self.assertEqual([1, 2, 3], insert)

    def test_empty_data_start_index(self):
        # given
        empty_data = []
        insert_data = [1, 2, 3]
        start_index = 10

        # when
        insert = list_insert(empty_data, insert_data, start_index)

        # then
        self.assertEqual([1, 2, 3], insert)

    def test_empty_insert_data(self):
        # given
        data = [1, 2, 3]
        empty_insert_data = []

        # when
        insert = list_insert(data, empty_insert_data)

        # then
        self.assertEqual([1, 2, 3], insert)

    def test_empty_insert_data_start_index(self):
        # given
        data = [1, 2, 3]
        empty_insert_data = []
        start_index = 10

        # when
        insert = list_insert(data, empty_insert_data, start_index)

        # then
        self.assertEqual([1, 2, 3], insert)

    def test_data_insert_data(self):
        # given
        data = [1, 2, 3]
        insert_data = [4, 5, 6]

        # when
        insert = list_insert(data, insert_data)

        # then
        self.assertEqual([1, 2, 3, 4, 5, 6], insert)


if __name__ == '__main__':
    unittest.main()
