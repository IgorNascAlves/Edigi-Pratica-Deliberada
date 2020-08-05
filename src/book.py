from datetime import datetime as dt
from re import fullmatch
from src.validation_utils import is_null_or_empty


class Book:
    def __init__(self, title: str, abstract: str, summary: str,
                 num_pages: int, isbn: str, author: str,
                 category: str, edition: int, price: float):
        self.set_title(title)
        self.set_abstract(abstract)
        self.set_summary(summary)
        self.set_num_pages(num_pages)
        self.set_isbn(isbn)
        self.set_edition(edition)
        self.set_price(price)

        self.author = author
        self.category = category
        self.__time = str(dt.today())

    def set_title(self, title: str) -> None:
        if is_null_or_empty(title):
            raise Exception("Title can not be empty or null")
        self.__title = title

    def set_abstract(self, abstract: str) -> None:
        size_abstract = len(abstract)
        minimum_size = 500
        if size_abstract < minimum_size:
            raise Exception("Abstract need to be higher than 500 characters")
        self.__abstract = abstract

    def set_summary(self, summary: str) -> None:
        if is_null_or_empty(summary):
            raise Exception("Summary can not be empty or null")
        self.__summary = summary

    def set_num_pages(self, num_pages: int) -> None:
        minimum_size = 0
        if num_pages <= minimum_size:
            raise Exception(f"Num pages need to be more than {minimum_size}")
        self.__num_pages = num_pages

    def set_isbn(self, isbn: str) -> None:
        self.__validate_isbn(isbn)
        self.__isbn = isbn

    def set_edition(self, edition: int) -> None:
        if str(edition)[0] != '1':
            raise Exception("ISBN invalid - must star with 1")
        self.__edition = edition

    def set_price(self, price: float) -> None:
        minimum_price = 0
        if price < minimum_price:
            raise Exception("Price need to be higher than 0 ")
        self.__price = price

    def __eq__(self, other):
        return other.__title == self.__title

    @property
    def title(self):
        return self.__title

    def __validate_isbn(self, isbn: str) -> None:
        pattern = "978.[0-9]{2}.[0-9]{5}.[0-9]{2}.[0-9]"
        result = fullmatch(pattern, isbn)
        if result is None:
            raise Exception("ISBN invalid - pattern 978-xx-xxxxx-xx-x")
