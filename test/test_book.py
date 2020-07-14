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
        self.edition = 1
        self.price = 20.00

    def test_createBook_return_Book(self):
        book1 = Book(self.title, self.abstract, self.summary,
                     self.num_pages, self.isbn, self.author,
                     self.category, self.edition, self.price)
        self.assertIsNotNone(book1)


if __name__ == '__main__':
    unittest.main()
