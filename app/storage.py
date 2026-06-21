import json

def read_file():
    try:
        with open("expenses.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    return data
    

def write(data):
    with open("expenses.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)