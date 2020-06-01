import json_analisys
import support
import os
import exam_creation
import category_manager

support.msg("Welcome to the IMOQ managing system")
resp = support.menu("Choose your action",
                    "Register a new question",
                    "Search a question by id",
                    "Create exam",
                    "Create category",
                    "Select category",
                    "Exit program")
os.system("cls")


if resp == 1:
    support.msg("Registering a new question")

    question_category = json_analisys.ask_category()
    question_details = {}
    question_details["question_id"] = json_analisys.get_last_id(question_category) + 1
    question_details["question"] = input("Please insert the question: ")
    alternatives = ["A", "B", "C", "D", "E"]
    for alternative in alternatives:
        question_details[f"{alternative}"] = input(f"Please insert the {alternative} alternative: ")

    os.system("cls")

    confirm_resp = support.confirm_question(question_details)
    if confirm_resp == "Y":
        json_analisys.write_json(question_details, question_category)
    else:
        pass
elif resp == 2:
    support.msg("Searching by ID")
    question_category = json_analisys.ask_category()
    json_analisys.search_by_id(question_category)
elif resp == 3:
    support.msg("Create a new exam")
    question_category = json_analisys.ask_category()
    number_of_questions = exam_creation.ask_number_of_questions()
    exam = exam_creation.create_exam(number_of_questions)
    exam_creation.view_exam(exam)   
elif resp == 4:
    support.msg("Creating a new category")
    category = input("Insert the category: ")
    category_manager.create_category(category)
elif resp == 5:
    support.msg("Category selection")
    category_manager.see_categories()
elif resp == 6:
    exit()
