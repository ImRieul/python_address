import unittest
from main.search import *


search = Search(['number', 'alphabet'])


# append_row
class AppendRow(unittest.TestCase):
    def test_list(self):
        # given
        input_data = [1, 'a']

        # when
        search.append_row(input_data)

        # then
        self.assertEqual(list(search.data.loc[0]), input_data)

    def test_list_len_one(self):
        # given
        input_data = ['world']

        # when
        search.append_row(input_data)

        # then
        self.assertEqual(list(search.data.loc[0]), input_data)

    def test_str(self):
        # given
        input_data = 'world'

        # when
        search.append_row(input_data)

        # then
        self.assertEqual(list(search.data.loc[0]), [input_data])

    def test_function(self):
        # given
        def input_data():
            pass

        # when
        search.append_row(input_data)

        # then
        self.assertEqual(list(search.data.loc[0]), [input_data])


class Address:
    def test_not_excel_sheet(self):
        pass


if __name__ == '__main__':
    unittest.main()
