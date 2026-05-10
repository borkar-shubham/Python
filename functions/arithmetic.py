#Defining custom user modules

def add(n1, n2):
    return n1 + n2

def square(num):
    return num ** 2

def square_root(num):
    return num ** 0.5

#this avoids to be appeared the below code result in the code where this module get imported.
if __name__ = "__main__":
    a=20
    b=30
    result = add(a,b)
    print(result)

# for user_module.py => __name__ => "__main__"
# for arithmetic.py => __name__ = "arithmetic"