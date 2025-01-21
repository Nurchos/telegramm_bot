import sqlite3


class Database:
    def __init__(self, db_name="reviews.db"):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                contact TEXT,
                visit_date DATE,
                rate INTEGER,
                extra_comments TEXT
            )
        """)
        conn.commit()
        conn.close()

    def save_review_to_db(self, data: dict):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO reviews (name, contact, visit_date, rate, extra_comments)
            VALUES (?, ?, ?, ?, ?)
        """, (
            data.get("name"),
            data.get("contact"),
            data.get("visit_date"),
            data.get("rate"),
            data.get("extra_comments")
        ))
        conn.commit()
        conn.close()


class BooksDatabase:
    def __init__(self, db_name="books.db"):
        self.db_name = db_name
        self._connect()

    def _connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                year INTEGER,
                author TEXT,
                genre TEXT,
                price INTEGER
            )
        """)
        self.conn.commit()

    def save_book(self, name, year, author, genre, price):
        self.cursor.execute("""
            INSERT INTO books (name, year, author, genre, price)
            VALUES (?, ?, ?, ?, ?)
        """, (name, year, author, genre, price))
        self.conn.commit()

    def close(self):
        self.conn.close()
