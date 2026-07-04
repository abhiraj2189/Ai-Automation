import sqlite3
from pathlib import Path

# Project Root
ROOT = Path(__file__).resolve().parents[2]

# Database Path
DB_PATH = ROOT / "database" / "ai_automation.db"


class Database:

    def __init__(self):
        # timeout: agar DB kisi aur connection se locked hai, 5 sec tak wait karega
        # bajaye turant "database is locked" error dene ke
        self.connection = sqlite3.connect(DB_PATH, timeout=5)
        self.cursor = self.connection.cursor()

        # WAL mode: reads aur writes ko ek doosre ko block karne se rokta hai,
        # locking errors kaafi kam ho jaate hain
        self.cursor.execute("PRAGMA journal_mode=WAL;")

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT DEFAULT 'user',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS ai_tools(

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            category TEXT,
            website TEXT

        )
        """)

        self.connection.commit()

    def get_user_by_email(self, email):

        self.cursor.execute(
            """
            SELECT * FROM users
            WHERE email = ?
            """,
            (email,)
        )

        return self.cursor.fetchone()

    def close(self):
        self.connection.close()

    # --- Context manager support: "with Database() as db:" ---
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Agar block ke andar error aaya to rollback, warna already commit ho chuka hoga
        if exc_type is not None:
            self.connection.rollback()
        self.close()
        # False return karne se original error upar propagate hoga (suppress nahi hoga)
        return False