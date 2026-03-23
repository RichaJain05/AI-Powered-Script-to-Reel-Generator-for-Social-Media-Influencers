import json

def save_result(result):

    try:
        # try to read existing data
        with open("history.json", "r") as file:
            data = json.load(file)
    except:
        # if file is empty or not present
        data = []

    # add new result
    data.append(result)

    # write back to file
    with open("history.json", "w") as file:
        json.dump(data, file, indent=4)