from typing import List

from src.author import Author


class CollectionAuthors:
    def __init__(self):
        self.__lista: List[Author] = []

    def add(self, author: Author) -> None:
        if author in self.__lista:
            raise Exception("Author with same email already registered")
        self.__lista.append(author)

    def __len__(self):
        return len(self.__lista)
