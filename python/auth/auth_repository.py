from python.database.database import Database
import sqlite3


class AuthRepository:

    def create_user(self, username, email, password):

        try:
            with Database() as db:
                db.cursor.execute("""
                INSERT INTO users(username, email, password)
                VALUES (?, ?, ?)
                """, (username, email, password))

                db.connection.commit()

        except sqlite3.IntegrityError:
            raise ValueError("Email already registered")

    def get_user(self, email):

        with Database() as db:
            return db.get_user_by_email(email)