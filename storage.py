import json

def save_result(result):

    try:
        with open("history.json", "r") as file:
            data = json.load(file)

            # ensure data is a list
            if not isinstance(data, list):
                data = []

    except:
        data = []

    data.append(result)

    with open("history.json", "w") as file:
        json.dump(data, file, indent=4)