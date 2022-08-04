import unittest

import pandas

from main.pandas_crud import BasePandas


class BasePandasData(unittest.TestCase):
    def test_ok(self):
        # given
        check_data = pandas.DataFrame({'a': [1], 'b': [2]})

        # when
        base_pandas = BasePandas().data

        # then
        self.assertEqual(base_pandas.to_dict(), check_data.to_dict())


if __name__ == '__main__':
    unittest.main()