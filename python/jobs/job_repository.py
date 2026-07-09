import sqlite3
import os


class JobRepository:

    DB = "database/ai_automation.db"

    def __init__(self):

        os.makedirs("database", exist_ok=True)

        self.conn = sqlite3.connect(
            self.DB,
            check_same_thread=False
        )

        self.cursor = self.conn.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS jobs(

            job_id TEXT PRIMARY KEY,

            topic TEXT,

            status TEXT,

            progress INTEGER,

            current_step TEXT,

            output TEXT,

            error TEXT

        )

        """)

        self.conn.commit()

    def create_job(

        self,

        job_id,

        topic

    ):

        self.cursor.execute("""

        INSERT INTO jobs

        VALUES(?,?,?,?,?,?,?)

        """,(

            job_id,

            topic,

            "Pending",

            0,

            "Waiting",

            "",

            ""

        ))

        self.conn.commit()

    def update(

        self,

        job_id,

        status,

        progress,

        step,

        output="",

        error=""

    ):

        self.cursor.execute("""

        UPDATE jobs

        SET

        status=?,

        progress=?,

        current_step=?,

        output=?,

        error=?

        WHERE job_id=?

        """,(

            status,

            progress,

            step,

            output,

            error,

            job_id

        ))

        self.conn.commit()

    def get_job(

        self,

        job_id

    ):

        self.cursor.execute(

            "SELECT * FROM jobs WHERE job_id=?",

            (job_id,)

        )

        row = self.cursor.fetchone()

        if row is None:

            return None

        return {

            "job_id": row[0],

            "topic": row[1],

            "status": row[2],

            "progress": row[3],

            "current_step": row[4],

            "output": row[5],

            "error": row[6]

        }