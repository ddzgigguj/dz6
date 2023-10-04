import sqlite3
from pathlib import Path


def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent.parent / "db.sqlite3")
    cursor = db.cursor()
def create_tables():
    cursor.execute(
        """
        DROP TABLE IF EXISTS product
        """
    )
    cursor.execute(
        """
       DROP TABLE IF EXISTS category
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS product (
            productId INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price FLOATprice FLOAT,
            categoryId INTEGER,
            FOREIGN KEY (categoryId) REFERENCES category (id)
        )
        """
    )

    cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS subscrebu (
    ID INTEGER PRIMARY KEY AUTOINCREMENT
    
    )
    ''')


    db.commit()
def populate_tables():
    cursor.execute(
        """
        INSERT INTO product (name, price)
        VALUES  ('Манга', 25.0),
                ('Манхва', 19.0),
                ('Манихува', 26.0)
        """
    )
    cursor.execute(
        """
        INSERT INTO product (name, price, categoryId)
        VALUES ('Атака Титанов', 25.0, 1),
                ('Клинок рассикающий демонов', 25, 1),
                ('Ветролом', 19.0, 2),
                ('Ранкер живуший второй раз', 19.0, 2),
                ('Пик боевых исскуств', 26.0, 3),
                ('Приключение Доната в Другом мире', 26.0, 3)
        """
    )
    db.commit()

def subscrebu(user_id):
    cursor.execute(
        """INSERT INTO subscrebu(ID)
        VALUES (:user_id)""",
        {"user_id":user_id},
    )
    db.commit()

def get_products():
    cursor.execute(
        """
        SELECT p.name, c.name FROM product p JOIN category c ON p.categoryId = c.id
        """
    )
    return cursor.fetchall()
def get_product_by_category(category_id):
    cursor.execute(
        """
        SELECT * FROM product WHERE categoryId = :c_id
        """,
        {"c_id": category_id},
    )
    return cursor.fetchall()


def select_sub():
    cursor.execute('''SELECT ID FROM subscrebu''')
    users = cursor.fetchall()
    users_id = [user for user in users]
    return users_id
    return [user for user in cursor.fetchall()]


if __name__ == "__main__":
    init_db()
    create_tables()
    populate_tables()