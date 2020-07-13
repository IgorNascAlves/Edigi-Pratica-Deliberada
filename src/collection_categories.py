from typing import List

from src.category import Category


class CollectionCategories:
    def __init__(self):
        self.__lista: List[Category] = []

    def add(self, category: Category) -> None:
        if category in self.__lista:
            raise Exception("Category with same name already registered")
        self.__lista.append(category)
