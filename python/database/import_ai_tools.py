import json
from pathlib import Path
from python.database.database import Database

ROOT = Path(__file__).resolve().parents[2]

JSON_FILE = ROOT / "data" / "ai_tools" / "ai_tools.json"


db = Database()
db.create_tables()

with open(JSON_FILE, "r", encoding="utf-8") as file:
    tools = json.load(file)

for tool in tools:

    db.cursor.execute(
        """
        INSERT INTO ai_tools(name, category, website)
        VALUES (?, ?, ?)
        """,
        (
            tool.get("name", ""),
            tool.get("category", ""),
            tool.get("website", "")
        )
    )

db.connection.commit()
db.close()

print("AI Tools Imported Successfully")