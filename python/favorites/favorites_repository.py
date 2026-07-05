from python.database.database import Database


class FavoritesRepository:

    def add_favorite(self, user_id, tool_name, website):

        db = Database()

        db.cursor.execute("""
        INSERT INTO favorites(user_id, tool_name, website)
        VALUES (?, ?, ?)
        """, (user_id, tool_name, website))

        db.connection.commit()
        db.close()

    def get_favorites(self, user_id):

        db = Database()

        db.cursor.execute("""
        SELECT id, tool_name, website, created_at
        FROM favorites
        WHERE user_id = ?
        ORDER BY id DESC
        """, (user_id,))

        data = db.cursor.fetchall()

        db.close()

        return data

    def delete_favorite(self, favorite_id, user_id):

        db = Database()

        db.cursor.execute("""
        DELETE FROM favorites
        WHERE id = ? AND user_id = ?
        """, (favorite_id, user_id))

        db.connection.commit()

        db.close()