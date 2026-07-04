from python.utils.json_manager import load_json, save_json
from python.utils.paths import get_data_path


class DatabaseManager:

    def save(self, folder, filename, data):
        path = get_data_path(folder, filename)
        save_json(path, data)

    def load(self, folder, filename):
        path = get_data_path(folder, filename)
        return load_json(path)