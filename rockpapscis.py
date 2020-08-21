
import random
t = ["Rock", "Paper", "Scissors"]


computer = random.choice(t)


player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?\n")
    if player == computer:
        print("Tie!",player,computer)
    elif player == "Rock":
        if computer == "Paper":
            print('computer=',computer)
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
              print('computer=',computer)
              print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
              print('computer=',computer)
              print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = random.choice(t)
