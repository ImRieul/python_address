import unittest

import pandas.core.frame

from main.excel import *


file_exist = 'sample.xlsx'
file_not_exist = 'hello python'


class NewExcel(unittest.TestCase):
    def test_read_excel__exist(self):
        excel = Excel(file_exist)
        self.assertIsInstance(excel.sheet, pandas.core.frame.DataFrame)

    def test_read_excel__not_exist(self):
        with self.assertRaises(FileNotFoundError):
            excel = Excel(file_not_exist)

    def test_read_excel__type_not_str(self):  # str 타입이 아니면 None으로 들어가는 거 같다.
        def not_str():
            pass
        with self.assertRaises(FileNotFoundError):
            excel = Excel(not_str())

    # sheet_name value
    def test_read_excel__exist_sheet(self):
        excel = Excel(file_exist, sheet_name='data')
        self.assertFalse(excel.sheet.empty)

    def test_read_excel__not_exist_sheet(self):
        with self.assertRaises(ValueError):
            excel = Excel(file_exist, sheet_name='hello')

    # index
    def test_read_excel__in_index_row(self):
        excel = Excel(file_exist, index_row=1)
        self.assertFalse(excel.sheet.empty)

    def test_read_excel__in_not_index_row(self):
        with self.assertRaises(ValueError):
            excel = Excel(file_exist, index_row=10000)

    def test_read_excel__in_index_col(self):
        excel = Excel(file_exist, index_col=1)
        self.assertFalse(excel.sheet.empty)

    def test_read_excel__in_not_index_col(self):
        with self.assertRaises(IndexError):
            excel = Excel(file_exist, index_col=10000)


if __name__ == '__main__':
    unittest.main()
