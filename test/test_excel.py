import os
import unittest

from main.excel import *
from error.error_excel import *

# os.chdir('../')
test_excel_file_name = 'sample.xlsx'
excel = Excel(test_excel_file_name)


class ExcelReadExcelTest(unittest.TestCase):
    def test_exist(self):
        self.assertEqual(excel.get_excel_name(), test_excel_file_name)

    def test_not_exist(self):
        excel_not_exist_name = 'not_exist_file.xlsx'
        excel_not_exist = Excel(excel_not_exist_name)
        self.assertEqual(excel_not_exist.get_excel_name(), excel_not_exist_name)
        os.remove(setting.ROOT_PROJECT + f'/{excel_not_exist_name}')

    def test_not_exist_read_only(self):
        excel_not_exist_name = 'not_exist_file.xlsx'
        with self.assertRaises(FileNotFoundError):
            Excel(excel_not_exist_name, read_only=True)

    def test_name_not_str(self):
        def test_func():
            pass
        with self.assertRaises(ExcelFileNameTypeError):
            Excel(test_func)


class ExcelGetSheetName(unittest.TestCase):
    def test_default(self):
        sheet_name = excel.get_sheet_name()
        self.assertEqual(sheet_name, 'data')

    def test_input_exist(self):
        sheet_input_name = 'data'
        sheet_name = excel.get_sheet_name(sheet_input_name)
        self.assertEqual(sheet_name, sheet_input_name)

    def test_input_not_exist(self):
        sheet_input_name = 'hello python'
        with self.assertRaises(KeyError):
            excel.get_sheet_name(sheet_input_name)


# class ExcelSetSheetName(unittest.TestCase):
#     def test_empty_name(self):
#         excel = Excel(test_excel_file_name)
#         sheet_name = excel.get_sheet_name()
#
#         excel.set_sheet_name('with_test')


if __name__ == '__main__':
    unittest.main()
