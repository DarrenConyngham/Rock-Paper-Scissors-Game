from random import choice #used for the computer to make a choice
from time import sleep #used to delay the new question being asked

print("Welcome to Rock, Paper, Scissors!")


PLAYER_NAME = str(input("What is your name? "))
COMP_SCORE = 0
PLAYER_SCORE = 0

def num_rounds():
    """Asks the particpant how many rounds that they will be playing
    """
    while True:
        try:
            global rounds
            rounds = int(input("How may rounds to you want to play? "))
            break
        except:
            print("You have not entered a whole number. Try again...")
    
    print(f"{PLAYER_NAME}, you will be playing {rounds} rounds of Rock, Paper, Scissors. Here we go...")


def game_play():
    """ This is the actual Rock, Paper, Scissors game being played out.
    """
    for i in range(rounds):
        player = str(input("Rock, Paper or Scissors? ")).lower().strip() 
        #.lower() and .strip() allows me to accept input in uppercase or with whitespace    
        comp = choice(['rock', 'paper', 'scissors'])
        
        while True:
            if player not in ["rock", "paper", "scissors"]:
                print("You have not entered a valid input.")
                player = str(input("Rock, Paper or Scissors? ")).lower().strip()
            else:
                break    
        
        print(f"\nComputer plays {comp}.")
        
        global COMP_SCORE
        global PLAYER_SCORE
        
        if player == comp:
                print("It is a draw.")
                COMP_SCORE += 0.5
                PLAYER_SCORE += 0.5        
        
        if player == "rock":
            if comp == "paper":
                print("Computer wins this round.")
                COMP_SCORE += 1
                PLAYER_SCORE += 0            
            if comp == "scissors":
                print(f"{PLAYER_NAME} wins this round!")
                COMP_SCORE += 0
                PLAYER_SCORE += 1
                
        if player == "paper":
            if comp == "rock":
                print(f"{PLAYER_NAME} wins this round!")
                COMP_SCORE += 0
                PLAYER_SCORE += 1
            if comp == "scissors":
                print("Computer wins this round.")
                COMP_SCORE += 1
                PLAYER_SCORE += 0
                
        if player == "scissors":
            if comp == "rock":
                print("Computer wins this round.")
                COMP_SCORE += 1
                PLAYER_SCORE += 0
            if comp == "paper":
                print(f"{PLAYER_NAME} wins this round!")
                COMP_SCORE += 0
                PLAYER_SCORE += 1 
        
        print(f"\nSCORES\n{PLAYER_NAME}: {PLAYER_SCORE}\nComputer: {COMP_SCORE}")
        sleep(1)
    
#The code below allows a player to continue to play indefinitely
while True:
    num_rounds()
    game_play()
    if COMP_SCORE > PLAYER_SCORE:
        print(f"\nThe computer won by {int(COMP_SCORE - PLAYER_SCORE)} point(s). Sorry :(")
    if COMP_SCORE < PLAYER_SCORE:
        print(f"WELL DONE {PLAYER_NAME.upper()}! YOU ARE THE WINNER BY {int(PLAYER_SCORE - COMP_SCORE)} point(s)!!!")
    if COMP_SCORE == PLAYER_SCORE:
        print("It is a tie.")
    
    response = input("Do you want to play again? Enter No to quit. ")
    
    if response.lower().strip() == "no":
        print("\nGoodbye. Thanks for playing.")
        break
    
    print("")
    print("Awesome. Here we go...")
    
    COMP_SCORE = 0
    PLAYER_SCORE = 0