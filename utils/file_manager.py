import os
import json
from settings import DATA_FILE_PATH

# Path to the data folder and file
# DATA_FOLDER = ".data"
# DATA_FILE = "program_data.json"
# DATA_PATH = os.path.join(DATA_FOLDER, DATA_FILE)
DATA_PATH = DATA_FILE_PATH
DATA_FOLDER = os.path.dirname(DATA_PATH)


def ensure_file_exists():
    """
    Ensure the data folder and file exist.
    Creates folder and file if they don't exist.
    """
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    if not os.path.exists(DATA_PATH):
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump({}, f, indent=4)  # start with empty JSON


def load_data():
    """
    Load JSON data from the file.
    Returns an empty dict if file is empty.
    """
    ensure_file_exists()
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {}
    return data


def write_data(data):
    """
    Write all data to the file.

    Args:
        data (dict): Data to write (should be serializable to JSON)
    """
    ensure_file_exists()
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
