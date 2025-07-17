# this is guess the number game
# Chapter 3: AtBS
# author: diablo010
import random

low_num = 1
high_num = 100

secret_number = random.randint(low_num, high_num)
guesses = 0
is_running = True

print(f"Python Number Guessing Game")
print(f"Select a number between {low_num} and {high_num}")
# print(f"Secret number is {secret_number}")

while is_running:
    guess = input("Take a guess ~ ")

    if guess.isdigit():  # checks if all characters are numbers
        guess = int(guess)
        guesses += 1

        if guess < low_num or guess > high_num:
            print("That is out of range !")
        elif guess < secret_number:
            print("Too low !")
        elif guess > secret_number:
            print("Too high !")
        else:
            print(f"The answer was {secret_number}")
            print(f"No. of guesses: {guesses}")
            is_running = False
    
    else:
        print("Invalid guess")
        print("Please select a number in range")

print("Thanks for playing!")
