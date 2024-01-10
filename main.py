import random

choices = ["Rock", "Paper", "Scissors"]

computer = random.choice(choices)
player = None

while player not in choices:
    player = input("Rock, Paper, Scissors").lower()

    print("Computer: ", computer)
    print("Player: ", player)

    if player == computer:
        print("Computer: ", computer)
        print("Player: ", player)
        print("You tied!")
    elif player == "Rock":
        if computer == "Paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Paper won!")
        if computer == "Scissors":
            print("Computer:", computer)
            print("Player: ", player)
            print("Rock won!")
    elif player == "Paper":
        if computer == "Rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Rock won!")
        if computer == "Scissors":
            print("Computer:", computer)
            print("Player: ", player)
            print("Paper won!")
    elif player == "Scissors":
        if computer == "Paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Scissors won!")
        if computer == "Rock":
            print("Computer:", computer)
            print("Player: ", player)
            print("Rock won!")





