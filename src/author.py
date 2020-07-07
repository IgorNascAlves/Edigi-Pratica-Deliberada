from datetime import datetime as dt
from email_validator import validate_email, EmailNotValidError  # type: ignore


class Author:
    def __init__(self, name, email):
        self.set_name(name)
        self.set_email(email)
        self.__time = str(dt.today())

    def set_name(self, name) -> None:
        if name in ['', ' ', None]:
            raise ValueError("Name cannot be none")

        self.__name = name

    def set_email(self, email) -> None:
        try:
            valid = validate_email(email)
        except EmailNotValidError:
            raise ValueError("Invalid e-mail")
        else:
            self.__email = valid.email

    def __eq__(self, other):
        return other.email == self.email

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def time(self):
        return self.__time
