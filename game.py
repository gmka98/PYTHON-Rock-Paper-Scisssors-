import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


while True:
    user = input ('Make a choice (ROCK,PAPER,SCISSORS):')
    possible_ations = ["rock,paper,scissors"]
    IA_action = random.choice(possible_ations)
    print(f"\n You chose {user}, It chose {IA_action}.\n")
    
    if user == IA_action:
        print("It's a tie nobody won :| both of you lose")
        
    elif user == 'ROCK':
    
     if IA_action == "scissors":
        print('THE ROCK ! Bottom the scissors!!! YOU WIN! >:(')
    else:
        print('Paper recover The Rock! You loose :)')
        
    if user == "PAPER":
    
    elif IA_action == "scissors":
    print("The Paper lose again the scissors >:), You loose")
    
else:("THE ROCK ! recover the paper with his people CHAMP!! :( You win!")

     elif user == "SCISSORS":
    if IA_action == "Paper":
        print("THE SCiSSors like your cut G! :/ You Win!")
else:
        print("rock smashes your scissors hahaha ;) You LOOSE!")

        play_again = input("Lose again?" "(y/n): ")
        if play_again.lower() != "y":
            break

>>> Action.Rock == Action(0)
True
>>> Action(0)
<Action.Rock: 0>
    function finale(){
    }


    
