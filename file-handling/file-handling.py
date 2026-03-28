'''
Opening a file
Syntax: open("file_name with path", mode)
Where, 
modes: r, x, w, a, t, b
r - reads a file
x - creates a file
w - writes into the file
a - appends a file
t - opens a file in text mode
b - opens a file in binary mode
rt - default mode i.e file opens in text & read mode
'''
#need to run this from the folder where the file exists.
########################################################################################################################

### rt mode - opening the text file & read the contets.
fh = open("abc.txt", 'rt')  #just OPENS the file, doesn't read it
print(fh)                   #prints the object metadata, not content
fh.close()

#Opening & reading the contents of the file as a string.

handler = open("abc.txt", 'rt')
content1 = handler.read()        #✅ actually reads the file.
handler.seek(0)  #reseting the courser after reading the content1 to the begining of the line.
content2 = handler.read(10) #reads first 10 characters from a file.
#Or we can put the partial (content2 = handler.read(10) reading before content1 = handler.read() to avoid the handler.seek(0).
handler.close()

print(content1, type(content1))   #✅ prints the content
print(content2)

#readline - reads a single line from a file
handler2 = open("abc.txt", 'rt')
line1 = handler2.readline()
line2 = handler2.readline()
line3 = handler2.readline()
line4 = handler2.readline()
handler2.close()

print(f'line1: {line1}')
print(f'line2: {line2}')
print(f'line3: {line3}')
print(f'line4: {line4}') #empty string -> the file has reached to end of the file (EOF)

#readlines - reads all the lines from a file as a list.
handler3 = open("abc.txt", 'rt')
lines = handler3.readlines()

handler3.close()

print(f'lines: {lines}') #this will print the lines in the list with \n at the end.
print(type(lines))

#to print the line one by one without \n]
for line in lines:
    print(line.rstrip()) #removing space from end of a string

########################################################################################################################

### x mode - creating the new text file

x = open('file1.txt', 'xt')
#writing into a new text file
x.write("This is the new file created by file handler.\n")
x.write("This is next line")
#close the file
x.close()

########################################################################################################################

### w mode - opens the file for writing, overwrites file.
# It also creates the file if it does not exist.
file_handler = open('file2.txt', 'wt') #here file_handler can be replaced by any other variables.
file_handler.write("This is the overwritten text using w mode.\n")
file_handler.write('Have a nice day..!')
file_handler.close()

########################################################################################################################

### a mode - appends the content in the file
#if the given file does not exists, it will work as a w mode.
y = open('file2.txt', 'at')
y.write('\nThis is the appended line added by a mode.')
y.write('\nThis is the another appended line added by a mode.')
y.close()

########################################################################################################################

### with statement:
#lets take an example of normal file handling -
fh = open('abc.txt', 'rt')
content = fh.read()
fh.close()
print(content)

#we do the same with "with" statement which do not requires the closing of file manually
with open('abc.txt', 'rt') as fh:
    content = fh.read()

print(content)

#creating new file & writing a content in it
with open('xyz.txt', 'xt') as fh:
    fh.write('This is the new line created with new file by with statement.\n')
    fh.write('This is the another new line created by with statement.\n')

########################################################################################################################

## check if file exists













