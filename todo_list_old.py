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
    
def headerNames(): # returns the names of the headers
    for row in reader:
        return row # breaks after one loop
    
def rewriteHeaders(headers): # cant seem to get the headers in the list
    oldList = list(reader)
    print(oldList)
        
def rowCount():
    return sum(1 for row in reader) - 1

def updateIDs():
    updatingList = list(reader) # cast to a list
    for i in range(len(updatingList)): # iterate through list
        updatingList[i][0] = i+1 # edit the IDs 
    writer.writerows(updatingList) # write the IDs back in

def addItem(): # appends an item to the list
    taskName = input("Task name: ")
    
    rating = -1
    while rating == -1:
        try:
            tempRating = int(input("Rating: "))
            if tempRating < 1:
                raise ValueError()
            rating = tempRating
        except ValueError:
            print("Input was not an integer above 0.")
    
    descripton = input("Description: ")
    
    writer.writerow([rowCount()+1, taskName, rating, descripton])
    
def deleteItem():
    # select for name and if duplicate ask for 1st vs 2nd vs...? 
    # edit each cell to update ID
    print("uh oh")

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
        
        header = ["id", "task_name", "rating", "body_text"]
        # if (list(headerNames()) != header):
        #     rewriteHeaders(header)

        while True:
            task = input("Type 'view' to see your to-do list. Type 'add' to add a task. Type 'delete' to remove a task.\n")
            task = task.lower()
            
            updateIDs()
            
            if task == 'view':
                printList()
            elif task == 'add':
                addItem()
            elif task == 'delete':
                print("delete")
            else:
                print("Invalid command.")
        
except KeyboardInterrupt:
    print("\nClosing program.")
