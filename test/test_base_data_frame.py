import unittest

import pandas

from error.error_base_dataframe import *
from main.base_data_frame import BaseDataFrame


class testBaseDataFrame(BaseDataFrame):
    def __init__(self, df_dataframe: pandas.DataFrame):
        super().__init__(df_dataframe)

    def append_over_row_data(self, over_row: int) -> None:
        super()._append_column(over_row)


class GetRowIndex(unittest.TestCase):
    def test_ok(self):
        # given
        df = pandas.DataFrame({'a': [1, 2]})
        bp = BaseDataFrame(df)

        # when
        row_index = bp.get_row_size()

        # then
        self.assertEqual(row_index, 2)

    def test_this_column_index(self):
        # given
        df = pandas.DataFrame({'a': [1], 'b': [2], 'c': [3]})
        bp = BaseDataFrame(df)

        # when
        row_index = bp.get_row_size()

        # then
        self.assertNotEqual(row_index, 3)


class GetColumnIndex(unittest.TestCase):
    def test_ok(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame({
            'a': [1], 'b': [2]
        }))

        # when
        column_index = bp.get_column_size()

        # then
        self.assertEqual(column_index, 2)

    def test_this_row_index(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame({
            'a': [1, 2, 3]
        }))

        # when
        column_index = bp.get_column_size()

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


class GetRowIndexToName(unittest.TestCase):
    def test_ok(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))

        # when
        get_row_name_index = bp.get_row_index('ㄱ')

        # then
        self.assertEqual(0, get_row_name_index)

    def test_input_row_index(self):
        with self.assertRaises(ValueError):  # then
            # given
            bp = BaseDataFrame(pandas.DataFrame(
                data={'a': [1, 2]},
                index=['ㄱ', 'ㄴ'],
            ))

            # when
            bp.get_row_index(0)


class GetColumnIndexToName(unittest.TestCase):
    def test_ok(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))

        # when
        get_column_name_index = bp.get_column_index('a')

        # then
        self.assertEqual(0, get_column_name_index)

    def test_input_column_index(self):
        with self.assertRaises(ValueError):  # then
            # given
            bp = BaseDataFrame(pandas.DataFrame(
                data={'a': [1, 2]},
                index=['ㄱ', 'ㄴ'],
            ))

            # when
            bp.get_column_index(0)


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


class SetRowDataToName(unittest.TestCase):
    def test_ok(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        set_row_data = [3]

        # when
        bp.set_row_data_from_name(set_row_data)

        # then
        self.assertEqual(set_row_data, bp.get_row_data(row_index=2))


class SetRowData(unittest.TestCase):
    # todo 테스트 한 것들
    #  1. 데이터 수정
    #  2. column이 초과됐으면 컬러 생성
    #  3. column index를 기준으로 데이터 입력
    def test_row_name_ok(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        set_row_data = [3]

        # when
        bp.set_row_data_from_name(set_row_data, row_name='ㄷ')

        # then
        self.assertEqual([3], bp.get_row_data(row_name='ㄷ'))

    def test_row_name_exist(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        set_row_data = [3]

        # when
        bp.set_row_data_from_name(set_row_data, row_name='ㄱ')

        # then
        self.assertEqual([3], bp.get_row_data(row_name='ㄱ'))

    def test_over_column_set_true__row_name(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        set_row_data = [3, 33]

        # when
        bp.set_row_data(set_row_data, row_name='ㄷ', over_column=True)

        # then
        self.assertEqual([3, 33], bp.get_row_data(row_name='ㄷ'))

    def test_over_column_set_false__row_name(self):
        with self.assertRaises(BaseDataFrameSetOverRow):  # then
            # given
            bp = BaseDataFrame(pandas.DataFrame(
                data={'a': [1, 2]},
                index=['ㄱ', 'ㄴ'],
            ))
            set_row_data = [3, 33]

            # when
            bp.set_row_data(set_row_data, row_name='ㄷ', over_column=False)

    def test_over_column_set_true__row_index(self):
        # given
        bp = BaseDataFrame(pandas.DataFrame(
            data={'a': [1, 2]},
            index=['ㄱ', 'ㄴ'],
        ))
        set_row_data = [3, 33]

        # when
        bp.set_row_data(set_row_data, row_index=2, over_column=True)

        # then
        self.assertEqual([3, 33], bp.get_row_data(row_index=2))

    def test_over_column_set_false__row_index(self):
        with self.assertRaises(BaseDataFrameSetOverRow):  # then
            # given
            bp = BaseDataFrame(pandas.DataFrame(
                data={'a': [1, 2]},
                index=['ㄱ', 'ㄴ'],
            ))
            set_row_data = [3, 33]

            # when
            bp.set_row_data(set_row_data, row_index=2, over_column=False)


if __name__ == '__main__':
    unittest.main()
