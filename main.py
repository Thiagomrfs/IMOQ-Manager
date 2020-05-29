import json
import json_analisys
import support
import os

support.msg("Welcome to the IMOQ managing system")
resp = support.menu("Choose your action",
                    "Register a new question",
                    "Search a question by id",
                    "Create exam database",
                    "Exit program")
os.system("cls")


if resp == 1:
    support.msg("Registering a new question")
    question_details = {}
    question_details["question_id"] = json_analisys.get_last_id() + 1
    question_details["question"] = input("Please insert the question: ")
    alternatives = ["A", "B", "C", "D", "E"]
    for alternative in alternatives:
        question_details[f"{alternative}"] = input(f"Please insert the {alternative} alternative: ")
    os.system("cls")

    confirm_resp = support.confirm_question(question_details)
    if confirm_resp == "Y":
        json_analisys.write_json(question_details)
    else:
        pass
# elif resp == 2:
    
# elif resp == 3:

# elif resp == 4:

# elif resp == 5:
