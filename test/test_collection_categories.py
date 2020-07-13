import unittest

from src.category import Category
from src.collection_categories import CollectionCategories


class TestCollectionCategories(unittest.TestCase):

    def test_addCategoryWithSameName_RaiseException(self):

        name = 'Data Science'

        category1 = Category(name)
        category2 = Category(name)

        collection = CollectionCategories()
        collection.add(category1)

        self.assertRaises(Exception, collection.add, category2)


if __name__ == '__main__':
    unittest.main()
