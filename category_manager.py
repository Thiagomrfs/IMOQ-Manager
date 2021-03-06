import json
import support
import json_analisys
import os

if "Data" not in os.listdir():
    os.mkdir(f"{os.getcwd()}/Data")

if os.getcwd().split("\\")[-1] is not "Data":
    os.chdir("./Data")

def create_category(category):
    if f"{category.capitalize()}.json" not in os.listdir():
        try:
            with open(f"{category.capitalize()}.json", "a+", encoding="utf8") as category:
                category.write("[]")
        except:
            raise FailedToCreateCategory("Failed to create category")
    else:
        print("\033[31mIt seems like the category already exists.\033[m")

def see_categories():
    categories = os.listdir()
    for category in categories:
        print(category)

def choose_category(): 
    ...
