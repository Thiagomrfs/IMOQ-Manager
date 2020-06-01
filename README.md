# IMOQ-Manager
A python questions manager created to help professors to organize their questions database using simple ```.Json``` files to create a local storage.


## Requirements
python 3.6+


## How to run?
Just run the ```main.py``` file and follow the interface, the support files will be created automatically.

### Register a new question
As you register questions, the manager automatcally create archives at the ```./Data``` folder, who contains json files named as the informed category of questions.
#### Example:
    .
    + Data
      + Subject_one.json
      + Subject_two.json
      + Subject_three.json

### Searching question by id
after creating a category and added questions on it you'll be able to search questions by their id, wich is gradually generated as you add questions to the database.

### Create exam
to help our beloved professors to create exams or activities based on the avaliable database, this functionality randomly select an amount of questions and displays it in colums.

### Create category
Create a new category at ```./Data```.

### See Category
Shows the database of the selected category
