from typing import List

from src.book import Book


class CollectionBooks:
    def __init__(self):
        self.__lista: List[Book] = []

    def add(self, book: Book) -> None:
        if book in self.__lista:
            raise Exception("Book with same title already registered")
        self.__lista.append(book)

    def search(self, text_search: str) -> List:
        if len(text_search) < 2:
            raise Exception("Need to have at least two characters")
        if text_search not in self.__lista:
            raise Exception(text_search + " not found")
        matching = [s for s in self.__lista if text_search == s]
        return matching
