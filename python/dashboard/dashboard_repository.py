from python.database.database import Database


class DashboardRepository:

    def get_stats(self, user_id):

        with Database() as db:

            db.cursor.execute(
                "SELECT COUNT(*) FROM notes WHERE user_id=?",
                (user_id,)
            )
            notes = db.cursor.fetchone()[0]

            db.cursor.execute(
                "SELECT COUNT(*) FROM favorites WHERE user_id=?",
                (user_id,)
            )
            favorites = db.cursor.fetchone()[0]

            db.cursor.execute(
                "SELECT username,email,created_at FROM users WHERE id=?",
                (user_id,)
            )

            user = db.cursor.fetchone()

            return {
                "notes": notes,
                "favorites": favorites,
                "username": user[0],
                "email": user[1],
                "member_since": user[2]
            }