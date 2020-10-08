import unittest
from datetime import datetime as dt

from src.category import Category


class MyTestCategory(unittest.TestCase):

    def test_CreateCategory_TimeSave(self):
        name = 'Data Science'
        category = Category(name)
        self.assertEqual(str(dt.today().date()), category.instant)

    def test_CreateCategory_NoneName_RaiseException(self):
        name = None
        self.assertRaises(ValueError, Category, name)


if __name__ == '__main__':
    unittest.main()
