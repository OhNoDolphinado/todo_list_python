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
    
    answers = [taskName, rating, descripton, None]
    
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
    
def fixTags(index): # iterates through dataframe and changes all tag cells to lists
    global todoDataframe
    
    if (isinstance(todoDataframe.iat[index, 3], str)):  
        newCell = todoDataframe.iat[index, 3]
        newCell = newCell.replace("['", "")
        newCell = newCell.replace("']", "")
        newCell = newCell.split("', '")

        todoDataframe.iat[index, 3] = newCell
    elif (isinstance(todoDataframe.iat[index, 3], list) and len(todoDataframe.iat[index, 3]) > 0):
        return
    else:
        todoDataframe.iat[index, 3] = None

def editTag():
    task = input("Type 'add' to add a tag to an item. Type 'delete' to remove a tag from an item. Type 'purge' to remove all instances of a tag.\n")
    task = task.lower()
    
    match task:
            case "add":
                name = input("Please type the name of the item you'd like to add a tag to:\n")
                tag = input("Please type the tag you'd like to add:\n")
                addTag(name, tag)
            case "delete":
                name = input("Please type the name of the item you'd like to remove a tag from:\n")
                tag = input("Please type the tag you'd like to delete:\n")
                deleteTag(name, tag)
            case "purge":
                tag = input("Please type the tag you'd like to remove entirely:\n")
                purgeTag(tag)
            case _:
                print("Invalid command.")

def addTag(name, tag):
    pass

def deleteTag(name, tag):
    pass

def purgeTag(tag):
    for i in range(len(todoDataframe)):
        if isinstance(todoDataframe.iat[i, 3], list) and tag in todoDataframe.iat[i, 3]: # checks if cell is a list and has the requested tag
            todoDataframe.iat[i, 3].remove(tag) # remove the tag from the list int the cell

            fixTags(i) # converts None to list at the edited cell for consistency's sake

# THE FUNCTION NEEDS TO:
# - take an input
# - have a loop
# - have a conditional (like an if statement)
# - have calls that run __different__ parts of the code

try:
    
    todoDataframe = pd.read_csv('todo.csv')
    
    headers = ["task_name", "rating", "body_text", "tags"]
    
    if(isHeaderCorrect(headers) == False):
        fixHeader(headers)
    
    for i in range(len(todoDataframe)):
        fixTags(i)
    
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
                editTag()
            case _:
                print("Invalid command.")
                
except KeyboardInterrupt:
    todoDataframe = todoDataframe.to_csv('todo.csv', index=False)
    print("\nClosing program.")