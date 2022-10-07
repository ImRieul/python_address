class RowClass:
    def __init__(self, row: list):
        self.empty = []
        self.__row: list = row

    @property
    def row(self) -> list:
        return self.__row

    @row.setter
    def row(self, value):
        self.__row = value

    def __str__(self):
        return self.__row

    def __call__(self, *args, **kwargs):
        return self.__row

    def __len__(self):
        return len(self.__row)