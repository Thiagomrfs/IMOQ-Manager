import json
import json_analisys
import support
from random import randint

def ask_number_of_questions():
    try:
        number_of_questions = int(input("Insert the number of questions: "))
        return number_of_questions
    except:
        while True:
            try:
                number_of_questions = int(input("\033[31mPlease insert a valid number:\033[m "))
            except:
                continue
            else:
                return number_of_questions

def create_exam(questions=10):
    with open("database.json") as db:
        data = json.load(db)
    if len(data) < questions:
        print("\033[31mFatal error: There's no questions enough in the database\033[m")
    else:
        used_questions = []
        count = 0
        selected_questions = []

        while count != questions:
            choose = randint(0, len(data)-1)
            if choose in used_questions:
                continue
            else:
                count +=1
                used_questions.append(choose)
                selected_questions.append(data[choose])
    return selected_questions

def view_exam(exam):
    for question in exam:
        print("\033[34m" + question["question"] + "\033[34m")
        print("\033[33m")
        print("A) " + question["A"])
        print("B) " + question["B"])
        print("C) " + question["C"])
        print("D) " + question["D"])
        print("E) " + question["E"])
        print("\033[m")
        