#Unkike lists, touples & strings cannot be modified and used for fixed data.
#Touples can contains any datatypes, such as lists, True, None, touple inside touple.

t1 = ("Python", 10, 6.5, True, [3,5,8], (3,6,1))
print(len(t1))
print(t1[0])
print(t1[-1])

t2 = 1,2,3 #a tuple can also be represented like this.
print(type(t2))

#list can be converted into tuples and vice-versa
l1 = [1,2,4,6]
print(l1, type(l1))
t3 = tuple(l1)
print(t1, type(t3))

fruits = ("Mango", "Apple", "Banana", "Kiwi")
print(fruits, type(fruits))
fruits = list(fruits)
print(fruits, type(fruits))

#contatination
t4 = (1,2)
t5 = (3,4)
t6 = t4 + t5
print(t6)

#repeatation
t7 = (1,2,3,4)
print(t7 * 3)

#membership - in
print(f"Is Mango present in fruits list? {'Mango' in fruits}") #returns True
print(f"Is Pinaple present in fruits list? {'Pinaple' in fruits}") #returns False

#membership - not in
print(f"Is Mango present in fruits list? {'Mango' not in fruits}") #returns False
print(f"Is Pinaple present in fruits list? {'Pinaple' not in fruits}") #returns True

#count
#syntax: tuple.count(element)
t8 = (10, 20, 30, 40, 50, 20, 10, 40, 50)
print(f"The count of an element is {t8.count(50)}")

#index
#syntax: tuple.index(element)
print(f"The index of an element is {t8.index(40)}")

#min/max/sum
print(min(t8))
print(max(t8))
print(sum(t8))

#Mutability & Immutability
s1 = "I am learning Python"
s1.replace("Python", "Java")
print(s1) # This will return "I am learning Python" this proves that along with tuples, strings are also immutable.
#to get the replaced value, need to assign the replace statement in another string
s2 = s1.replace("Python", "Go")
print(s2)