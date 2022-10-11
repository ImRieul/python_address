import pandas


class RowClass:
    def __init__(self, data: pandas.DataFrame):
        self.empty = []
        self._data: pandas.DataFrame = data
        # index가 숫자 0~ 있으면 굳이 만들 필요가 없다.
        self._row: dict = pandas.DataFrame(self._data.to_dict('index')).to_dict('list')
        self._column: dict = {}

    # RowClass().row()[row] 이렇게 써야하는 불편함이 있음
    #   -> 함수의 결과를 변수로 저장하자.
    #   -> 실행되는 함수에서 _check_data 실행
    @property
    def row(self) -> dict:
        self._check_data()
        index_to_number = {index: value for index, value in enumerate(self._row.values())}
        self._row.update(index_to_number)

        return self._row

    def _check_data(self):
        pass


if __name__ == '__main__':
    df = pandas.DataFrame({'a': [1, 2], 'b': [3, 4]})
    row_class = RowClass(df)
    print(1, row_class.row[1])
    row_class.row[1] = [22, 44]
    print(2, row_class.row[1])

    # df.equelr
