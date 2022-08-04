class ExcelNotFindRowIndex(Exception):
    def __init__(self):
        super(ExcelNotFindRowIndex, self).__init__('Excel not find in excel row index')


class ExcelNotFindColumnIndex(Exception):
    def __init__(self):
        super(ExcelNotFindColumnIndex, self).__init__('Excel not find in excel column index')