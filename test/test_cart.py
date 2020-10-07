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

        self.book2 = Book("Python to DS", "*" * 500,
                          "introduction to python to ML", 50,
                          "978–85–33302-27–3", "Guilherme Silveira",
                          "Data Science", 11, 30.0)

        self.collection = CollectionBooks()
        self.collection.add(self.book1)
        self.collection.add(self.book2)

    def test_closeCart_returnSuccess(self):
        cart = Cart()
        amount = 6
        total = self.price * amount
        cart.add(self.book1, amount)
        results = cart.close()
        self.assertEqual(total, results['total'])
        self.assertEqual(amount, results[self.title])

    def test_closeCartWithTwoBooks_returnSuccess(self):
        cart = Cart()
        amount_1 = 2
        amount_2 = 3
        total = self.book1.price * amount_1 + self.book2.price * amount_2

        cart.add(self.book1, amount_1)
        cart.add(self.book2, amount_2)
        results = cart.close()

        self.assertEqual(total, results['total'])

    def test_add0ItemsInTheCart_RaiseException(self):
        cart = Cart()
        amount = 0
        self.assertRaises(Exception, cart.add, self.book1, amount)


if __name__ == '__main__':
    unittest.main()
