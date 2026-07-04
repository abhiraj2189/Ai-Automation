import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

DB_PATH = ROOT / "database" / "ai_automation.db"


class Database:

    def __init__(self):
        self.connection = sqlite3.connect(DB_PATH)
        self.cursor = self.connection.cursor()

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS ai_tools(

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            category TEXT,
            website TEXT
        )
        """)

        self.connection.commit()

    def close(self):
        self.connection.close()