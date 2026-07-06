import sqlite3
from pathlib import Path

# Project Root
ROOT = Path(__file__).resolve().parents[2]

# Database Path
DB_PATH = ROOT / "database" / "ai_automation.db"


class Database:

    def __init__(self):
        self.connection = sqlite3.connect(DB_PATH, timeout=5)
        self.cursor = self.connection.cursor()

        # Enable WAL Mode
        self.cursor.execute("PRAGMA journal_mode=WAL;")

    def create_tables(self):

        # ==========================
        # Users Table
        # ==========================
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

        # ==========================
        # AI Tools Table
        # ==========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS ai_tools(

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            category TEXT,
            website TEXT

        )
        """)

        # ==========================
        # Notes Table
        # ==========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes(

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(user_id) REFERENCES users(id)

        )
        """)

        # ==========================
        # Favorites Table
        # ==========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS favorites(

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            tool_name TEXT NOT NULL,
            website TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(user_id) REFERENCES users(id)

        )
        """)

        # ==========================
        # Chat History Table
        # ==========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history(

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            conversation_id TEXT NOT NULL,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(user_id) REFERENCES users(id)

        )
        """)

        self.connection.commit()

    def get_user_by_email(self, email):

        self.cursor.execute("""
        SELECT *
        FROM users
        WHERE email = ?
        """, (email,))

        return self.cursor.fetchone()

    def close(self):
        self.connection.close()

    # Context Manager
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):

        if exc_type is not None:
            self.connection.rollback()

        self.close()

        return False