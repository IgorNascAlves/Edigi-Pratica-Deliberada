import unittest

from src.book import Book
from src.collection_books import CollectionBooks


class TestCollectionBooks(unittest.TestCase):

    def setUp(self):
        self.title = "Python to ML"
        self.abstract = "*" * 500
        self.summary = "introduction to python to ML"
        self.num_pages = 50
        self.isbn = "978–85–33302-27–3"
        self.author = "Guilherme Silveira"
        self.category = "Data Science"
        self.edition = 11
        self.price = 20.00

    def test_addBookWithSameTitle_RaiseException(self):

        title = "Python to ML"

        book1 = Book(title, self.abstract, self.summary,
                     self.num_pages, self.isbn, self.author,
                     self.category, self.edition, self.price)

        book2 = Book(title, self.abstract, self.summary,
                     self.num_pages, self.isbn, self.author,
                     self.category, self.edition, self.price)

        collection = CollectionBooks()
        collection.add(book1)

        self.assertRaises(Exception, collection.add, book2)


if __name__ == '__main__':
    unittest.main()
