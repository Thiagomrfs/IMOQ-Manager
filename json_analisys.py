import json


def read():
    with open("database.json", "r+") as db:
        data = json.load(db)
    print(data)

def write(key, value):
    with open("database.json", "r+") as db:
        data = json.load(db)

    data.append({key: value})

    with open("database.json", "w+") as db:
        json.dump(data, db, indent=4, separators=(",", ":"))

