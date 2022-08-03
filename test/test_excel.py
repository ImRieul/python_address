import unittest

import pandas.core.frame

from main.excel import *


class ReadExcel(unittest.TestCase):
    def test_exist(self):
        # given
        file_exist = 'sample.xlsx'

        # when
        excel = Excel(file_exist)

        # then
        self.assertIsInstance(excel.sheet, pandas.core.frame.DataFrame)

    def test_not_exist(self):
        with self.assertRaises(FileNotFoundError):  # then
            # given
            file_not_exist = 'hello python'

            # when
            excel = Excel(file_not_exist)

    def test_type_not_str(self):  # str 타입이 아니면 None으로 들어가는 거 같다.
        with self.assertRaises(FileNotFoundError):  # then
            # given
            def not_str():
                pass

            # when
            Excel(not_str())

    def test_exist_sheet(self):
        # given
        file_exist = 'sample.xlsx'
        sheet_name = 'Sheet1'

        # when
        excel = Excel(file_exist, sheet_name=sheet_name)

        # then
        self.assertFalse(excel.sheet.empty)

    def test_not_exist_sheet(self):
        with self.assertRaises(ValueError):  # then
            # given
            file_exist = 'sample.xlsx'
            sheet_name = 'hello'

            # when
            Excel(file_exist, sheet_name=sheet_name)

    def test_in_index_row(self):
        # given
        file_exist = 'sample.xlsx'
        index_row = 1

        # when
        excel = Excel(file_exist, index_row=index_row)

        # then
        self.assertEqual(excel.get_index_row(), index_row)

    def test_over_index_row(self):
        with self.assertRaises(ValueError):  # then
            # given
            file_exist = 'sample.xlsx'
            index_row = 10000000000

            # when
            Excel(file_exist, index_row=index_row)

    def test_in_index_col(self):
        # given
        file_exist = 'sample.xlsx'
        index_col = 1

        # when
        excel = Excel(file_exist, index_col=index_col)

        # then
        self.assertEqual(excel.get_index_col(), index_col)

    def test_over_index_col(self):
        with self.assertRaises(IndexError):  # then
            # given
            file_exist = 'sample.xlsx'
            index_col = 10000000000

            # when
            Excel(file_exist, index_col=index_col)

    def test_over_index_row_and_col(self):
        with self.assertRaises(ValueError):  # then
            # given
            file_exist = 'sample.xlsx'
            index_row = 10000000000
            index_col = 10000000000

            # when
            Excel(file_exist, index_row=index_row, index_col=index_col)


if __name__ == '__main__':
    unittest.main()
