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
   - by tags
- Add / remove tags
   - Adding a tag means iterating over the list and editing the list
- Clean data as it enters (escape chars on commas, etc) (inside addItem()) (not needed)
- Go back and comment everything all pretty-like (look at docstrings and type hinting)

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

def itemInColumn(index, name):
    return name in todoDataframe[index].values

def addItem():
    taskName = ""
    while taskName == "":
        try:
            tempTaskName = input("Task name: ")
            if itemInColumn("task_name", tempTaskName):
                raise NameValidationError()
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
    global todoDataframe # required to edit todoDataFrame value
    
    itemToDelete = input("Name of item to delete: ")
    todoDataframe = todoDataframe[todoDataframe["task_name"] != itemToDelete]

def sortList():
    global todoDataframe # required to edit todoDataFrame value
    
    sortingParameter = input("What would you like to sort by?\n(Options are: 'name', 'rating', 'tags')\n")
    ascDesc = askDesc()
    match sortingParameter:
        case "name":
            sortingParameter = "task_name"
        case "rating":
            sortingParameter = "rating"
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
            ascDesc = False
        case "desc":
            ascDesc = True
    return ascDesc
    
def tagsToList(): # iterates through dataframe and changes all tag cells to lists
    global todoDataframe
    
    for i in range(len(todoDataframe)):    
        newCell = todoDataframe.iat[i, 3]
        newCell = newCell.replace("['", "")
        newCell = newCell.replace("']", "")
        newCell = newCell.split("', '")

        todoDataframe.iat[i, 3] = newCell

def importTags(): # scrapes through the dataframe and grabs all tags

    tags = []
    for row in range(len(todoDataframe)):
        for j in todoDataframe.iat[row, 3]:
            if j not in tags and j != "[]":
                tags.append(j)
    return tags

def editTag(tags):
    task = input("Type 'create' to make a new tag. Type 'add' to add a tag to an item. Type 'delete' to remove a tag from an item.\n")
    task = task.lower()
    
    tag = input(f"Please type the name of the tag you'd like to {task}:\n")
    
    match task:
            case "create":
                createTag(tag)
            case "add":
                addTag(tag)
            case "delete":
                deleteTag(tag)
            case _:
                print("Invalid command.")
            
def createTag():
    pass    

def addTag():
    itemToTag = input("What's the name of the item you'd like to add a tag to?\n")

def deleteTag():
    pass

# THE FUNCTION NEEDS TO:
# - take an input
# - have a loop
# - have a conditional (like an if statement)
# - have calls that run __different__ parts of the code

# for add:
# ask two things: name of item to edit, and tags
# parse tag(s) into list
# find tags cell in dataframe
# append new tags to the tags cell

# for remove:
# ask one thing: name of item to edit
# find tags cell in dataframe
# remove tag from the tags cell

# def editTags():
#     # item = input("Which item would you like to add a tag to?\n")
#     # if (not(itemInColumn(0, item))): # figure out how to make this ensure the item you're looking for actually exists
#     #     print("Item not found.")
#     #     return
#     task = input("Would you like to add tags ('add'), or remove some ('delete')?\n")
#     if task == "add":
#         addRemoveTags("add")
#     elif task == "delete":
#         addRemoveTags("delete")
#     else:
#         print("Not a valid command.")

# def addRemoveTags(mode):
#     tagsToBeEdited = input(f"What tags would you like to {mode}? (Delinate with ', ' -- ex. earth, wind, fire)\n")
#     tagsToBeEdited = tagsToBeEdited.split(", ")
    
#     temp2DList = todoDataframe.values
    
#     for tag in tagsToBeEdited:
#         for i in range(len(temp2DList[0])):
#             temp2DList[i][3] = convertCellToList(temp2DList[i][3])
#             if (mode == "add"):
#                 temp2DList[i][3].append(tag)
#             elif (mode == "delete"):
#                 temp2DList[i][3].remove(tag)
#             todoDataframe.iat[i, 3] = temp2DList[i][3] # figure out how to make this copy our new list into the dataframe cell
    
# def convertCellToList(item): # converts strings in the csv that should be lists into lists
#     if isinstance(item, str):
#         item = item.replace("[", "")
#         item = item.replace("]", "")
#         item = item.split(", ")
#     return item

try:
    
    todoDataframe = pd.read_csv('todo.csv')
    
    headers = ["task_name", "rating", "body_text", "tags"]
    
    if(isHeaderCorrect(headers) == False):
        fixHeader(headers)
    
    tagsToList()
    availableTags = importTags()
    print(availableTags)
    
    while True:
        task = input("Type 'view' to see your to-do list. Type 'add' to add a task. Type 'delete' to remove a task. Type 'sort' to sort the list. Type 'tags' to edit tags.\n")
        task = task.lower()
        
        match task:
            case "view":
                printList()
            case "add":
                addItem()
            case "delete":
                removeItem()
            case "sort":
                sortList()
            case "tags":
                editTag(availableTags)
            case _:
                print("Invalid command.")
                
except KeyboardInterrupt:
    todoDataframe = todoDataframe.to_csv('todo.csv', index=False)
    print("\nClosing program.")