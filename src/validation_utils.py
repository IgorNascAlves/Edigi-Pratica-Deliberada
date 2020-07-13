from email_validator import validate_email, EmailNotValidError  # type: ignore
from typing import Union


def eh_nulo_ou_vazio(valor: Union[str, int, float]) -> bool:
    return valor in [None, '', ' ']


def valida_email(email: str) -> None:
    try:
        validate_email(email)
    except EmailNotValidError:
        raise ValueError("Invalid e-mail")
