import unittest

from src.cart import Cart
from src.book import Book
from src.collection_books import CollectionBooks


class TestCart(unittest.TestCase):

    def setUp(self) -> None:
        self.price = 20.00
        self.title = "Python to ML"
        self.book1 = Book(self.title, "*" * 500,
                          "introduction to python to ML", 50,
                          "978–85–33302-27–3", "Guilherme Silveira",
                          "Data Science", 11, self.price)

        self.collection = CollectionBooks()
        self.collection.add(self.book1)

    def test_closeCart_returnSuccess(self):
        cart = Cart(self.collection)
        amount = 6
        total = self.price * amount
        cart.add(self.title, amount)
        results = cart.close()
        self.assertEqual(total, results['total'])
        self.assertEqual(amount, results[self.title])

    def test_addInvalidBookInTheCart_RaiseException(self):
        cart = Cart(self.collection)
        amount = 6
        title = 'Wrong title'
        self.assertRaises(Exception, cart.add, title, amount)

    def test_add0ItemsInTheCart_RaiseException(self):
        cart = Cart(self.collection)
        amount = 0
        self.assertRaises(Exception, cart.add, self.title, amount)


if __name__ == '__main__':
    unittest.main()
