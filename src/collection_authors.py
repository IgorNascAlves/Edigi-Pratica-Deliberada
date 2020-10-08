from mysql.connector import connect, errors

from src.author import Author


class CollectionAuthors:

    def add_banco(self, author: Author) -> None:
        cnx = connect(user='root', database='DBEdigi', password='01234')
        cursor = cnx.cursor()

        add_author = ("insert into author "
                      "(fullname, email, instant) "
                      "VALUES (%s, %s, %s)")

        data_author = (author.name, author.email, author.instant)
        cursor.execute(add_author, data_author)

        try:
            cnx.commit()
        except errors.IntegrityError:
            raise Exception("Author with same email already registered")
        finally:
            cursor.close()
            cnx.close()
