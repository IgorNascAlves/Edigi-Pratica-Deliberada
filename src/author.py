from datetime import datetime as dt

from src.validation_utils import eh_nulo_ou_vazio, valida_email


class Author:
    def __init__(self, name, email):
        self.set_name(name)
        self.set_email(email)
        self.__time = str(dt.today())

    def set_name(self, name) -> None:
        if eh_nulo_ou_vazio(name):
            raise ValueError("Name cannot be none")

        self.__name = name

    def set_email(self, email) -> None:
        valida_email(email)
        self.__email = email

    def __eq__(self, other):
        return other.__email == self.__email

    @property
    def time(self):
        return self.__time
