from datetime import datetime as dt

from src.validation_utils import is_null_or_empty


class Category:
    def __init__(self, name: str):
        self.set_name(name)
        self.__time = str(dt.today())

    def set_name(self, name) -> None:
        if is_null_or_empty(name):
            raise ValueError("Name cannot be none")

        self.__name = name

    def __eq__(self, other):
        return other.__name == self.__name

    @property
    def time(self):
        return self.__time
