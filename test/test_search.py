import unittest
from main.search import *


# search_yourself
class CuttingData(unittest.TestCase):
    def test_ok(self):
        search = Search(['number', 'alphabet'])
        input_data = [1, 'a']
        search.cutting_data(input_data)
        self.assertEqual(list(search.box.loc[0]), input_data)


if __name__ == '__main__':
    unittest.main()
