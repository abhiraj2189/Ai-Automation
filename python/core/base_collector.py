from database.database_manager import DatabaseManager


class BaseCollector:

    def __init__(self):
        self.db = DatabaseManager()

    def save(self, folder, filename, data):
        self.db.save(folder, filename, data)