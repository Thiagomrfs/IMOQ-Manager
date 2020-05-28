import json


def read():
    with open("database.json", "r+") as db:
        data = json.load(db)
    print(data)

def write_json(new_data):
    with open("database.json", "r+") as db:
        data = json.load(db)

    data.append(new_data)

    with open("database.json", "w+") as db:
        json.dump(data, db, indent=4, separators=(",", ":"))

try: 
    db = open("database.json")
    json.load(db)
    db.close()
except:
    db = open("database.json", "a+")
    db.write("[]")
    db.close()