from typing import List

from src.book import Book


class CollectionBooks:
    def __init__(self):
        self.__lista: List[Book] = []

    def add(self, book: Book) -> None:
        if book in self.__lista:
            raise Exception("Book with same title already registered")
        self.__lista.append(book)
