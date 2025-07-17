# this is rock, paper, scissors game
# Chapter 3: AtBS
# author: diablo010
import random

options = ("ROCK", "PAPER", "SCISSORS")

playing = True

print("ROCK🪨 , PAPER📃 , SCISSORS✂️ ")
while playing:
    player = None
    computer = random.choice(options)

    while player not in options:   
        player = input("Choose from (rock, paper, scissors)").upper()
        print(f"{player} vs {computer}")

    if player == computer:
        print("Tie !")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    else: 
        print("You lose!")

    if not input("Play again? (y/n)").lower() == 'y':
        playing = False