from python.database.database import Database


class NotesRepository:

    def create_note(self, user_id, title, content):

        with Database() as db:

            db.cursor.execute("""
            INSERT INTO notes(user_id, title, content)
            VALUES (?, ?, ?)
            """, (user_id, title, content))

            db.connection.commit()

    def get_notes(self, user_id):

        with Database() as db:

            db.cursor.execute("""
            SELECT id, title, content, created_at
            FROM notes
            WHERE user_id = ?
            ORDER BY id DESC
            """, (user_id,))

            return db.cursor.fetchall()

    def update_note(self, note_id, user_id, title, content):

        with Database() as db:

            db.cursor.execute("""
            UPDATE notes
            SET title=?, content=?
            WHERE id=? AND user_id=?
            """, (title, content, note_id, user_id))

            db.connection.commit()

    def delete_note(self, note_id, user_id):

        with Database() as db:

            db.cursor.execute("""
            DELETE FROM notes
            WHERE id=? AND user_id=?
            """, (note_id, user_id))

            db.connection.commit()