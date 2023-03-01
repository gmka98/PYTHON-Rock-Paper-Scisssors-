import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

possible_actions = ["rock", "paper", "scissors"]

while True:
    user = input('Make a choice (ROCK,PAPER,SCISSORS): ').upper()
    IA_action = random.choice(possible_actions)
    print(f"\nYou chose {user}, It chose {IA_action}.\n")

    if user == IA_action:
        print("It's a tie nobody won :| both of you lose")
    elif user == 'ROCK':
        if IA_action == "scissors":
            print('THE ROCK! Bottoms the scissors!!! YOU WIN! >:(')
        else:
            print('Paper recovers the rock! You lose :)')
    elif user == "PAPER":
        if IA_action == "scissors":
            print("The paper loses against the scissors >:), you lose")
        else:
            print("The rock recovers the paper with his people CHAMP!! :( You win!")
    elif user == "SCISSORS":
        if IA_action == "paper":
            print("THE SCISSORS like your cut G! :/ You Win!")
        else:
            print("Rock smashes your scissors hahaha ;) You LOSE!")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
