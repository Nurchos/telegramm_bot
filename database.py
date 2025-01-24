import sqlite3


class Database:
    def __init__(self, db_name="application.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self._init_tables()

    def _init_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                contact TEXT,
                visit_date DATE,
                rate INTEGER,
                extra_comments TEXT
            )
        """)
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

    def save_review(self, data: dict):
        self.cursor.execute("""
            INSERT INTO reviews (name, contact, visit_date, rate, extra_comments)
            VALUES (?, ?, ?, ?, ?)
        """, (
            data.get("name"),
            data.get("contact"),
            data.get("visit_date"),
            data.get("rate"),
            data.get("extra_comments")
        ))
        self.conn.commit()

    def get_reviews(self):
        self.cursor.execute("SELECT * FROM reviews")
        return self.cursor.fetchall()

    def save_book(self, name, year, author, genre, price):
        self.cursor.execute("""
            INSERT INTO books (name, year, author, genre, price)
            VALUES (?, ?, ?, ?, ?)
        """, (name, year, author, genre, price))
        self.conn.commit()

    def get_books(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books")
            return cursor.fetchall()

    def close(self):
        pass
