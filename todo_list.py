# Todo List project for AP CSP create task

'''
TODO:
- Check pandas header, add header if not present (done)
- View list (done)
- Add items (done)
- Remove items (done)
- Sort items
   - by name, alphabetically (done)
   - by "star" rating (done)
   - by task length(?)
   - by tags
- Add / remove tags -- a cell that's a list of tags
   - Adding a tag means iterating over the list and editing the list
- Clean data as it enters (escape chars on commas, etc) (inside addItem()) (not needed)

TO GET CREDIT:
- Write a sorting algorithm that takes in a list of lists and returns a sorted list of lists

'''

import pandas as pd

def isHeaderCorrect(headers):
    return headers == list(todoDataframe.head())

def fixHeader(headers):
    todoDataframe.columns = headers

def printList():
    print("\nTodo list:\n----------")
    for row in todoDataframe.values:
        starCount = int(row[1])
        stars = starCount * "★"
        spaces = (5-starCount) * " "
        print(f"{stars}{spaces} | {row[0]} | {row[2]} | TAGS: {row[3]}")
    print("")
        
class NameValidationError(Exception): # custom error for use in addItem()
    pass

def checkItemAlreadyInColumn(index, name):
    return name in todoDataframe[index].values

def addItem():
    taskName = ""
    while taskName == "":
        try:
            tempTaskName = input("Task name: ")
            if checkItemAlreadyInColumn("task_name", tempTaskName):
                raise NameValidationError
            taskName = tempTaskName
        except NameValidationError:
            print("Please use a name not already in use.")
            
    rating = -1
    while rating == -1:
        try:
            tempRating = int(input("Rating: "))
            if tempRating < 1 or tempRating > 5:
                raise ValueError()
            rating = tempRating
        except ValueError:
            print("Provide an integer from 1 to 5.")
    
    descripton = input("Description: ")
    
    answers = [taskName, rating, descripton, []]
    
    todoDataframe.loc[len(todoDataframe)] = answers
    
def removeItem():
    global todoDataframe # needed to edit todoDataFrame value
    
    itemToDelete = input("Name of item to delete: ")
    todoDataframe = todoDataframe[todoDataframe["task_name"] != itemToDelete]

def sortList():
    global todoDataframe # needed to edit todoDataFrame value
    
    sortingParameter = input("What would you like to sort by?\n(Options are: 'name', 'rating', 'length', 'tags')\n")
    match sortingParameter:
        case "name":
            ascDesc = askDesc()
            sortingParameter = "task_name"
        case "rating":
            ascDesc = askDesc()
            sortingParameter = "rating"
        case "length":
            todoDataframe.sort_values(by=headers[2], key=lambda length: length.str.len()) # this no worky :(
            return
        case "tags":
            print("sorting by tags isnt programmed yet lmao")
            return
        case _:
            print("Not a valid sorting type.")
            return

    todoDataframe = todoDataframe.sort_values(by=sortingParameter, ascending=ascDesc)

def askDesc():
    ascDesc = input("Ascending ('asc') or descending ('desc')\n")
    match ascDesc:
        case "asc":
            ascDesc = True
        case "desc":
            ascDesc = False
    return ascDesc

def editTags():
    ''''''

try:
    
    todoDataframe = pd.read_csv('todo.csv')
    
    headers = ["task_name", "rating", "body_text", "tags"]
    
    if(isHeaderCorrect(headers) == False):
        fixHeader(headers)
    
    while True:
        task = input("Type 'view' to see your to-do list. Type 'add' to add a task. Type 'delete' to remove a task. Type 'sort' to sort the list. Type 'tags' to edit tags.\n")
        task = task.lower()
        
        if task == "view":
            printList()
        elif task == "add":
            addItem()
        elif task == "delete":
            removeItem()
        elif task == "sort":
            sortList()
        elif task == "tags":
            editTags()
        else:
            print("Invalid command.")
        
except KeyboardInterrupt:
    todoDataframe = todoDataframe.to_csv('todo.csv', index=False)
    print("\nClosing program.")