from src.collection_books import CollectionBooks

from datetime import datetime as dt
from typing import Dict, List


class Cart:
    def __init__(self, collection: CollectionBooks):
        self.__collection: CollectionBooks = collection
        self.__items: List = []
        self.__total: int = 0
        self.__time: str = ""

    def add(self, title, amount) -> None:
        if amount < 1:
            raise Exception("You need to add at least one item")
        book = self.__collection.get_book_infos(title)
        self.__items.append((self.__collection.get_book_infos(title), amount))
        self.__total += book.price * amount

    def close(self) -> Dict:
        resume = {item[0].title: item[1] for item in self.__items}
        resume['total'] = self.__total
        self.__time = str(dt.today())
        return resume
