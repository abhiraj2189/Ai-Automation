from python.database.database import Database


class AIChatRepository:

    def save_chat(
        self,
        user_id,
        conversation_id,
        question,
        answer
    ):

        with Database() as db:

            db.cursor.execute("""
            INSERT INTO chat_history
            (
                user_id,
                conversation_id,
                question,
                answer
            )
            VALUES
            (?, ?, ?, ?)
            """, (
                user_id,
                conversation_id,
                question,
                answer
            ))

            db.connection.commit()

    def get_history(self, user_id):

        with Database() as db:

            db.cursor.execute("""
            SELECT
                id,
                conversation_id,
                question,
                answer,
                created_at
            FROM chat_history
            WHERE user_id=?
            ORDER BY id ASC
            """, (user_id,))

            return db.cursor.fetchall()

    def get_conversations(self, user_id):

        with Database() as db:

            db.cursor.execute("""
            SELECT
                conversation_id,
                MIN(question)
            FROM chat_history
            WHERE user_id=?
            GROUP BY conversation_id
            ORDER BY MAX(id) DESC
            """, (user_id,))

            return db.cursor.fetchall()

    def delete_conversation(
        self,
        user_id,
        conversation_id
    ):

        with Database() as db:

            db.cursor.execute("""
            DELETE
            FROM chat_history
            WHERE
            user_id=?
            AND
            conversation_id=?
            """, (
                user_id,
                conversation_id
            ))

            db.connection.commit()