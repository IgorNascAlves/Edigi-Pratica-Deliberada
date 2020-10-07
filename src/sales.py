from typing import Dict


class Sales:
    def __init__(self, time, resume: Dict, id_sale=0):
        self.__id_sale = id_sale
        self.__time: str = time
        self.__resume = resume
        self.save_sale()

    def save_sale(self):
        del self.__resume['total']
        for book in self.__resume:
            id_book = self.__find_id(book)
            print(f"ID_sale: {self.__id_sale} Amount: {self.__resume[book]}")
            print(f"ID_book: {id_book} Time: {self.__time}")

    def __find_id(self, book):
        return 0
