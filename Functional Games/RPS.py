import random
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
EXIT = 'exit'

def make_choice():
    user_input = input("Make a choice:\n\
        'r' -> Rock\n\
        'p' -> Paper\n\
        's' -> Scissors\n\
        'x' -> Exit Game\n\
        >>>\t")
    if(user_input == 'r'):
        return ROCK
    elif(user_input == 'p'):
        return PAPER
    elif(user_input == 's'):
        return SCISSORS
    elif(user_input == 'x'):
        return EXIT
    else:
        make_choice()

def __eq__(choice1, choice2):
    if choice1 == choice2:
        return True

def __gt__(choice1, choice2):
    if(choice1 == PAPER and choice2 == ROCK):
        return True
    elif(choice1 == ROCK and choice2 == PAPER):
        return False


    elif(choice1 == ROCK and choice2 == SCISSORS):
        return True
    elif(choice1 == SCISSORS and choice2 == ROCK):
        return False


    elif(choice1 == SCISSORS and choice2 == PAPER):
        return True
    elif(choice1 == PAPER and choice2 == SCISSORS):
        return False
    else:
        return False

def main():
    sentinel = True
    while(sentinel):
        player1Choice = make_choice()
        player2Choice = make_choice()
        if(player1Choice == EXIT or player2Choice == EXIT):
            sentinel = False
        elif (__gt__(player1Choice, player2Choice)):
            print("\nPlayer 1 chose:\t" + player1Choice + "\n\
    Player 2 chose:\t" + player2Choice + "\n\
    Player 1 Wins!\n\n")
        elif (__eq__(player1Choice, player2Choice)):
            print("\nPlayer 1 chose:\t" + player1Choice + "\n\
    Player 2 chose:\t" + player2Choice + "\n\
    It's a Tie!\n\n")
        else:
            print("\nPlayer 1 chose:\t" + player1Choice + "\n\
    Player 2 chose:\t" + player2Choice + "\n\
    Player 2 Wins!\n\n")

main()
