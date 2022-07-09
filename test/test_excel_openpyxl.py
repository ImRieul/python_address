import os
import unittest

from main.excel_openpyxl import *
from error.error_excel import *

# os.chdir('../')
test_file_name = 'sample.xlsx'
test_not_file_name = 'Hello python'
excel = Excel(test_file_name)


class ExcelReadExcelTest(unittest.TestCase):
    def test_exist(self):
        self.assertEqual(excel.get_file_name(), test_file_name)

    def test_not_exist(self):
        excel_not_exist_name = 'not_exist_file.xlsx'
        excel_not_exist = Excel(excel_not_exist_name)
        self.assertEqual(excel_not_exist.get_file_name(), excel_not_exist_name)
        os.remove(f'{setting.ROOT_PROJECT}/{excel_not_exist_name}'
                  if platform.system() != 'Windows'
                  else f'{setting.ROOT_PROJECT}\\{excel_not_exist_name}')

    def test_not_exist_read_only(self):
        excel_not_exist_name = 'not_exist_file.xlsx'
        with self.assertRaises(FileNotFoundError):
            Excel(excel_not_exist_name, read_only=True)

    def test_name_not_str(self):
        def test_func():
            pass
        with self.assertRaises(ExcelFileNameTypeError):
            Excel(test_func)


class ExcelFileTest(unittest.TestCase):
    def test_not_equal_name(self):
        self.assertEqual(excel.get_file_name(), test_file_name)

    def test_equal_name(self):
        self.assertEqual(excel.get_file_name(), test_file_name)


class ExcelSheetTest(unittest.TestCase):
    # get_sheet_name
    def test_get_sheet_name__active(self):
        sheet_input_name = 'data'
        sheet_name = excel.get_sheet_name()
        self.assertEqual(sheet_name, sheet_input_name)

    def test_get_sheet_name__exist(self):
        sheet_input_name = 'data'
        sheet_name = excel.get_sheet_name(sheet_input_name)
        self.assertEqual(sheet_name, sheet_input_name)

    def test_get_sheet_name__not_exist(self):
        sheet_input_name = 'hello python'
        with self.assertRaises(KeyError):
            excel.get_sheet_name(sheet_input_name)

    # get_sheet_names
    def test_get_sheet_names__not_type(self):
        self.assertNotIsInstance(excel.get_sheet_names(), str)

    def test_get_sheet_names__in_sheet(self):
        self.assertIsInstance(excel.get_sheet_names(), list)

    def test_get_sheet_names__in_not_sheet(self):
        sheet_name = 'Hello python'
        self.assertFalse(sheet_name in excel.get_sheet_names())

    # def test_active_sheet__name_None(self):
        # self.assertEqual(excel.get_sheet_active())


if __name__ == '__main__':
    unittest.main()
