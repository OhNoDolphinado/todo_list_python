# Todo List project for AP CSP create task

'''
TODO:
- View list (done)
- Add items (done)
- Remove items
- Sort items
   - by name, alphabetically
   - by "star" rating
   - by task length(?)
- Clean data as it enters (escape chars on commas, etc) (inside addItem()) (not needed)

TO GET CREDIT:
- Write a sorting algorithm that takes in a list of lists and returns a sorted list of lists

'''

import pandas as pd

def printList():
    
    print("\nTodo list:\n----------")
    for row in todoDataframe.values:
        starCount = int(row[1])
        stars = starCount * "★"
        spaces = (5-starCount) * " "
        print(f"{stars}{spaces} | {row[0]} | {row[2]}")
    print("")
        
class NameValidationError(Exception): # for use in addItem()
    pass

def checkItemAlreadyInColumn(name, index): # does this return true if the name is in the column?
    return name in todoDataframe[index]

def addItem():
    taskName = ""
    while taskName == "":
        try:
            tempTaskName = input("Task name: ")
            if 1 == 1: # use checkItemAlreadyInColumn()
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
    
    answers = [taskName, rating, descripton]
    
    todoDataframe.loc[len(todoDataframe)] = answers
    
def removeItem():
    '''
    ask for name of item
    '''

def sortList(sortingParameter):
    '''
    input is what you're sorting for
    turn dataframe into 2d array 
    bubblesort 2d array
    turn 2d array into dataframe
    '''

try:
    
    todoDataframe = pd.read_csv('todo.csv')
    
    while True:
        task = input("Type 'view' to see your to-do list. Type 'add' to add a task. Type 'delete' to remove a task.\n")
        task = task.lower()
        
        if task == "view":
            printList()
        elif task == "add":
            addItem()
        elif task == "delete":
            removeItem()
        else:
            print("Invalid command.")
        
except KeyboardInterrupt:
    todoDataframe = todoDataframe.to_csv('todo.csv', index=False)
    print("\nClosing program.")