from email_validator import validate_email, EmailNotValidError  # type: ignore
from typing import Union


def is_null_or_empty(valor: Union[str, int, float]) -> bool:
    return valor in [None, '', ' ']


def check_email(email: str) -> None:
    try:
        validate_email(email)
    except EmailNotValidError:
        raise ValueError("Invalid e-mail")
