#while loop runs runs again & again as long as a condition is true, & terminates when the condition becomes false
#difference btw if & while is, "if" runs once when the confition is met and while runs again & again until condition becomes false.

num = 1

while num < 5:
    print(num)
    num = num + 1

#while loop with break
correct_psswd = "Python@123"
while True:     #infinite loop
    user_password = input("Enter your password: ") 
    if user_password == correct_psswd:
        print("The password is correct 😀")
        break   #infinite loop will stopped once met above condition.
    else:
        print("Incorrect password ☹️")
print("Logging in..!")