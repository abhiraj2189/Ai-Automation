from python.database.database import Database

db = Database()

rows = db.cursor.execute(
    "SELECT id, name, category, website FROM ai_tools"
).fetchall()

for row in rows:
    print(row)

db.close()