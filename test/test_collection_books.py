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

    def test_searchBookByTitle_return_BooksInfo(self):
        title = "Python to ML"
        text_search = "Py"

        book = Book(title, self.abstract, self.summary,
                    self.num_pages, self.isbn, self.author,
                    self.category, self.edition, self.price)

        collection = CollectionBooks()
        collection.add(book)

        result = collection.search(text_search)

        self.assertIsNotNone(result)

    def test_searchBookByTitle_return_MatchedBooks(self):
        title1 = "Python to ML"
        title2 = "Python to DS"
        text_search = "Py"

        book1 = Book(title1, self.abstract, self.summary,
                     self.num_pages, self.isbn, self.author,
                     self.category, self.edition, self.price)

        book2 = Book(title2, self.abstract, self.summary,
                     self.num_pages, self.isbn, self.author,
                     self.category, self.edition, self.price)

        collection = CollectionBooks()
        collection.add(book1)
        collection.add(book2)

        result = collection.search(text_search)

        self.assertEqual(2, len(result))

    def test_searchBookWithTitleShorterThan2chars_raiseException(self):
        title = "Python to ML"
        text_search = "P"

        book = Book(title, self.abstract, self.summary,
                    self.num_pages, self.isbn, self.author,
                    self.category, self.edition, self.price)

        collection = CollectionBooks()
        collection.add(book)

        self.assertRaises(Exception, collection.search, text_search)


if __name__ == '__main__':
    unittest.main()
