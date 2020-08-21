from src.book import Book

from datetime import datetime as dt
from typing import Dict, List


class Cart:
    def __init__(self):
        self.__items: List = []
        self.__total: int = 0
        self.__time: str = ""

    def add(self, book: Book, amount: int) -> None:

        if amount < 1:
            raise Exception("You need to add at least one item")

        self.__items.append((book, amount))

    def calculate_the_total(self):
        for book, amount in self.__items:
            self.__total += book.price * amount

    def close(self) -> Dict:

        resume = {item[0].title: item[1] for item in self.__items}

        self.calculate_the_total()
        resume['total'] = self.__total

        self.__time = str(dt.today())

        return resume
