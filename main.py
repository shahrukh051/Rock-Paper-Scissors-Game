# rock paper scissors game

import random

user_win = 0
computer_win = 0
options = ["rock", "paper", "scissor"]

while True:
    user_input = input("type rock/paper/scissor or Q to quit the game:  \n").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("invalid input")
        continue

    random_number = random.randint(0, 2)
    #rock:0, paper:1, scissor:2
    computer_pick = options[random_number]
    print("computer pickes", computer_pick)
    if user_input == computer_pick:
        print("It's a tie!")
        continue
    if user_input == "scissor" and computer_pick == "rock":
        print("computer won")
        computer_win += 1
    elif user_input == "rock" and computer_pick == "paper":
        print("computer won")
        computer_win += 1
    elif user_input == "paper" and computer_pick == "scissor":
        print("computer won")
        computer_win += 1
    else:
        print("computer lost")
        user_win += 1
    print("you won", user_win, "times.")
    print("the computer won", computer_win, "times.")