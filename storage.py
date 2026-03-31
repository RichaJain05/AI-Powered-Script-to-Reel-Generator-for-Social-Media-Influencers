import json
import os

def save_result(result):

    file_path = "history.json"

    # if file doesn't exist → create empty list
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            json.dump([], file)

    try:
        # read existing data
        with open(file_path, "r") as file:
            data = json.load(file)
    except:
        # if file corrupted → reset
        data = []

    # append new result
    data.append(result)

    # save back
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)