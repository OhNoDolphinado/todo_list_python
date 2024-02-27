# Todo list

# Sorts items:
# - by name, alphabetically
#   - A-Z or Z-A
# - by a "star" rating
# - By task length

# when items get put in, append escape char to commas in body

# Stores items in CSV which gets edited(?)
# figure out how to change the text on the editor without new line


import csv
import time
    
def headerNames(): # returns the names of the headers
    for row in reader:
        return row # breaks after one loop
    
def addItem(): # appends an item to the list
    taskName = input("Task name: ")
    
    rating = -1
    while rating == -1:
        try:
            tempRating = int(input("Rating: "))
            if tempRating < 0:
                raise Exception("Positive integers only.") # try to fold this into valueerror?
            rating = tempRating
        except ValueError:
            print("Input is not a positive integer.")    
    
    descripton = input("Description: ")
    
    writer.writerow([taskName, rating, descripton])
    
def printList(): # prints the list
    print("\nTodo list:\n---------")
    for row in list(reader)[1:]: # skipping first row
        starCount = "★" * int(row[1]) # formatting the stars
        print(f"{starCount} | {row[0]} | {row[2]}")
    print("")

try:
    with open("todo.csv", mode='r+', newline='') as todo_list_file:
        reader = csv.reader(todo_list_file)
        writer = csv.writer(todo_list_file)

        printList()
        addItem()
        # while True:
        #     addItem(writer)
        
except KeyboardInterrupt:
    print("Closing program.")
