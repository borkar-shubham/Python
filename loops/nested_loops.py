#nested loops are the loops inside the loops

for i in range(1,4):     #this loop will run from 1 to 3 
    for j in range(2):   # each iteration from above loop will iterate for 0 to 1 times.
        print(f'i={i}, j={j}') # so the entire loop will run 3*2=6 times

#star pattern using nested for loop:

for i in range(1, 6):   #this range decides how many rows will be printed
    for j in range(1, i+1):  #this decides how many starts * will be printed in each row.
        print("*", end=" ")  #to avoid to go to next line just after printing the *, we using end with space
    print()                  #this print function will help to go to next line once complete row get printed from inner loop.

'''
Write a program to simulate a roll of a dice.
A dice has 6 faces with numbers 1 to 6 written on it.
The program should be randomly prints a number between 1 and 6.
'''
import random

print("Welcome to the rolling dice game")

while True:
    choice = input("Press 'Enter' to roll a dice or 'q' to quit --> ")
    choice = choice.strip()          #to avoid any unintensional spaces before/after 'q' or "enter".
    if choice == 'q':
        print("Quiting the game, bye...")
        break
    elif choice == '':             #when user press enter, empty string has provided
        number = random.randint(1,6)  #randint includes starting & ending range
        print(f"Your number is {number}")
    else:
        print("Invalid Input!")
print("Game Over..!")

