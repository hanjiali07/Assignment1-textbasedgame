from Detective import Detective
from Murderer import Murderer
from Game import Game
from tkinter import *

import tkinter.messagebox
root = tkinter.Tk()
messageFont = ("Terminal", 10)
Width, Height = 750, 100

intro = "In the quiet town of Stars Hallow, the Edencrest Manor, a magnificent mansion,held dark secrets. One fateful night, a chilling scream shattered the peace as Lord Christian Dior was found murdered in his study."
intro2 = "Meanwhile, in the shadows of the mansion, a figure lurked—the Murderer. Amaster of disguise and deceit, the Murderer had been living in the shadows of the manor,observing the unfolding events with bated breath. Their aim was to eliminate any tracethat could lead to their apprehension and make a daring escape from the mansionunnoticed"
intro3 ="The Stars Hollow Constabulary, led by Inspector Montgomery, was summoned toinvestigate the crime. Suspicion hung heavy as they interrogated staff and scoured themansion for clues."
intro4 ="Meanwhile, in the shadows of the mansion, a figure lurked—the Murderer. Amaster of disguise and deceit, the Murderer had been living in the shadows of the manor,observing the unfolding events with bated breath. Their aim was to eliminate any tracethat could lead to their apprehension and make a daring escape from the mansionunnoticed."
intro5 ="You stand at the mansion's threshold, facing a choice: Will you embrace thedarkness as the Murderer, seeking to outwit the Inspector and escape the clutches ofjustice, or will you step into the shoes of the Detective, determined to unravel the secretsof Eboncrest Manor and bring the murderer to justice? The choice is yours, and the fateof stars hallow hangs in the balance."

msg = Message(root, text=intro, width=Width, anchor='center',font=messageFont ).grid( row=2, column=0, columnspan=2, sticky="e")
msg2 = Message(root, text=intro2, width=Width, anchor='center',font=messageFont ).grid( row=4, column=0, columnspan=2, sticky="e")
msg3 = Message(root, text=intro3, width=Width, anchor='center',font=messageFont ).grid( row=5, column=0, columnspan=2, sticky="e")
msg4 = Message(root, text=intro4, width=Width, anchor='center',font=messageFont ).grid( row=6, column=0, columnspan=2, sticky="e")
msg5 = Message(root, text=intro5, width=Width, anchor='center',font=messageFont ).grid( row=7, column=0, columnspan=2, sticky="e")

root.title("Mystery of Edencrest Manor")
root.geometry('750x500')

def detectivePopUp():
    tkinter.messagebox.showinfo("Welcome to GFC", "You are now the detective")
    root.destroy()
    import detectivepage

def murdererPopUp():
    tkinter.messagebox.showinfo("Welcome to GFG", "You are now the murderer.")
    root.destroy()
    import murdererpage

#create a button
detectiveButton = Button(root, text="Detective", font=("Terminal",10), command=detectivePopUp, height=2, width=10)
murdererButton = Button(root, text="Murderer", font=("Terminal",10), command=detectivePopUp, height=2, width=10)

#position of button
detectiveButton.place(y = 400, x = 150)
murdererButton.place(y = 400, x = 500 )

strength = 0
int = 0
dex = 0

storyDecision = input("Do you want to be the detective or murderer?: ")
if(storyDecision == "murderer"):
    print("I'm the murderer")
    strength = 2
    dex = 1
    int = 1
    player = Murderer(strength, dex, int)
else: 
    print("I'm the detective")
    strength = -1
    dex = 1
    int = 2
    player = Detective(strength, dex, int)

    total = Game.rollDice()
    print("Current Player Strenght: ")
    print("Rolling Dice: ")
    print(total)
    print(player.strength)

    results = Game.challenge_outcome(total, player.strength)
    print("Making a str check")
    print(results)
    player.strength = player.strength + Game.changeStats(results)
    print("Strength " + str(player.strength))