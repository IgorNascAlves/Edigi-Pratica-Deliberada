from typing import List
from mysql.connector import connect

from src.author import Author


class CollectionAuthors:
    def __init__(self):
        self.__lista: List[Author] = []

    def add(self, author: Author) -> None:
        if author in self.__lista:
            raise Exception("Author with same email already registered")
        self.__lista.append(author)

    def add_banco(self, author: Author) -> None:
        cnx = connect(user='root', database='DBEdigi', password='01234')
        cursor = cnx.cursor()

        add_author = ("insert into author "
                      "(fullname, email, instant) "
                      "VALUES (%s, %s, %s)")

        data_author = (author.name, author.email, author.instant)
        cursor.execute(add_author, data_author)

        cnx.commit()
        cursor.close()
        cnx.close()
