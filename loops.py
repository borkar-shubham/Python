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
employee = {"emp-id": 1001, "name": Tom, "dept": "Finance"}

for i in employee:
    print(i, employee[i]) #employee[i] --> it will print the values with keys. i will print keys alone.