# Todo List project for AP CSP create task

'''
TODO:
- View list (done)
- Add items
- Remove items
- Sort items
   - by name, alphabetically
   - by "star" rating
   - by task length(?)
- Clean data as it enters (escape chars on commas, etc) (inside addItem())

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
        
def addItem():
    taskName = input("Task name: ")
    
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
    
    # need to actually add it to the dataframe lmao
    
def removeItem():
    print('remove item')


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
    print("\nClosing program.")