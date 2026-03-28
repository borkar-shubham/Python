age = int(input("Enter your age: "))

if age < 0:
    raise ValueError("Age cannot be negative.") #ValueError can be replaced as generic term "Exception"
else:
    if age >= 18:
        print("You are eligible for vote.")
    else:
        print("You are not eligible for vote.")