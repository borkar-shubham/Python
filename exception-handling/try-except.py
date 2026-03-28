#Handling exceptions with try & except:
#Syntax -
# try:
#     < Code that might cause an error >
# except ExceptionType:
#     < Code that runs if the error occurs >
# else:
#     print(f"You entered: {x}")  ###only runs if no exception
# finally:
#.    print("Operation completed.") ##runs irrespective of errors & without error.
#-----------------------------------------------------------------------------------------------------------------
## Prevent program crashes
## Handle multiple errors
try:
    num1 = int(input("Enter the num1: "))
    num2 = int(input("Enter the num2: "))
    result = num1/num2
    print(result)

#zero division error will be print instead of throwing error when provided zero in denominator.
except ZeroDivisionError:
    print("The dinominator cannot be zero..!")
#value error will be printed when instead intergers, anything else has been provided in input.
except ValueError:
    print("Input should only be digits.")
#-----------------------------------------------------------------------------------------------------------------
## else — runs if no error occurred
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print(f"You entered: {x}")  # only runs if no exception
#-----------------------------------------------------------------------------------------------------------------
## finally — runs no matter what

try:
    fh = open("tmp.py", "r")
    content = fh.read()
except FileNotFoundError:
    print("File not found!")
finally:
    fh.close()  # always runs, error or not
#-----------------------------------------------------------------------------------------------------------------
## Catch any exception with Exception
try:
    risky_operation()
except Exception as e:
    print(f"Something went wrong: {e}")
#-----------------------------------------------------------------------------------------------------------------
## Raising an exception
age = int(input("Enter your age: "))

if age < 0:
    raise ValueError("Age cannot be negative.") #ValueError can be replaced as generic term "Exception"
else:
    if age => 18:
        print("You are eligible for vote.")
    else:
        print("You are not eligible for vote.")
#-----------------------------------------------------------------------------------------------------------------