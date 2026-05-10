#Regular Expressions (RegEx)

message1 = "The current version of Python is 3.17"

#Check if "Python" word is present in the string.
print("Python" in message1)
print(message1.find("Python")) #prints the index of provided word.


import re

'''
Search function in re module -
re.search(regex_pattern, string)
--> returns a match object if found else, returns None.
'''
message2 = "The current version of Python is 3.13, the previous versions are 3.12, 3.11, 3.10"

match_obj = re.search('13', message2)
print(match_obj)

if re.search('13', message2):
    print("Found..!")
else:
    print("Not Found..!")

