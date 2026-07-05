from python.database.database import Database


class ProfileRepository:

    def get_profile(self, user_id):

        with Database() as db:

            db.cursor.execute("""
            SELECT username, email, role, created_at
            FROM users
            WHERE id = ?
            """, (user_id,))

            return db.cursor.fetchone()

    def update_profile(self, user_id, username, email):

        with Database() as db:

            db.cursor.execute("""
            UPDATE users
            SET username=?, email=?
            WHERE id=?
            """, (username, email, user_id))

            db.connection.commit()