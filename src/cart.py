from src.book import Book
from src.sales import Sales

from datetime import datetime as dt
from typing import Dict, List


class Cart:
    def __init__(self):
        self.__items: List = []
        self.__time: str = ""

    def add(self, book: Book, amount: int) -> None:

        if amount < 1:
            raise Exception("You need to add at least one item")

        self.__items.append((book, amount))

    def calculate_the_total(self) -> int:
        total: int = 0
        for book, amount in self.__items:
            total += book.price * amount
        return total

    def close(self) -> Dict:

        resume = {item[0].title: item[1] for item in self.__items}

        resume['total'] = self.calculate_the_total()

        self.__time = str(dt.today().date())

        Sales(time=self.__time, resume=resume.copy())

        return resume
