print("***Welcome to the Number Guessing Game!***")
print("I 'm think of a number between 1 and 100. Can you guess it?")

import random
result = random.randint(1,100)

count = 0

while True:

    count = count + 1

    num = int(input("Enter your guess: "))

    if num < result:
        print("Too low! Try again.")
    elif num > result:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {count} attempts.")
        break