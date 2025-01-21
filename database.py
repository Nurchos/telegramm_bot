import sqlite3


class ReviewsDatabase:
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
