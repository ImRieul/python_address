import unittest

from main.entity.dataframe.base_dataframe import BaseDataFrame


class TestRow(unittest.TestCase):
    def test_row(self):
        # given
        df = BaseDataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

        # when
        row = df.row

        # then
        self.assertEqual({0: [1, 4], 1: [2, 5], 2: [3, 6]}, row)

    def test_row_index(self):
        # given
        df = BaseDataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}, index=['ㄱ', 'ㄴ', 'ㄷ'])

        # when
        row = df.row

        # then
        self.assertEqual({'ㄱ': [1, 4], 'ㄴ': [2, 5], 'ㄷ': [3, 6]}, row)

    def test_row_get_from_key_name(self):
        # given
        df = BaseDataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}, index=['ㄱ', 'ㄴ', 'ㄷ'])

        # when
        row = df.row['ㄱ']

        # then
        self.assertEqual(row, [1, 4])

    def test_row_get_from_key_index(self):
        # given
        df = BaseDataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}, index=['ㄱ', 'ㄴ', 'ㄷ'])

        # when
        row = df.row[0]

        # then
        self.assertEqual(row, [1, 4])

    def test_row_save(self):
        # given
        df = BaseDataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}, index=['ㄱ', 'ㄴ', 'ㄷ'])

        # when
        df.row['ㄹ'] = [123, 456]
        row_check = list(df().loc['ㄹ'])
        print(row_check)

        # then
        self.assertEqual(row_check, [123, 456])


class TestColumn(unittest.TestCase):
    def test_column(self):
        # given
        df = BaseDataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}, index=['ㄱ', 'ㄴ', 'ㄷ'])

        # when
        column = df.column

        # then
        self.assertEqual(column, {'a': [1, 2, 3], 'b': [4, 5, 6]})

    def test_column_get_from_name(self):
        # given
        df = BaseDataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}, index=['ㄱ', 'ㄴ', 'ㄷ'])

        # when
        column = df.column['a']

        # then
        self.assertEqual(column, [1, 2, 3])

    def test_column_get_from_index(self):
        # given
        df = BaseDataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}, index=['ㄱ', 'ㄴ', 'ㄷ'])

        # when
        column = df.column[0]

        # then
        self.assertEqual(column, [1, 2, 3])

    def test_column_save(self):
        # given
        df = BaseDataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}, index=['ㄱ', 'ㄴ', 'ㄷ'])

        # when
        df.column['c'] = [7, 8, 9]
        column_check = list(df().loc[:, 'c'])

        # then
        self.assertEqual(column_check, [7, 8, 9])


if __name__ == '__main__':
    unittest.main()
