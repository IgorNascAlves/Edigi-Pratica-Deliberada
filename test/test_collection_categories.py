import unittest
from mysql.connector import errors

from src.category import Category
from src.collection_categories import CollectionCategories


class TestCollectionCategories(unittest.TestCase):

    def test_addCategoryWithSameName_RaiseException(self):

        name = 'Data Science'

        category1 = Category(name)
        category2 = Category(name)

        collection = CollectionCategories()
        try:
            collection.add_banco(category1)
        except errors.IntegrityError:
            pass
        finally:
            self.assertRaises(Exception, collection.add_banco, category2)


if __name__ == '__main__':
    unittest.main()
