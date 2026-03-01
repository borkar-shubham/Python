#if statement
# if <condition>:
#     statement1 
#     statement2
#     ........
#     statementN
# statementM

#if the condition is true, python will execute the statements inside code block till statementN and then statementM.
#if the condition is false, it will directly go to the statementM.

#if-else statement:

age = float(input("What is your age? "))

if age >= 18:
    print("You are eligible for vote..!")
else:
    print("You are not eligible for vote..!")

#Example - To find whether the number is odd or even
# Operator used - % (modulus) - gives remainder
#if remainder - 0 -> Number is even
#if remainder != 0 -> Number is odd

num = int(input("Enter the integer to check if it is even or odd: "))

if (num % 2 == 0):
    print("The number is even..!")
elif (num % 2 == 1):
    print("The number is odd..!")
else:
    print("The number is invalid..!")

#ex - to check the +ve & -ve number

num2 = float(input("Enter the number to check if it is +ve or -ve: "))
if (num2 >= 0):
    print("The number is positive..!")
else:
    print("The number is negative..!")

#ex - multi if-elif-else
'''
>=90 Grade A
80 to 89 Grade B
70 to 79 Grade C
60 to 69 Grade D
< 60 grade F
'''

percents = int(input("Enter the % to check the result: "))

if (percents >= 90):
    print("You have got grade A..!")
elif (percents >= 80 and percents < 90):
    print("You have got grade B..!")
elif (percents >= 70 and percents < 80):
    print("You have got grade C..!")
elif (percents >= 60 and percents < 70):
    print("You have got grade D..!")
else: #for percents < 60
    print("You have got grade F..!")


#nested if-else
if percents >= 45:
    print("Congratulations, you have passed..!")
    if (percents >= 90):
        print("You have got grade A..!")
    elif (percents >= 80 and percents < 90):
        print("You have got grade B..!")
    elif (percents >= 70 and percents < 80):
        print("You have got grade C..!")
    elif (percents >= 60 and percents < 70):
        print("You have got grade D..!")
    else: #for percents < 60
        print("You have got grade F..!")
else:
    print("You have failed, try hard next time..!")


#Operators -   Unary, Binary, & Ternary
#Ternary Operators OR one liner conditions:
#Syntax: true-expression if condition else false-expression
num3 = int(input("Enter the number: "))
print("Even") if num3 % 2 == 0 else print("Odd")

