#memory address of an element in the list can be found by below function id(element)
list1 = ["Samsung", -20, "Nokia", "Apple"]
print("Memory location of an element is", id("Nokia"))

days_of_week = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print(days_of_week)
print(f"Last day of week is {days_of_week[-1]}")
print("Lenth of elements in list", len(days_of_week))

#reverse - it reversed the given list.
days_of_week.reverse()
print("Reversed list", days_of_week)

l1 = [3,5,0,7,1,8,4]
print("list l1 =", l1)

#slice - it sclices the elements with input as an start_index:end_index:step_count
print("Sliced list l1", l1[1:5:1]) #It will print from index[1] till index[4] with the steps count 1

#sort -- sorts in reverse/forward manner.
l1.sort()
print("Sorted list l1", l1)
l1.sort(reverse=True)
print("Reverse sorted list l1",l1)

l2 = [1,7,0,5,0,2,0,7,2,5]
print("list l2 =", l2)

#count -- it counts the occurance of an element and returns the value in number of times.
print("Count of 0 in l2 is ", l2.count(0))
# item_to_count = int(input("Enter the number to be counted from above: ")) #int can be removed in case of strings.
# c = l2.count(item_to_count)
# print(f"Occurance of {item_to_count} is {c} times")

#membership - in (will return True if item is present or vice-vera)
print(f"Is 5 present in l2? {5 in l2}")
#membership - not in (will return False if item is present or vice-vera)
print(f"Is 3 not present in l2? {3 not in l2}")

#concatination - it joins the two lists.
print("Concatinated list l1+l2 =", l1+l2)

#repeat - repeats the list * n times.
l3 = [0,5,2]
print("list l3 =", l3)
print("Repeated list l3*3", l3 * 3)

#append -- adds an item to the end of list.
fruits = ["apple","mango","pinapple","kiwi"]
print("Fruits =", fruits)
#syntax: list.append(item)
fruits.append("banana")
print("Appended list Fruits", fruits)
#Note: append functions takes only one argument.

#extend -- adds multiple items to the end of list
fruits.extend(["ghrapes","guava"])
print("Extended list", fruits)

#insert -- adds an element before specified index
#syntax: list.insert(index, item)
flowers = ["Rose","Sunflower","Lotus","Jasmine"]
print(flowers)
flowers.insert(2, "Lily")
print("Inserted 'Lily' in list", flowers)

#remove -- removes item of first occurance from list
flowers.remove("Lotus")
print("Removed 'Lotus' from list", flowers)

#pop - takes an index instead of item name and removes
flowers.pop(3) #OR use (-1) or () index for last element removal
print("Poped element with index 3", flowers)

#numbers operations in list
l4 = [3,-5,9,7.4,6,-2,5,1]
print(f"list l4 = {l4}")

#min - finds smallest number in the list
print(f"The minimum number in list l4 is {min(l4)}")

#max - biggest number in the list
print(f"The maximum number in list l4 is {max(l4)}")

#sum - finds total of numbers
print(f"The total sum of numbers in list l4 is {sum(l4)}")

#nested lists - list inside a list
l5 = [3, 5, 0, "python", [1,2,4], True, None, 10]
print("list l5 =", l5)
#inner list [1,2,4] is at index 4 and fetching its element of 2nd index i.e 4
print(f"fetching element from list inside a list {l5[4][2]}") # the index will increase as the nested lists increases.

