#Created by whid0t, 2020
#That's a simple rock, paper, scissors game. Please choose one before starting
#the game. I needed 2 hours to fix the seeing who wins section because of wrong
#math so please rate me good XD.
import time
import random
from random import choice

#variables and start of the game
neshta = ["rock", "paper", "scissors"]

print("Please choose one:")

for x in range(len(neshta)):
    print (neshta[x])

#user input
while True:
    try:
        izb_igrach = input("Choice: ")
        if izb_igrach == neshta[0]:
                a = 8.0
        elif izb_igrach == neshta[1]:
                a = 4.0
        elif izb_igrach == neshta[2]:
                a = 1.0
#input check
    except ValueError:
        print("Please make a available choice...")
        continue
    else:
        print("You chose: %s" %izb_igrach)
        time.sleep(3.0)
        break
#input check again
while True:

    if izb_igrach not in ('rock', 'paper', 'scissors'):
        print("Please choose one from them")
        break

#random choice for the computer
    else:
        print("3")
        time.sleep(1.5)
        print("2")
        time.sleep(1.5)
        print("1")
        time.sleep(1.5)
        izbor_comp = random.choice(neshta)
        print("My choice is ", izbor_comp)
        if izbor_comp == neshta[0]:
                b = 8.0
        elif izbor_comp == neshta[1]:
                b = 4.0
        elif izbor_comp == neshta[2]:
                b = 1.0
        time.sleep(2.0)
        
#seeing who wins
        
        c = a / b
        win = [4.0, 2.0, 0.125]
        lose = [8.0, 0.5, 0.25]
        draw = 1.0
        float(draw)
        if c in win:
            print("I win")
        elif c in lose:
            print("You win")
        else:
            print("Draw")

        time.sleep(1.5)
        print("Good game. Restart me if you want to try again")
        break








