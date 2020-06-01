import json
import support
import json_analisys
import os

if "Data" not in os.listdir():
    os.mkdir(f"{os.getcwd()}/Data")

def create_category(category):
    os.chdir("./Data")
    with open(f"{category.capitalize()}.json", "a+", encoding="utf8") as category:
        category.write("[]")

def see_categories():
    ...

def choose_category(): 
    ...