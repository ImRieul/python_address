import pandas


class RowClass:
    def __init__(self, row: dict):
        self.empty = []
        self.__row: dict = row

    def __get__(self, instance, owner):
        # print(instance)
        return instance.rows_z

    def __set__(self, instance, value):
        # print(instance)
        print(value)
        pass


if __name__ == '__main__':
    row_class = RowClass([1, 2, 3])
    print(row_class.empty)
    print(row_class.row)