from datetime import datetime as dt

from src.validation_utils import is_it_null_ou_empty, validate_isbn,\
    validate_if_start_with_one


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
        if is_it_null_ou_empty(title):
            raise Exception("Title can not be empty or null")
        self.title = title

    def set_abstract(self, abstract: str) -> None:
        size_abstract = len(abstract)
        minimum_size = 500
        if size_abstract < minimum_size:
            raise Exception("Abstract need to be higher than 500 characters")
        self.abstract = abstract

    def set_summary(self, summary: str) -> None:
        if is_it_null_ou_empty(summary):
            raise Exception("Summary can not be empty or null")
        self.summary = summary

    def set_num_pages(self, num_pages: int) -> None:
        minimum_size = 0
        if num_pages < minimum_size:
            raise Exception("Num pages need to be >= than 0 pages")
        self.num_pages = num_pages

    def set_isbn(self, isbn: str) -> None:
        if validate_isbn(isbn):
            raise Exception("ISBN start with 978 format xxx-xx-xxxxx-xx-x")
        self.isbn = isbn

    def set_edition(self, edition: int) -> None:
        if validate_if_start_with_one(edition):
            raise Exception("Edition need to start with 1")
        self.edition = edition

    def set_price(self, price: float) -> None:
        minimum_price = 0
        if price < minimum_price:
            raise Exception("Price need to be higher than 0 ")
        self.price = price
