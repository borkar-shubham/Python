#sets are non-sequential collection of items means cannot have indexing within it.
set1 = {"Python", 10.6, -2, True, None}
print(set1, len(set1))

#sets do not allow the duplicate elements, use cases like passport number where duplicate entried are restricted.

#membership
nums = {16, 3, 8, 3, 7}
print(3 in nums)
print(8 not in nums)

#concatinations not supported
#repeat is not supported

#type cast is possible in sets

days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun") #tuple
days = set(days)
print(days) #it will return elements in set having random order everytime.

#add - elements can be added in the sets
nums.add(99)
print(nums)
#If we try to add an element which already present in the set, it won't make any changes as it does not posses duplicate values.

#remove - removes an element from set. Returns error if element not present in set.
days.remove("Sun")
print(days)

#discard - removes an element from set. Does not returns any error if element is already not present in set.
days.discard("Jan")
print(days)

#intersection - finds common elements within two sets.
student1 = {"Biology", "Physics", "Maths", "Chemistry", "CS"}
student2 = {"Biology", "Economics", "Maths", "Chemistry"}
student3 = {"Maths", "Sanskrit", "Maths", "English"}

common_subs = student1.intersection(student2)
print(common_subs)

#union - combines all elements of all provided sets
combined_subs = student1.union(student2,student3)
print(combined_subs)

#difference of sets
weekends = {"Sat", "Sun"}
weekdays = days.difference(weekends)
#OR weekdays = days - weekends
print(weekdays)

#frozensets - sets that are immutable
fs1 = frozenset({1,2,3,4,5})
print(fs1, type(fs1))

fs1.add(6)
print(fs1)

#common & difference operations can be performed on frozensets

