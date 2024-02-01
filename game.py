import random


Options=("rock","paper","scissors")

running = True
while running :
    player= None
    computer= random.choice(Options)

    while player not in Options:
    
     player= input("Enter your choice (rock ,paper,scissors): ")

        
    print(f"player: {player}")
    print(f"computer: {computer}")
    if player == computer:
     print("It's a tie! ")
    elif player == "rock" and computer == "scissors":
     print("YOU WIN :) !")
    elif player == "paper" and computer == "rock":
     print("YOU WIN :) !")
    elif player == "scissors" and computer == "paper":
     print("YOU WIN :) !")
    else:
     print("YOU LOSE :( ")
    play_again = input("Play again? (y/n): ").lower()
    if not play_again == "y":
     running= False
print("Thanks for playing !")