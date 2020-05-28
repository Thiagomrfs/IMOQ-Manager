import json


def read():
    with open("database.json", "r+") as db:
        data = json.load(db)
    print(data)

def write_json(new_data):
    with open("database.json", "r+", encoding="utf8") as db:
        data = json.load(db)

    data.append(new_data)

    with open("database.json", "w+", encoding="utf8") as db:
        json.dump(data, db, indent=4, separators=(",", ":"), ensure_ascii=False)

def get_last_id():
    with open("database.json") as db:
        data = json.load(db)
    count = 0
    for question in data: 
        count += 1
    return count

def see_question():
    ...


try: 
    db = open("database.json")
    json.load(db)
    db.close()
except:
    db = open("database.json", "a+")
    db.write("[]")
    db.close()
