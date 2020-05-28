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
