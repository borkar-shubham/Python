'''
Creating a simple number guessing game.
The user gets 10 chances to guess the number.
If the user guesses the number before 10 chances, stop asking for the input from the user
'''

print("Welcome to the number guessing game. You have 10 attempts.")
print("The secret number is between 1 to 50.")

import random

secret_number = random.randint(1, 50)
attempts = 10
is_guess_correct = False

num = 1
while num <= 10:
    print(f"You have {attempts} attempts remaining.")
    user_number = int(input("Guess & enter the ssecret number: "))
    if user_number == secret_number:
        print("Congratulations...🎉 you have guessed the correct secret number!")
        is_guess_correct = True
        break
    else:
        if user_number < secret_number:
            higher_or_lower = "higher"
            print(f"You have guessed the incorrect number, Try {higher_or_lower} number.")
        else:
            higher_or_lower = "lower"
            print(f"You have guessed the incorrect number, Try {higher_or_lower} number.")
    num += 1
    attempts -= 1
if not is_guess_correct:
    print("Better luck next time, You have exhausted all the attempts")
print(f"The secret number was {secret_number}. Game Over..!")