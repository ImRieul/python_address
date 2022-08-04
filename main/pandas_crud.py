import pandas


class BasePandas:
    def __init__(self):
        self.data: pandas.DataFrame = self.__read()

    def __read(self) -> pandas.DataFrame:
        pass
