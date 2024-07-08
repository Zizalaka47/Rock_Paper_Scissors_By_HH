import random

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))  
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk)) 

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

player_move = input("Choose [r]ock, [p]aper or [s]cissors: ").lower()

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid input. Try again...")

computer_random_number = random.randint(1, 3)

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
else:
    computer_move = scissors

prLightPurple(f"Your choice is {player_move}.")
prYellow(f"The computer chose {computer_move}.")

if (player_move == rock and computer_move == scissors) or \
   (player_move == paper and computer_move == rock) or \
   (player_move == scissors and computer_move == paper):
    prGreen("You win!")
elif player_move == computer_move:
    prLightGray("Draw!")
else:
    prRed("You lose!")
