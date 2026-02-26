#comma separated key-value pair enclosed in {}.
# {key1:value1, key2:value2, key3:value3}
#Allowed keys - str, int, float, bool, tuple (immutable datatypes)
#NotAllowed keys - list, set, dict (mutable datatypes)
#keys must be of immutable datatypes.
#values can be any datatypes

#below is the dictionary of groceries with items:price.
groceries = {'milk':20, 'biscuits':30, 'bread':25}
print(groceries, type(groceries))
item = str(input("Enter the item to get its price:"))
print(groceries[item])

#updating the dictionary
groceries['eggs'] = 10
print(groceries)

#updating values of existing keys
groceries['milk'] = 40
print(groceries)

#fetching the value from dictionary
student1 = {"maths":76.4, "eng":87.2, "phy":71.9, "chem":84}
print(student1["eng"])

#similar functionality using get() - It do not returns an error in case incorrect key provided.
#syntax <dict>.get(<key>, <default>) - it will print the default value if the key is not present in dictionary.
print(student1.get("bio")) #It will print None, as no default value provided

#membership
print(76.4 in student1) #It will return False as it can only check for the key, not value.
print("eng" in student1)

#updating/merging the dictionaries
groceries1 = {'milk':20, 'biscuits':30, 'bread':25, 'weat':36}
groceries2 = {'rice':55, 'milk':25, 'maze':40}

groceries1.update(groceries2) #adding data from groceries2 to groceries1 dictionary
print(groceries1) #new items will be added and existing values will get updated

#pop - removing data from the dictionary
groceries1.pop("milk")
print(groceries1)

#in case of duplicate keys, python reads left to right, removes duplicate keys and prints the most recent value
groceries3 = {'milk':20, 'biscuits':30, 'bread':25, 'weat':36, 'milk':45}
print(groceries3)

#fetching values from dictionary inside dictionary
student2 = {'id':10001, 'name':'David', 'class':10, 'marks':{'maths':71.9, 'eng':83.2, 'phy':76.4, 'chem':79.2}}
print(student2['marks']['chem'])

#fetching all the keys, values & items from the dictionary
print(student2.keys(), type(student2.keys()))
print(student2.values(), type(student2.values()))
print(student2.items(), type(student2.items()))


#shallow & deep copy in dictionary
d1 = {'id':10001, 'name':'John', 'class':9, 'marks':{'maths':71.9, 'eng':83.2, 'phy':76.4, 'chem':79.2}}

import copy
#deepcopy
d2 = copy.deepcopy(d1)

d1['name'] = 'Danny'
d1['marks']['maths'] = 77 #updating the inner item value

print(f"d1-> {d1}", id(d1))
print(f"d2-> {d2}", id(d2)) #inner dict item value in d2 won't get updated as its copied with deep copy function.

#similarly in shalow copy, outer item values won't get changes but inner dict item values will get changed.