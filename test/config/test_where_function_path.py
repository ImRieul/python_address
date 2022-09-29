import unittest
from main.config import where_function_path


class TestWhereFunctionPath(unittest.TestCase):
    def test_out_deep_level(self):
        # given
        level = 10

        # when
        path = where_function_path(level)

        # then
        self.assertEqual('run', path)  # test Code에선 run, 모듈에선 <module>

    def test_not_int(self):
        with self.assertRaises(ValueError):  # then
            # given
            level = 'life is a short'

            # when
            path = where_function_path(level)

    def test_negative_number(self):
        # given
        level = -10

        # when
        path = where_function_path(level)

        # then
        self.assertEqual('where_function_path', path)

    def test_upper_call_function(self):
        # given
        level = 2

        def upper_function():
            return where_function_path(level)

        # when
        path = upper_function()

        # then
        self.assertEqual('test_upper_call_function', path)

    def test_now_call_function(self):
        # given
        level = 1  # default

        # when
        path = where_function_path(level)

        # then
        self.assertEqual('test_default', path)


if __name__ == '__main__':
    unittest.main()
