# String Operation:

s1 = "Hello World"

# Lenght of a string
print (len ())

# Indexing 
print (s1[0])  # prints first character
print (s1[-1]) # prints last character

# Concatination S1+S2
s2 = " Python"
print (s1 + s2)

#Slicing
print (s1[0:5]) # prints Hello
print (s1[6:])  # prints World

'''
Syntax for indexing: string_name[index_number]
Syntax for slicing: string_name[start_index:end_index:step_size]
start_index: Starting index of the slice (inclusive)
end_index: Ending index of the slice (exclusive)
step_size: Interger that specifies the step size for slicing (default is 1)
'''
print (s1[2:7:1]) # prints llo W
print (s1[1:6:2])   # prints l o

# fstrings - allows us to embed expressions inside string literals, using curly braces {}.
name = "Alice"
age = 30
print (f"My name is {name} and I am {age} years old.")

# Escape sequences - special characters that are used to represent certain characters in a string.
## n/ - New Line
print ("Hello\nWorld") # prints -
# Hello
# World
## t/ - Tab
print ("Hello\tWorld") # prints Hello    World
## // - Backslash
print ("This is a backslash: \\") # prints This is a backslash: \
## /' - Inserts a single quote
print ('This is a Python\'s code') # prints -- This is a Python's code
## /" - Inserts a double quote
print ("He says, \"we are learning Python\"") # prints -- He says, "we are learning Python"

# Membership Operators (in, not in)
print ("hello" in s3) # prints True
print ("Python" in s3) # prints False
pring ("Python" not in s3) # prints True

# Comparison Operators
s4 = "Hello"
s5 = "hello"
print (s4 == s5) # prints False
print (s4 != s5) # prints True

# Stripping - Removes spaces from the string
s6 = "   Hello World   "
print (s6.strip()) # removes leading and trailing spaces

# Replace - Replaces a specified phrase with another specified phrase
s7 = "Hello World"
print (s7.replace("World", "Python")) # prints Hello Python
print (s7.replace("l", "L")) # prints HeLLo WorLd -- replaces all occurrences of "l" with "L".
print (s7.replace("l", "L",1)) # prints HeLlo World -- replaces only the first occurrence of "l" with "L"

# Count - Returns the number of times a specified value occurs in a string
s8 = "Hello World"
print (s8.count("o")) # prints 2
print (s8.count("l")) # prints 3

# String Methods
s9 = "We are learning Python"
print (s9.upper()) # prints WE ARE LEARNING PYTHON
print (s9.lower()) # prints we are learning python
print (s9.title()) # prints We Are Learning Python
print (s9.split()) # prints ['We', 'are', 'learning', 'Python']
print (s9.capitalize()) # prints We are learning python
print (s9.startswith("We")) # prints True
print (s9.endswith("Python")) # prints True



