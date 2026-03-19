#Syntax
# def function_name(arg1, arg2, arg3,...argn):
#     statement1
#     statement2

#creating the function which will have "name" as an argument.
def greeting_someone(name):
    print(f"Hello {name}, good morning..")
    print("Have a great day..!")

#calling the function with passing an agrument.
greeting_someone("carol")
greeting_someone("Adam")
greeting_someone("Noah")

#defining the function for addtion of 2 numbers
def add (num1, num2):
    result = num1 + num2
    return result

#calling function and returning a single value
val1 = int(input("Enter a first number: "))
val2 = int(input("Enter a second number: "))
val = add(val1, val2)
print(f"The addtion of {val1} & {val2} is {val}")

#returning multiple values
def arithmetic(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    return add, sub, mul #returns 3 values
    
val1 = int(input("Enter a first number: "))
val2 = int(input("Enter a second number: "))

result1, result2, result3 =  arithmetic(val1, val2) #get stores the returned value into other variable sequentially
print(f"Addition of {val1}, {val2} is {result1}")
print(f"Substraction of {val1}, {val2} is {result2}")
print(f"Multiplication of {val1}, {val2} is {result3}")
#--------------------------------------------------------------------------------------------------------------------
#Type of Arguments:
# a. Positional Arguments -
def add(a, b):
    return a+b
result = add(4, 7) 
print(result)
#here, 4 is goint to assign to a & 7 to b respectively.
#--------------------------------------------------------------------------------------------------------------------
# b. Default Arguments
def add(a, b=8):
    return a+b
result = add(10, 21)
print(result)
#here, 21 will get replaced by 8 as we have explicitly provided the value of b.
def add(a, b=8):
    return a+b
result = add(10)
print(result)
# here, if we do not pass the value of b then it will take the default value defined in function itself.

#note: always remember to put the default arg at last or after all the non-defalut args.############################
#--------------------------------------------------------------------------------------------------------------------
# c. Keyword Arguments - can be used while calling the function itself.
def add(a, b=5, c=9):
    print(f"a:{a}, b:{b}, c:{c}")
    return a+b+c

result = add(10, c=3) #passing only a & c values
print(result)

#when we use the keyword value assigning, the order of positioning args does not matter.
#--------------------------------------------------------------------------------------------------------------------
# d. Variable Length Positional Arguments (0 to nth)):
def add(*args):                #use * only while defining the function
    print(args, type(args))

add(1,7,2) #here we can pass n number of args. using "args" is a standard way, we can use anything instead of "args".

#here, when we pass the number of arguments to *args, these gets stores in the variable args in the form of tupple.

def add(*args):
    return sum(args)

result = add(4,8,5,2)
print(result)

#example
def student_details(id, name, *marks):
    if len(marks) == 0:
        print(f"Student {name} did not attend the exam.")
    else:
        percent = sum(marks)/len(marks)
        print(f"Student {name} with id {id} secured {percent}%.")

#calling function to get the students details -
student_details(1002, "John", 87.0,76.4,81,93,79) #providing 5 subs marks
student_details(1007, "Bunty", 76,93,71,89,70,88) #providing 6 subjects marks
student_details(1004, "Alex")  #providing no args

#--------------------------------------------------------------------------------------------------------------------

# e. Variable Length Keywords Arguments (**args):
#the values passed to the **args gets stored in the variable in the form of "dictionary".
def myfunction(**kwargs):
    print(kwargs, type(kwargs))

myfunction(x=10, y=20)

#example
def student_details(id, name, **marks):
    if len(marks) == 0:
        print(f"Student {name} did not attend the exam.")
    else:
        percent = sum(marks.values())/len(marks)
        print(f"Student {name} with id {id} secured {percent}%.")

#calling function to get the students details -
student_details(1002, "John", maths=92,chem=88.4,bio=75,eng=97,phy=87) #providing 5 subs marks with keyword args
student_details(1007, "Bunty", maths=77,chem=81,bio=79,eng=77.9,phy=69,env=90) #providing 6 subjects marks
student_details(1004, "Alex")  #providing no args

#in case of *args & **args, the squesnce will be always as (abc, *args, **args)
#--------------------------------------------------------------------------------------------------------------------

#Docstrings in functions
def func():
    '''
    This is the docstring.
    We can document the functionality here..
    :return: None
    '''
    return None

help(func)

#Recursion
'''
It is a process in which a function calls itself until certain condition is met.
Factorial of n = n * (n-1) * (n-2) * (n-3)
4! = 4 * 3 * 2 * 1
'''
#Without Recursion
def fact(num):
    Factorial = 1
    while num > 1:
        Factorial *= num
        num -= 1
    return Factorial

n = 4
print(f'Factorial of {n} is {fact(n)} - without reccursion.')

#With Reccursion
def fact_rec(n):
    if n == 1:
        return 1
    else:
        factorial = n * fact_rec(n - 1)
        return factorial

n = 4
print(f'Factorial of {n} is {fact_rec(n)} - with reccursion.')

#Function as an argument:
def add_1(number):
    return number + 1

def square(number):
    return number ** 2

#calling a function inside the another function

n = int(input('Enter a number: '))
sqr = square(add_1(n))
print(sqr)

#Lambda Function:
#below is the example of regular function -
def add(a,b):
    return a + b

addition = add(3,4)
print(addition)

#Converting it to lambda function -
add = lambda a,b : a + b
addition = add(7,8)
print(addition)

#Filter using lambda function:
#Filter(function, sequence)

seq = [1,2,3,4,5,6,7,8,9,10]
odd = lambda x: True if x % 2 != 0 else False #adding the condition if x is not divisible by 2 then x is True
filtered_output = list(filter(odd, seq))
print(f'The filtered output is {filtered_output}.')

#OR the above function can also be written as -
filtered_output = list(filter(lambda x: True if x % 2 != 0 else False, seq)) #here lambda func is getting called for each element in seq list.
print(f'The filtered output is {filtered_output}.')

#mapping using lambda function
seq = [1,2,3,4]
mapped_output = map(lambda x: x ** 2, seq)
print(f'The mapped output is {list(mapped_output)}.')