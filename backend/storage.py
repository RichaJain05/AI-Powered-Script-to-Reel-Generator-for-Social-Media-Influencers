import json
import os

# history.json is always created in the same folder as this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HISTORY_FILE = os.path.join(BASE_DIR, "history.json")

def save_result(result):
    try:
        # Check if file exists and is not empty
        if os.path.exists(HISTORY_FILE) and os.path.getsize(HISTORY_FILE) > 0:
            with open(HISTORY_FILE, "r") as file:
                data = json.load(file)
                
            if not isinstance(data, list):
                data = []
        else:
            data = []

    except (json.JSONDecodeError, FileNotFoundError):
        # If the file is corrupted or missing, start fresh
        data = []

    data.append(result)

    with open(HISTORY_FILE, "w") as file:
        json.dump(data, file, indent=4)