import unittest

from error.error_search import SearchNotEqualColumnLength
from main.search import Search


# append_row
class AppendRow(unittest.TestCase):
    def test_input_list(self):
        # given
        search = Search(['number', 'alphabet'])

        # when
        search.append_row([1, 'a'])

        # then
        input_data = list(search.data.loc[0])
        self.assertEqual([1, 'a'], input_data)

    def test_input_list_len_one(self):
        with self.assertRaises(SearchNotEqualColumnLength):  # then
            # given
            search = Search(['number', 'alphabet'])
            input_data = ['hello world!']

            # when
            search.append_row(input_data)

    def test_str(self):
        # given
        search = Search(['number', 'alphabet'])
        input_data = 'world'

        # when
        search.append_row(input_data)

        # then
        self.assertEqual(list(search.data.loc[0]), [input_data, input_data])

    def test_function(self):
        # given
        search = Search(['number', 'alphabet'])

        def input_data():
            pass

        # when
        search.append_row(input_data)

        # then
        self.assertEqual(list(search.data.loc[0]), [input_data, input_data])


class AppendColumn(unittest.TestCase):
    def test_input_list(self):
        # given
        search = Search(['a', 'b', 'c'])
        input_column = {'d': [4]}

        # when
        search.append_column(input_column)

        # then
        self.assertEqual(dict(search.data['d']), input_column)


# class ToAddress:
#     def test_(self):
        # given


        # when
        # then


if __name__ == '__main__':
    unittest.main()
