from random import choice
from time import sleep


print()
Name = ""
Name = input(" --  What is your name? I`m gonna call you by that. ")
print()


wins_1 = 0
wins_2 = 0

while True:

    # print(pyfiglet.figlet_format("    R P S"))
    print("""
      ____  ____  ____  
     |  _ \|  _ \/ ___| 
     | |_) | |_) \___ \ 
     |  _ <|  __/ ___) |
     |_| \_\_|   |____/ 
     
    """)

    player1_wins = 0
    player2_wins = 0

    winning_score = 0

    while True:

        try:

            winning_score = int(input(" --  What is the winning score? "))
            print()

            break

        except:

            print()
            print(" --  You must inter an integer!!  --")
            print()

    while player1_wins < winning_score and player2_wins < winning_score:

        print(f" --  {Name} : {player1_wins} | Computer : {player2_wins}  --")

        Player_1 = input(f" # {Name} , Make your move : ").lower()

        computerMove_moves = ["rock", "paper", "scissors"]
        computerMove = choice(computerMove_moves)
        Player_2 = computerMove

        print(f" # Computer move is : {Player_2}")

        if (Player_1 == "e") or (Player_1 == "exit"):

            print()
            print("--  You are intred EXIT  --")
            print()
            print(" ** ** ** ** ** ** ** ** ** ** ** ** ")
            break

        elif (Player_1 == Player_2) or (Player_1 == "r" and Player_2 == "rock") or (
                Player_1 == "s" and Player_2 == "scissors") or (Player_1 == "p" and Player_2 == "paper"):
            
            sleep(1)
            print(" --  TIE  --")

        elif Player_1 == "rock" or Player_1 == "r":

            if Player_2 == "scissors":
                sleep(1)
                print(f" --  {Name} win  --")
                player1_wins += 1

            elif Player_2 == "paper":
                sleep(1)
                print(" --  Computer win  --")
                player2_wins += 1

        elif Player_1 == "paper" or Player_1 == "p":

            if Player_2 == "rock":
                sleep(1)
                print(f" --  {Name} win  --")
                player1_wins += 1

            elif Player_2 == "scissors":
                sleep(1)
                print(" --  Computer win  --")
                player2_wins += 1

        elif Player_1 == "scissors" or Player_1 == "s":

            if Player_2 == "paper":
                sleep(1)
                print(f" --  {Name} win  --")
                player1_wins += 1

            elif Player_2 == "rock":
                sleep(1)
                print(" --  Computer win  --")
                player2_wins += 1

        else:

            print(" --  WHAT??  --")

        print()
    print(" --  Final score  --")
    print(f" --  {Name} : {player1_wins} | Computer : {player2_wins}  --")
    print()
    if player1_wins == winning_score:
        print(f" --  {Name} WON  --")
        wins_1 = wins_1 + 1
    elif player2_wins == winning_score:
        print(" --  Computer WON  --")
        wins_2 = wins_2 + 1
    else:
        print(" ***********************************")
        break
    print()
    print(" --  At All  -- ")
    print(f" --  {Name} : {wins_1} | Computer : {wins_2}  -- ")
    print()
    print("                END")
    print()
    print(" ***********************************")
    print()
    while True:
        try:
            run = 1
            print(f" --  {Name} Are you continu?  --")
            print("        1.YEAP    2.NOPE")
            run = int(input(" --  I chosed : "))
            if run == 2:
                break

            elif run == 1:
                print()
                print(" --  Countinue!  --")
                print()
                break
        except:
            print(" --  WHAT??  --")
            print()
    if run == 2:
        break

winbar = ""
if wins_1 > wins_2:
    winbar = "WINNER OF RPS GAME! Congratulation."
elif wins_1 < wins_2:
    winbar = "LOSER OF RPS GAME! Sory."
elif wins_2 == wins_1:
    winbar = "TIE WITH COMPUTER."

print()
print(" --  You left!  --")
print()
print(f" --  All plays : {wins_1 + wins_2}")
if wins_1 == 1:
    print(" --  Your win was once.")
elif wins_1 == 0:
    print(" --  You were not winner!")
else:
    print(f" --  You were win {wins_1} games.")

if wins_2 == 1:
    print(" --  Computers win was once.")
elif wins_2 == 0:
    print(" --  Computer was not winner!")
else:
    print(f" --  Computer was win {wins_2} games.")

print()

if wins_1 + wins_2 != 0:
    persent = (wins_1 / (wins_1 + wins_2)) * 100
else:
    persent = 0

print(f" --  You were win {persent} persents of games  --")

print()
print(f" --  Thancks a lot for your playing {Name} , you`re {winbar}  --")
print()

print(" --  Created by: shsotoudegan@gmail.com  --")
print()

