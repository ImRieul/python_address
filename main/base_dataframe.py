import pandas

from main.personal import tools


class BaseDataFrame:
    def __init__(self, dataframe: pandas.DataFrame):
        self._dataframe: pandas.DataFrame = dataframe
        self._row: dict = self._set_row()
        self._column: dict = self._set_column()
        # self._row: WithDict = WithDict(self._set_row())
        # self._column: WithDict = WithDict(self._set_column())

    @property
    def row(self) -> dict:
        self._update_dataframe()
        return self._row

    @property
    def column(self) -> dict:
        self._update_dataframe()
        return self._column

    def _update_dataframe(self):
        update_row = tools.dataframe_change_column_index(
            pandas.DataFrame(self._row),
            columns=list(self._dataframe.columns),
        )
        update_column = pandas.DataFrame(
            self._column,
            columns=list(self._dataframe.columns),
        )

        if not self._dataframe.equals(update_row):
            self._dataframe.update(update_row)

            if not self._dataframe.index.equals(update_row.index):
                for index in self._dataframe.index:
                    update_row.drop(index=index, inplace=True)

                self._dataframe = pandas.concat([self._dataframe, update_row])

            self._column = self._set_column()

        elif not self._dataframe.equals(update_column):
            self._dataframe.update(update_column)

            if not self._dataframe.columns.equals(update_column.columns):
                for column in self._dataframe.columns:
                    update_column.drop(columns=column, inplace=True)

                self._dataframe = pandas.concat([self._dataframe, update_column])

            self._row = self._set_row()

    def _set_row(self):
        result = {}
        result.update(self._index_to_dict_key_name())
        result.update(self._index_to_dict_key_number())
        return result

    def _set_column(self):
        result = {}
        result.update(self._column_to_dict_key_name())
        result.update(self._column_to_dict_key_index())
        return result

    def _index_to_dict_key_name(self) -> dict:
        return pandas.DataFrame(self._dataframe.to_dict('index')).to_dict('list')

    def _index_to_dict_key_number(self) -> dict:
        return {index: value for index, value in enumerate(self._index_to_dict_key_name().values())}

    def _column_to_dict_key_name(self) -> dict:
        return self._dataframe.to_dict('list')

    def _column_to_dict_key_index(self) -> dict:
        return {index: value for index, value in enumerate(self._column_to_dict_key_name().values())}

    def __call__(self):
        self._update_dataframe()
        return self._dataframe


class WithDict(dict):
    def __init__(self, dic: dict):
        super(WithDict, self).__init__(dic)

    def __setitem__(self, key, value):
        """
        기존의 dict는 __setitem__을 이용해 key와 value를 저장할 수 없었습니다.
        BaseDataFrame의 간편한 사용을 위해 __setitem__으로도 저장할 수 있게 수정합니다.
        -> ,, 원래 있는 기능이였다,, 그래도 매직 메소드를 공부한 기념으로 옮겨야겠다.

        :param key: 저장할 키
        :param value: 저장할 값
        """
        # if self.get(key) is None:
        #     super(WithDict, self.update({key: value})
        # else:
        #     super(WithDict, self).__setitem__(key, value)


if __name__ == '__main__':
    df = pandas.DataFrame({'a': [1, 2], 'b': [3, 4], 'c': [5, 6]})
    bdf = BaseDataFrame(df)

    print(bdf())
    bdf.row[1] = [22, 44, 66]
    print(bdf())
    bdf.row[33] = [33, 33, 33]
    print(bdf())

    bdf.column['d'] = [7, 8, 33]
    print(bdf())
