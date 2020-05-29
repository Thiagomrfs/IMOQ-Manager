import json
import support
import json_analisys
from pathlib import Path


def create_category(category):
    atual_directory = Path("C:\Development\IMOQ\Data")
    with open(f"{p}\{category.capitalize()}.json", "a+", encoding="utf8") as category:
        category.write("[]")

def see_categories():
    ...

def choose_category(): 
    ...
