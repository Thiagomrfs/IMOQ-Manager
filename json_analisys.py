import json
import support

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

def search_by_id():
    with open("database.json", "r+", encoding="utf8") as db:
        data = json.load(db)
    wanted_question = support.verify_int(input("Insert the ID of the wanted question: "), range(1, len(data)+1))
    found = data[wanted_question - 1]
    print("\033[34m" + found["question"] + "\033[34m")
    print("\033[33m")
    print("A) " + found["A"])
    print("B) " + found["B"])
    print("C) " + found["C"])
    print("D) " + found["D"])
    print("E) " + found["E"])
    print("\033[m")


try: 
    db = open("database.json")
    json.load(db)
    db.close()
except:
    db = open("database.json", "a+")
    db.write("[]")
    db.close()
