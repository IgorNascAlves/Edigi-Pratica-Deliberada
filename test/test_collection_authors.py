import unittest

from src.author import Author
from src.collection_authors import CollectionAuthors


class TestCollectionAuthors(unittest.TestCase):

    def test_addAuthorWithSameEmail_RaiseException(self):

        name1 = 'Igor do Nascimento Alves'
        name2 = 'Catarina Becker Barrantes'

        email = 'igor.nascimento.flipe@gmail.com'

        author1 = Author(name1, email)
        author2 = Author(name2, email)

        collection = CollectionAuthors()
        collection.add(author1)

        self.assertRaises(Exception, collection.add, author2)


if __name__ == '__main__':
    unittest.main()
