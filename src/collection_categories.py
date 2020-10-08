from mysql.connector import connect,  errors

from src.category import Category


class CollectionCategories:

    def add_banco(self, category: Category) -> None:
        cnx = connect(user='root', database='DBEdigi', password='01234')
        cursor = cnx.cursor()

        add_category = ("insert into category "
                        "(name, instant) "
                        "VALUES (%s, %s)")

        data_category = (category.name, category.instant)
        cursor.execute(add_category, data_category)

        try:
            cnx.commit()
        except errors.IntegrityError:
            raise Exception("Category with same name already registered")
        finally:
            cursor.close()
            cnx.close()
