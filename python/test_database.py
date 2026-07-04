from database.database_manager import DatabaseManager

db = DatabaseManager()

sample = [
    {
        "name": "ChatGPT",
        "company": "OpenAI"
    }
]

db.save(
    "ai_tools",
    "test.json",
    sample
)

print(db.load(
    "ai_tools",
    "test.json"
))