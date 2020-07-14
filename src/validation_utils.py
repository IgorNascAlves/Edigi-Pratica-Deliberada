from email_validator import validate_email, EmailNotValidError  # type: ignore
from typing import Union
# import re


def is_it_null_ou_empty(valor: Union[str, int, float]) -> bool:
    return valor in [None, '', ' ']


def check_email(email: str) -> None:
    try:
        validate_email(email)
    except EmailNotValidError:
        raise ValueError("Invalid e-mail")


def validate_isbn(isbn: str) -> None:
    pass


def validate_if_start_with_one(edtion: str) -> None:
    pass
