import json
import support
import os
import category_manager


def read(category):
    with open(f"{category}.json", "r+") as db:
        data = json.load(db)
    print(data)

def write_json(new_data, category):
    with open(f"{category}.json", "r+", encoding="utf8") as db:
        data = json.load(db)

    data.append(new_data)

    with open(f"{category}.json", "w+", encoding="utf8") as db:
        json.dump(data, db, indent=4, separators=(",", ":"), ensure_ascii=False)

def get_last_id(category):
    with open(f"{category}.json") as db:
        data = json.load(db)
    count = 0
    for question in data: 
        count += 1
    return count

def search_by_id(category):
    with open(f"{category}.json", "r+", encoding="utf8") as db:
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

def ask_category():
    question_category = input("please choose the question's category: ")
    if f"{question_category}.json" not in os.listdir(): 
        creation_resp = support.verify_yes_no(input("It seems like this category isn't created yet, would you like to create a new one? "))
        if creation_resp == "Y":
            category_manager.create_category(question_category)
    return question_category