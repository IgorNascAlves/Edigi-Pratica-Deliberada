import unittest
from datetime import datetime as dt

from src.author import Author


class TestCaseAuthor(unittest.TestCase):

    def test_CreateAuthor_InstantSave(self):
        name = 'Igor do Nascimento Alves'
        email = 'igor.nascimento.flipe@gmail.com'
        author1 = Author(name, email)
        self.assertEqual(str(dt.today().date()), author1.instant)

    def test_CreateAuthor_NoneName_RaiseException(self):
        name = None
        email = 'igor.nascimento.flipe@gmail.com'
        self.assertRaises(ValueError, Author, name, email)

    def test_CreateAuthor_InvalidEmail_RaiseException(self):
        name = 'Igor do Nascimento Alves'
        email = 'igor.nascimento.flipe@.com'
        self.assertRaises(ValueError, Author, name, email)


if __name__ == '__main__':
    unittest.main()
