import json
import sqlite3


class ProjectRepository:

    DB = "python/database/ai_automation.db"

    def save(self, project):

        conn = sqlite3.connect(self.DB)

        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS projects(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            topic TEXT,

            research TEXT,

            script TEXT,

            scenes TEXT,

            created_at DATETIME DEFAULT CURRENT_TIMESTAMP

        )
        """)

        cur.execute("""

        INSERT INTO projects(

            topic,

            research,

            script,

            scenes

        )

        VALUES(?,?,?,?)

        """,(

            project.topic,

            project.research,

            project.script,

            json.dumps(project.scenes)

        ))

        conn.commit()

        conn.close()