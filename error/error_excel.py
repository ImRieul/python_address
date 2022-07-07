# class ExcelSheetNameEmpty(Exception):
#     def __init__(self):
#         super(ExcelSheetNameEmpty, self).__init__('Excel sheet name can\'t not empty')


class ExcelFileNameTypeError(Exception):
    def __init__(self):
        super(ExcelFileNameTypeError, self).__init__('Excel file name type is only str')


class ExcelSheetNameTypeError(Exception):
    def __init__(self):
        super(ExcelSheetNameTypeError, self).__init__('Excel file name type is only str')
