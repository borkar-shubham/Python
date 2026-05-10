### json module

import json

students = {
    'student1': {'roll': 101, 'name': 'Hema', 'percent': 98.55, 'sports': True},
    'student2': {'roll': 102, 'name': 'Rekha', 'percent': 87, 'sports': False},
    'student3': {'roll': 103, 'name': 'Jaya', 'percent': 91.2, 'sports': False},
    'student4': {'roll': 104, 'name': 'Sushma', 'percent': 79.8, 'sports': True}
}

#dump() --> it converts the above dictionary and stores into the new json file.
# with open("students_data.json", "w") as fh:
#     json.dump(students, fh, indent=4) 
#     print("Created/updated a file - students_data.json")

#load() --> it loads the data from the file - students_data.json and stores in the variable "data".
# with open("students_data.json", "r") as fh:
#     data = json.load(fh)
# print(data)
# print(type(data))
'''
#update() --> It used for updating/syncing the data changes from above students dictionary to the json file.
print("Syncing the updated data in students_data.json")
with open("students_data.json", "r") as fh:       #opening the json file in read mode.
    data = json.load(fh)                          #loading the data with alias "fh" and storing it in variable "data".
data.update(students)                             #update operation

with open("students_data.json", "w") as fh:       #opening the json file in write mode.
    json.dump(data, fh, indent=4)                 #using dump function to write the updated data into the json file.

#NOTE: The above update function will return the error - FileNotFoundError: [Errno 2] No such file or directory: 'students_data.json' in case the file is not found or get deleted.
#To handling the error, we can use below code for the same operation -
'''
try:
    with open("students_data.json", "r") as fh:
        data = json.load(fh)
except FileNotFoundError:
    print("The json file is not found, creating the new file.")
    with open("students_data.json", "w") as fh:      ###write the file if got FileNotFoundError.
        json.dump(students, fh, indent=4)
else:
    data.update(students)              ##update operation
    with open("students_data.json", "w") as fh:    ##write the updated data in the json file.
        json.dump(data, fh, indent=4)
    print("Data updated in the json file.")