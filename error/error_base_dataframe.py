class ExcelNotEqualColumnLength(Exception):
    def __init__(self, error_list, column_list):
        super(ExcelNotEqualColumnLength, self).__init__(
            f"Not equal length in search column\n"
            f"value column: {error_list}\n"
            f"class column: {column_list}"
        )


class ExcelNotEqualRowLength(Exception):
    def __init__(self, error_list, column_list):
        super(ExcelNotEqualRowLength, self).__init__(
            f"Not equal length in search row\n"
            f"value column: {error_list}\n"
            f"class column: {column_list}"
        )

