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

with open("todo_list.csv", mode='r+') as todo_list_file:
    todo_list = csv.DictReader(todo_list_file)
    for row in todo_list:
        print(row["task_name"])
    
    fieldnames = ["task_name", "rating", "body_text"] # can this be made dynamic by reading from the file?
    writer = csv.DictWriter(todo_list_file, delimiter=",", escapechar="\n")
    
    # writer.writerow({"task_name" : "Code project", "rating" : "4", "body_text" : "stop being lazy and code"})
    
#sjdghkjds