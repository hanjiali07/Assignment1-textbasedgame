from tkinter import *
from Game import Game
from Detective import Detective

root = Tk()
root.geometry ("750x500")
root.title("Mystery of Edencrest Manor")

Width, Height = 750, 500
messageFont = ("Terminal",8)

strength = -1
dex = 1
int = 2
player = Detective(strength, dex, int)

f = ("Terminal", 20)

total = Game.rollDice()  
print("Rolling Dice: ")
print("Current Player Strength: ")
print(total)
print(player.strength)
results = Game.challenge_outcome(total, player.strength)
print(results)

if Game.changeStats(results) == True:
    player.strength = player.strength + Game.changeStats(results)
    print("Strength " + str(player.strength))
root.mainloop()
