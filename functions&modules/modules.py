#random module
import random
#     module.function()
print(random.random())  #random function retunrs random float between 0.0-1.0 excluding 1.0
print(random.randint(1,5))    #randint function returns the random integers between given range including both start & end int.

fruits = ["Apple", "Banana", "Cherry", "Kiwi", "Strawberry"]
print(random.choice(fruits)) #returns the random item from a sequence[]

random.shuffle(fruits) #returns the elements shuffled in random order
print(fruits)