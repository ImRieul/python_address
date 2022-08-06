import unittest

import pandas

from main.pandas_crud import BaseDataFrame


class GetRowIndex(unittest.TestCase):
    def test_ok(self):
        # given
        df = pandas.DataFrame({'a': [1, 2]})
        bp = BaseDataFrame(df)

        # when
        row_index = bp.get_row_index()

        # then
        self.assertEqual(row_index, 2)

    def test_this_column_index(self):
        # given
        df = pandas.DataFrame({'a': [1], 'b': [2], 'c': [3]})
        bp = BaseDataFrame(df)

        # when
        row_index = bp.get_row_index()

        # then
        self.assertNotEqual(row_index, 3)


class GetColumnIndex(unittest.TestCase):
    def test_ok(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame({
            'a': [1], 'b': [2]
        }))

        # when
        column_index = bp.get_column_index()

        # then
        self.assertEqual(column_index, 2)

    def test_this_row_index(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame({
            'a': [1, 2, 3]
        }))

        # when
        column_index = bp.get_column_index()

        # then
        self.assertNotEqual(column_index, 3)


class GetRowsName(unittest.TestCase):
    def test_ok(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ']
        ))

        # when
        rows_name = bp.get_rows_name()

        # then
        self.assertEqual(rows_name, ['ㄱ', 'ㄴ'])

    def test_this_data(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))

        # when
        row_name = bp.get_rows_name()

        # then
        self.assertNotEqual(row_name, [1, 2])

    def test_this_columns(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))

        # when
        row_name = bp.get_rows_name()

        # then
        self.assertNotEqual(row_name, 'a')


class GetColumnsName(unittest.TestCase):
    def test_ok(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))

        # when
        column_name = bp.get_columns_name()

        # then
        self.assertEqual(column_name, ['a'])

    def test_this_data(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))

        # when
        column_name = bp.get_columns_name()

        # then
        self.assertNotEqual(column_name, [1, 2])

    def test_this_row(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))

        # when
        column_name = bp.get_columns_name()

        # then
        self.assertNotEqual(column_name, ['ㄱ', 'ㄴ'])


class IsRow(unittest.TestCase):
    def test_row_name_ok(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        row_name = 'ㄱ'

        # when
        is_row = bp.is_row(row_name=row_name)

        # then
        self.assertTrue(is_row)

    def test_row_name_this_data(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        data_name = 1

        # when
        is_row = bp.is_row(row_name=data_name)

        # then
        self.assertFalse(is_row)

    def test_row_name_this_column(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        column_name = 'a'

        # when
        is_row = bp.is_row(row_name=column_name)

        # then
        self.assertFalse(is_row)

    def test_row_name_not_equal_type(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['50', 'ㄴ'],
        ))
        row_name_equal_type = 50

        # when
        is_row = bp.is_row(row_name=row_name_equal_type)

        # then
        self.assertFalse(is_row)

    def test_row_index_ok(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        row_index = 0

        # when
        is_row = bp.is_row(row_index=row_index)

        # then
        self.assertTrue(is_row)

    def test_row_index_not_find(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        row_index_not_find = 100

        # when
        is_row = bp.is_row(row_index=row_index_not_find)

        # then
        self.assertFalse(is_row)


class IsColumn(unittest.TestCase):
    def test_column_name_ok(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        column_name = 'a'

        # when
        is_column = bp.is_column(column_name=column_name)

        # then
        self.assertTrue(is_column)

    def test_column_name_this_data(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        data_name = 1

        # when
        is_column = bp.is_column(column_name=data_name)

        # then
        self.assertFalse(is_column)

    def test_column_name_this_row(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))

        # when
        is_column = bp.is_column(column_name='ㄱ')

        # then
        self.assertFalse(is_column)

    def test_column_name_not_equal_type(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'50': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        column_name_equal_type = 50

        # when
        is_column = bp.is_column(column_name=column_name_equal_type)

        # then
        self.assertFalse(is_column)

    def test_column_index_ok(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))

        # when
        is_column = bp.is_column(column_index=0)

        # then
        self.assertTrue(is_column)

    def test_column_index_not_find(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))

        # when
        is_column = bp.is_column(column_index=100)

        # then
        self.assertFalse(is_column)


class GetRowData(unittest.TestCase):
    def test_row_name_ok(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        row_name = 'ㄱ'

        # when
        rows_data = bp.get_row_data(row_name=row_name)

        # then
        self.assertEqual(rows_data, [1])

    def test_row_name_this_column(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        column_name = 'a'

        # when
        rows_data = bp.get_row_data(column_name)

        # then
        self.assertIsNone(rows_data)

    def test_row_name_this_data(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        data_name = 2

        # when
        row_data = bp.get_row_data(row_name=data_name)

        # then
        self.assertIsNone(row_data)

    def test_row_name_not_equal_type(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['50', 'ㄴ'],
        ))
        row_name_not_equal_type = 50

        # when
        row_data = bp.get_row_data(row_name=row_name_not_equal_type)

        # then
        self.assertIsNone(row_data)

    def test_row_index_ok(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        row_index = 0

        # when
        row_data = bp.get_row_data(row_index=row_index)

        # then
        self.assertEqual([1], row_data)

    def test_row_index_not_find(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        row_index_not_find = 100

        # when
        row_data = bp.get_row_data(row_index=row_index_not_find)

        # then
        self.assertIsNone(row_data)


class GetColumnData(unittest.TestCase):
    def test_column_name_ok(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        column_name = 'a'

        # when
        column_data = bp.get_column_data(column_name=column_name)

        # then
        self.assertEqual([1, 2], column_data)

    def test_column_name_this_row(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        row_name = 'ㄱ'

        # when
        column_data = bp.get_column_data(column_name=row_name)

        # then
        self.assertIsNone(column_data)

    def test_column_name_this_data(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        data_name = 2

        # when
        column_data = bp.get_column_data(column_name=data_name)

        # then
        self.assertIsNone(column_data)

    def test_column_name_not_equal_type(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'50': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        column_name_not_equal_type = 50

        # when
        column_data = bp.get_column_data(column_name=column_name_not_equal_type)

        # then
        self.assertIsNone(column_data)

    def test_column_index_ok(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        column_index = 0

        # when
        column_data = bp.get_column_data(column_index=column_index)

        # then
        self.assertEqual([1, 2], column_data)

    def test_column_index_not_find(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        column_index_not_find = 100

        # when
        column_data = bp.get_column_data(column_index=column_index_not_find)

        # then
        self.assertIsNone(column_data)


class SetRowData(unittest.TestCase):
    def test_row_index_name_none_ok(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        set_row_data = [3]

        # when
        bp.set_row_data(set_row_data)
        
        # then
        self.assertEqual([3], bp.get_row_data(row_index=bp.get_row_index() - 1))

    def test_row_index_name_exist_ok(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        set_row_data = [3]

        # when
        bp.set_row_data(set_row_data, 'ㄷ')

        # then
        self.assertEqual([3], bp.get_row_data(row_name='ㄷ'))

    def test_data_over_column(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        set_row_data = [3, 33]
        
        # when
        # todo column 크기에 맞지 않는 데이터는 입력되지 않는다.
        #  1. 옵션을 제공해서 크기가 넘어가더라도 자동으로 column의 내용을 채우도록 한다
        #  2. 옵션은 굳이 넣지 않는다.
        bp.set_row_data(set_row_data, 'ㄷ')

        # then
        self.assertEqual([3, 33], bp.get_row_data(row_name='ㄷ'))


if __name__ == '__main__':
    unittest.main()
