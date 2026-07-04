from python.database.database import Database


class AIToolsRepository:

    def get_all(self):

        db = Database()

        rows = db.cursor.execute("""
        SELECT
            id,
            name,
            category,
            website
        FROM ai_tools
        """).fetchall()

        db.close()

        result = []

        for row in rows:

            result.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "website": row[3]
            })

        return result