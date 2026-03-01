#for loop with list
l1 = ['Cooper', 1.2, True, 1998]
for x in l1: #OR for x in ['Cooper', 1.2, True, 1998]:
    print(x) # --> here x will get assigned to each of the values in each of an iteration.

#for loop with strings
for i in 'Apple':
    print(i) # i will be assigned to each letter of "Apple" in each iteration

#for loop with range
for k in range(1,5):
    print('banana')   #in case of range, iteration will be till n-1

#for loop with dictionary
employee = {"emp-id": 1001, "name": "Tom", "dept": "Finance"}

for i in employee:
    print(i, employee[i]) #employee[i] --> it will print the values with keys. i will print keys alone.

for i in employee.items():
    print(i)
for i in employee.items():
    print(i[0], i[1])

#range functions - used to generate the sequence of intergers in a given interval
#syntaxes -
#range(start, stop, step) --> stop - not included in interval.
#range(start, stop) --> step is 1 by default if don't provided
#range(stop) --> start is 0 & step 1 by default.
#as stop parameter got excluded, we use "len()" function to iterate till last element of a list.

for l in range(1, 10): #will take step as 1 by default.
    print(l)
for n in range(1, 10, 2):   #will generate the odd numbers as start is 1.
    print(n)
for m in range(2, 10, 2):   #will generate the even numbers as start is 2.
    print(m)
for p in range(20, 10, -2):   #will generate the even numbers at descending order.
    print(p)
for q in range(10):   #will generate 0 to 9
    print(q)

groceries = ["milk", "rice", "wheat", "sugar", "oil", "soap"]

for index in range(len(groceries)): #range(6) -> 0,1,2,3,4,5
    print(index) # will print 0 to 5

#Followings are the profits for quarter 1 to 4 respectively. 
profits = ["46Cr", "51Cr", "56Cr", "49Cr"]
for index in range(len(profits)):
    quarter = index + 1 #as quarter starts from 1 & index from 0
    print(f'The profit of quarter {quarter} is {profits[index]}.')

#finding total, lowest & highest using loops
scores = [34, 41, 22, 13, 29, 55]

total = 0 #lets asume total score is zero when match started.
for score in scores:
    total = total + score     #this total when match started (When loops starts)
print(f'Total score of a match is {total}') #This total is after match is over, here in case when loop is over.

#highest score using loop
highest = scores[0] #screening the highest score from starting.
for score in scores:
    if highest < score: #It will check one by one and if any next score found higher than currently iterating score
       highest = score #then it will assign that new high score value to the variable "highest".
print(f'Highest score is {highest}')

#high score using max function
highest = max(scores)
print(highest)

#simillarly it will work for lowest score using lowest > score or "min" function.

#Continue - skips the current iteration and jumps to the next loop cycle.
#It moves directly to the next loop cycle if the condition is true, else it allows to execute the code below it in case of false condition.
marks = [90, -1, 85, -3, 78]

for mark in marks:
    if mark < 0:  #it will skip the iteration and will execute the code below continue in case of marks less than zero.
        continue
    print("Valid mark:", mark)

#Break - It Stops Searching Once Found
#It Stops entire loop & Exits loop completely.
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    if num == 30:
        print("Found it!")
        break #as soon as it will find the 30, it will stops the next iterations and exit the loop.





