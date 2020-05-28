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
    question_id = json_analisys.get_last_id() + 1
    #ask the questtion
    #ask the alternatives
    # save {id: ID, question: QUESTION, a: A, b: B....}
    json_analisys.write_json({"id": question_id,
                                "question": "QUESTION",
                                "a": "A",
                                "b": "B",
                                "c": "C",
                                "d": "D",
                                "e": "E"})
# elif resp == 2:
    
# elif resp == 3:

# elif resp == 4:

# elif resp == 5:
