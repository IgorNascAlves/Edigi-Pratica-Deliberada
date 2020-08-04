import unittest

from src.book import Book


class MyTestCase(unittest.TestCase):

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

    def test_createBook_return_Book(self):
        book1 = Book(self.title, self.abstract, self.summary,
                     self.num_pages, self.isbn, self.author,
                     self.category, self.edition, self.price)
        self.assertIsNotNone(book1)

    def test_createBookWithFreePrice_return_Book(self):
        price = 0
        book1 = Book(self.title, self.abstract, self.summary,
                     self.num_pages, self.isbn, self.author,
                     self.category, self.edition, price)
        self.assertIsNotNone(book1)

    def test_createBookWithNoneTitle_raise_Exception(self):
        title = None
        self.assertRaises(Exception, Book, title, self.abstract,
                          self.summary, self.num_pages, self.isbn, self.author,
                          self.category, self.edition, self.price)

    def test_createBookWithShortAbstract_raise_Exception(self):
        abstract = "*" * 499
        self.assertRaises(Exception, Book, self.title, abstract,
                          self.summary, self.num_pages, self.isbn, self.author,
                          self.category, self.edition, self.price)

    def test_createBookWithNoneSummary_raise_Exception(self):
        summary = None
        self.assertRaises(Exception, Book, self.title, self.abstract,
                          summary, self.num_pages, self.isbn, self.author,
                          self.category, self.edition, self.price)

    def test_createBookWithZeroPages_raise_Exception(self):
        num_pages = 0
        self.assertRaises(Exception, Book, self.title, self.abstract,
                          self.summary, num_pages, self.isbn, self.author,
                          self.category, self.edition, self.price)

    def test_createBookWithInvalidISBN_raise_Exception(self):
        isbn = "123–85–33302-27–3"
        self.assertRaises(Exception, Book, self.title, self.abstract,
                          self.summary,  self.num_pages, isbn, self.author,
                          self.category, self.edition, self.price)

    def test_createBookWithInvalidEdition_raise_Exception(self):
        edition = 21
        self.assertRaises(Exception, Book, self.title, self.abstract,
                          self.summary,  self.num_pages, self.isbn,
                          self.author, self.category, edition, self.price)

    def test_createBookWithInvalidPrice_raise_Exception(self):
        price = -20
        self.assertRaises(Exception, Book, self.title, self.abstract,
                          self.summary,  self.num_pages, self.isbn,
                          self.author, self.category, self.edition, price)


if __name__ == '__main__':
    unittest.main()
