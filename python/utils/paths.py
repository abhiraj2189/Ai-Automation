import os

ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../")
)


def get_data_path(folder, filename):
    path = os.path.join(ROOT_DIR, "data", folder)
    os.makedirs(path, exist_ok=True)
    return os.path.join(path, filename)


def get_output_path(filename):
    path = os.path.join(ROOT_DIR, "output")
    os.makedirs(path, exist_ok=True)
    return os.path.join(path, filename)