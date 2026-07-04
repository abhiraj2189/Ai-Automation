from python.database.database import Database


class AuthRepository:

    def create_user(self, username, email, password):

        db = Database()

        db.cursor.execute("""
        INSERT INTO users(username, email, password)
        VALUES (?, ?, ?)
        """, (username, email, password))

        db.connection.commit()
        db.close()