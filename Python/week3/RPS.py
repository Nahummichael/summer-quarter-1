# Prompt the players for their names
# 1. Propmt player 1 for RPS
# 2. Prompt player 2 for RPS
# 3. compare p1 and p2  choices and decide a winner

#FIXES
# 1. check for valid response
# 2. Hide player input


def RPS():
    print("Welcome challenger to the game of games, ROCK, PAPER, SCISSORS")
    player1 = input("player 1, state thy name: ")
    player2 = input("player 2, state thy name: ")

    # Gather Player choices
    p1_Choice = input(f"{player1}, make thy choice and gamble upon thy victory, Rock, Paper, or Scissors: ")
    while not MoveValidation(p1_Choice):
        print(f"ts aint valid {player1} do it once more")
        p1_Choice = input(f"{player1}, make thy choice and gamble upon thy victory, Rock, Paper, or Scissors: ")
    
    p2_Choice = input(f"{player2}, you too make thy choice and gamble upon victory, Rock, Paper, or Scissors: ")
    while not MoveValidation(p2_Choice):
        print(f"ts aint valid {player2} fix it now")
        p2_Choice = input(f"{player2}, you too make thy choice and gamble upon victory, Rock, Paper, or Scissors: ")

    # Compare Player moves
    if p1_Choice == p2_Choice:
        print("yall both bums aint nobody win trash ahh")
    
    elif p1_Choice == "rock" and p2_Choice == "scissors":
        print(f"Rock triumphs over scissors, the victory belongs to {player1}")

    elif p1_Choice == "paper" and p2_Choice == "rock":
        print(f"Paper triumphs over rock, victory belongs to {player1}")

    elif p1_Choice == "scissors" and p2_Choice == "paper":
        print(f"scissors triumphs over paper, victory belongs to {player1}")

    elif p1_Choice == "rock" and p2_Choice == "paper":
        print(f"Paper triumphs over rock, victory belongs to {player2}")

    elif p1_Choice == "scissors" and p2_Choice == "rock":
        print(f"Rock triumphs over scissors, victory belongs to {player2}")

    elif p1_Choice == "paper" and p2_Choice == "scissors":
        print(f"Sissors triumphs over paper, victory belongs to {player2}")


def MoveValidation(playerMove):
    validMoves = ["rock", "paper", "scissors"]
    
    if playerMove.lower() in validMoves:
        return True
    else :
        return False




RPS()