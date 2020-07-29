from email_validator import validate_email, EmailNotValidError  # type: ignore
from typing import Union
import re


def is_it_null_ou_empty(valor: Union[str, int, float]) -> bool:
    return valor in [None, '', ' ']


def check_email(email: str) -> None:
    try:
        validate_email(email)
    except EmailNotValidError:
        raise ValueError("Invalid e-mail")


def validate_isbn(isbn: str) -> None:
    validate_if_star_with_978(isbn)
    validate_format(isbn)


def validate_if_star_with_978(isbn: str) -> None:
    br_code = '978'
    result = isbn[:3]
    if result != br_code:
        raise Exception("ISBN invalid - must star with " + br_code)


def validate_format(isbn: str) -> None:
    pattern = "[0-9]{3}.[0-9]{2}.[0-9]{5}.[0-9]{2}.[0-9]"
    result = re.fullmatch(pattern, isbn)
    if result is None:
        raise Exception("ISBN invalid - must have pattern xxx-xx-xxxxx-xx-x")


def validate_if_start_with_one(edtion: int) -> None:
    edtion_str = str(edtion)
    start_with_one = '1'
    result = edtion_str[0]
    if result != start_with_one:
        raise Exception("ISBN invalid - must star with " + start_with_one)
