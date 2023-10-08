from Detective import Detective
from Murderer import Murderer
from Game import Game
import tkinter
from tkinter import *
from PIL import Image, ImageTk

import tkinter.messagebox

"""This module implements the interactivity with the user.
"""
root = tkinter.Tk()
root.title("Mystery Of Edencrest Manor")
root.geometry("500x750")
Width, Height = 500, 750


canvas = tkinter.Canvas(root, width=Width, highlightthickness=0) #creates canvas
canvas.pack(side = "bottom", fill="both", expand="yes")

path_of_image = 'coverart.jpg' #this is where to get the image
image1 = ImageTk.PhotoImage(Image.open(path_of_image)) #open image
canvas.create_image(250, 400, image=image1)

title = "Mystery of Edencrest Manor" # title of the interface
canvas.create_text(250, 200, text="Mystery Of Edencrest Manor", font="Terminal 20", fill='white')


def start():
    '''this function gets rid of the interface and stars the game'''
    root.destroy()

startButton = Button(root, text="Start", font=("Terminal",10), command=start, height=2, width=10) #button to start the game
startButton.place(x = 205, y = 600)


root.mainloop()

#introduction to the story
introOne = print("Deep within the serene town of Stars Hallow, a notorious residence known as Edencrest Manor concealed its sinister mysteries.")
introTwo = print("One ill-fated evening, an ear-piercing shriek shattered the tranquillity when Lord Christian Dior's lifeless body was discovered in his private study. ")
introThree = print("Inspector Montgomery and his diligent team from the Stars Hollow Constabulary were urgently summoned to investigate this heinous crime.")
introFour = print("With suspicion looming heavily in the air, they meticulously questioned every staff member while scouring the vast manor for any semblance of evidence.")
introFive = print("Meanwhile, amidst the shadows that engulfed the mansion, a mysterious figure skulked—the Murderer. Residing within Edencrest Manor's dark corners, they observed each unfolding moment with bated breath. ")
introSix = print("Their ultimate objective? Eradicate all potential traces leading back to their identity and execute a daring escape without raising even an inkling of suspicion.")
intro = "You stand at the mansion's threshold, facing a choice: : Will you succumb to darkness by assuming the role of The Murderer—determined to outsmart Inspector Montgomery and evade justice’s clutches—or will you step into Detective shoes instead? Welcome, to the Mystery of Edencrest Manor."


isDetective = False #initializing variable for detective story
isMurderer = False  #initializing variable for murderer story


def detectiveStory():
    '''this function is the detective story along with the dice rolling.'''
    print("Role choice: Detective")
    print("As the Detective, you find yourself standing at Edencrest Manor, a foreboding place. The study door is slightly ajar.")
    print("After entering you see an envelope, on the desk with Lord Dior’s one-of-a-kind wax seal addressed to 'Cassandra'. Could it conceal dangerous secrets linked to a forbidden love affair?")
    print("Nearby, The broken windowpane suggests that someone may have recently intruded. Above the fireplace, Lady Isabella's portrait conceals secrets about her husband's unfaithfulness, fueling suspicions.")
    print("As you delve deeper into the mystery a story of secretive romance unfolds: Lord Dior’s hidden affair and Lady Elizabeth's growing doubts. Deception and betrayal lurk within Edencrest Manor's grand walls.")
    print("Guided by your intellect you are determined to uncover the truth using the clues at hand. The thrill of discovery consumes you as you edge closer, to revealing what lies beneath.")
    print("Your mission has now commenced and the roll of the dice will determine the path you take to unearth the secrets concealed within Edencrest Manor.")
    print()
    print("Challenge 1: Gathering Clues")
    print("Your first challenge is to search the mansion for vital clues that may lead you to the murderer. This challenge relies on your Intelligence (IQ).")


    challenge = input("Hit Enter to roll the dice: ") #user input to roll dice
    total = Game.rollDice() 
    print(Detective.getInt(player))
    results = Game.challenge_outcome(total, player.int) #gets roll outcome
    print("Making a int check: ")
    print(results)
    player.int = player.int + Game.changeStats(results) #this get this  new stat from rolling the dice
    if(results == "Critical Loss"):
        print("You've missed crucial evidence, your intelligence has been dropped.")
    elif(results == "Critical Win"):
        print("You uncover all key evidence. Your intelligence is raised")
    elif(results == "Loss"):
        print("You find some clues but not enough to make progress. No stats have changed.")
    else:
        print("You gather significant clues. No stats have changed.")
    print("Intelligence after challenge: " + str(player.int))
    
    challengeOneEnd = input("Challenge one end, enter to continue: ")
    print("With the vital clues in your possession, you shift your focus towards interrogating the staff and guests residing in the mansion.")
    print("The intricate network of relationships within Edencrest Manor grows increasingly fascinating as each connection holds the potential for a clue in solving this perplexing puzzle.")
    print("Your initial suspect is none other than Lord Christian Dior's trusted confidant and closest friend, the butler.")
    print("The undeniable bond they share raises suspicions about whether this heinous crime could be fueled by revenge or a betrayal among friends.")
    print("Moving on you approach Cassandra Hawthorne, who has been serving as a maid in the manor for quite some time.")
    print("She happens to be married to the chef renowned for his culinary expertise.")
    print("The doubts her husband harbor’s concerning their son's paternity cast a shadow of uncertainty over their family dynamics introducing a layer of complexity to our investigation.")
    print("Lastly, you engage in conversation with the chef himself Mr. Hawthorne. A man deeply distressed about his missing son.")
    print("He discloses that his son shares a connection with Lady Elizabeth that transcends their roles as employer and employee.")
    print("The chef's revelation regarding his son's presence near Lady Elizabeth raises questions, about their interactions and possible motives.")
    print("Once again, it is the roll of the dice which holds your fate, influencing the course of these conversations and whether you can gain further insight into the intricate web of relationships and uncover the truth behind the murder of Lord Nathaniel Blackthorn. ")
    print()
    print("Challenge 2: Interrogating Suspects")
    print("In this challenge, your Dexterity (DX) will be essential for your success in questioning the mansion's staff and suspects.")


    challenge2 = input("Hit Enter to roll the dice: ") #rolling the dice
    total = Game.rollDice()
    print(Detective.getDex(player))

    results = Game.challenge_outcome(total, player.dex) #gets the dice roll outcome
    print("Making a dex check: ")
    print(results)
    player.dex = player.dex + Game.changeStats(results) #gets the new stats 
    if(results == "Critical Loss"):
        print("You offend the suspects and get misleading information. Your dexterity has been dropped.")
    elif(results == "Critical Win"):
        print("You skillfully extract confessions. Your dexterity is raised")
    elif(results == "Loss"):
        print("You struggle to extract useful information. No stats have changed.")
    else:
        print("You obtain valuable insights. No stats have changed.")
    print("Dexterity after challenge: " + str(player.dex))

    challengeTwoEnd = input("Challenge two end, enter to continue: ")

    print("As the Detective, you have almost come to the end of your investigation and now the last hour for unveiling the murderer’s true face has arrived.")
    print("With the knowledge you’ve gained throughout this investigation your final challenge is to piece together the evidence and make an accurate deduction.")
    print("Could the murderer be: Lady Elizabeth, betrayed and seething with anger; Cassandra Hawthorne, entangled in a forbidden affair; Chef Hawthorne, harboring jealousy and secrets; the bruting son, heir to the Dior legacy; or the loyal butler, hiding behind a facade.")
    print("You are armed with a wealth of evidence and a deep understanding of the suspects and their motivations.")
    print("Given your Intelligence (IQ), Strength (ST), and Dexterity (DX) capabilities, the complex web of love, treachery, and secrets inside Edencrest Manor is now clear.")
    print("The roll of the dice now holds the key to bringing the murderer to justice.")
    print()
    print("Final Challenge: Identifying the Culprit.")
    print("Your final challenge is to piece together the evidence and make an accurate deduction.")

    challenge3 = input("Hit Enter to roll the dice: ")#rolling the dice
    total = Game.rollDice()
    print(Detective.getDex(player))
    print(Detective.getStrength(player))
    print(Detective.getInt(player))

    finalStatsTotal = player.dex + player.strength + player.int #gets stats for all attributes

    results = Game.challenge_outcome(total, finalStatsTotal) #prints the outcome of stats

    print("Making the final check: ")
    print(results)
    if(results == "Critical Loss"):
        print("You accuse the wrong person, letting the real killer go free.")
        isWin = False
    elif(results == "Critical Win"):
        print("You not only identify the killer but also capture them, ensuring justice is served.")
        isWin = True
    elif(results == "Loss"):
        print("You're close but not entirely correct.")
        isWin = False
    else:
        print("You correctly identify the murderer.")
        isWin = True

    if(isWin == False):
        print("You lost! Twenty-three years ago, Christian Dior had an affair with the housemaid Cassandra Hawthorne that resulted in the birth of a son whom was the legitimate inheritor of lord Dior's wealth.")
        print("Lady Elizabeth, being aware of this situation, engaged in her own affair with Cassandra's son. In hopes of gaining wealth and authority, the son murdered Christian Dior while Lady Elizabeth, complicit in this act benefited from it as well.")
        print("Due to your incompetence, they managed to get away with murder and you were fired from the inspection team.")
    else:
        print("You Won! You caught the killer who turned out to be the son of Cassandra Hawthorne and Lord Christian Dior– the product of an affair.")
        print("Lady Elizabeth, being aware of this situation, engaged in her own affair with Cassandra's son. ")
        print("In hopes of gaining wealth and authority, the son murdered Christian Dior while Lady Elizabeth, complicit in this act, benefited from it as well.")
        print("Due to this victory, you have been declared the best detective in Stars Hallow and you have been promoted to head of your department resulting in a huge pay raise!")

def murdererStory():
    '''this function includes the murderer role and story along with the dice roll.'''
    print("Role: Murderer")
    print("Twenty-three years ago, Christian Dior had an affair with the housemaid Cassandra Hawthorne which resulted in the birth of a son who was the legitimate inheritor of lord Dior's wealth – you.")
    print("Lady Elizabeth, being aware of this situation, engaged in her own affair with you.")
    print("In hopes of gaining wealth and authority, you murdered Christian Dior while your lover, Lady Elizabeth, complicit in this act benefited from it as well.")
    print()
    print("Challenge 1: Elimitating Evidence")
    print("Your first challenge is to erase any trace of your presence at the crime scene. This challenge relies heavily on your Dexterity (DX) attribute.")

    challenge = input("Hit Enter to roll the dice: ") # rolls dice
    total = Game.rollDice()
    print(Murderer.getDex(player))

    results = Game.challenge_outcome(total, player.dex)
    print("Making a dex check: ")
    print(results)
    player.dex = player.dex + Game.changeStats(results)
    if(results == "Critical Loss"):
        print("You make a mess, and the Inspector is hot on your trail. Your dexterity has been dropped.")
    elif(results == "Critical Win"):
        print("You eliminate all evidence and gain confidence. Your dexterity is raised")
    elif(results == "Loss"):
        print("You leave behind some incriminating evidence. No stats have changed.")
    else:
        print("You clean up the scene without a hitch. No stats have changed.")
    print("Dexterity after challenge: " + str(player.dex))
    challengeOneEnd = input("Challenge one end, enter to continue: ")

    print("In the dimly lit halls of Edencrest Manor, a sense of unease consumes you.")
    print("The butler,  your mother, the housemaid and the chef ( idk how to word that the chef is his dad not his biological dad) are being relentlessly questioned by the Inspector.")
    print("Their responses could determine whether you will be held responsible for the alleged murder of Lord Christian Dior.")
    print("As you realise the gravity of the situation adrenaline courses through your veins.")
    print("Your only defence in this game is your intellect. As you observe the scene around you you notice the suspicious expressions on the faces of the mansion's staff.")
    print("It becomes crucial for you to blend in seamlessly among them. With each step calculated carefully you manage to slip from the interrogation and join servants who are engrossed in their duties.")
    print("Your objective is to appear immersed while remaining detached from the unfolding drama.")
    print("Relying on your intellect you navigate through conversations, laughter and potential traps as lingering suspicion hangs heavy in the air.")
    print("Any misstep could draw attention from the piercing gaze of the Inspector towards yourself.")
    print("In your quest for safety your ultimate aim is to find Lady Elizabeth. Perhaps she can offer some protection or at least divert attention away from yourself. The roll of the dice will determine your success.")
    print()
    print("Challenge 2: Dodging Suspicion")

    challengeTwo = input("Hit Enter to roll the dice: ")
    total = Game.rollDice()
    print(Murderer.getInt(player))
    results = Game.challenge_outcome(total, player.int)
    print("Making a int check: ")
    print(results)
    player.int = player.int + Game.changeStats(results)
    if(results == "Critical Loss"):
        print("You draw suspicion to yourself. Your intelligence has been dropped.")
    elif(results == "Critical Win"):
        print("You successfully divert suspicion away from yourself. Your intelligence is raised")
    elif(results == "Loss"):
        print("You struggle to maintain your cover. No stats have changed.")
    else:
        print("You go unnoticed. No stats have changed.")
    print("Intelligence after challenge: " + str(player.int))

    challengeTwoEnd = input("Challenge two end, enter to continue: ")

    print("In the midst of the tense ambiance enveloping Edencrest Manor, your final challenge presents itself: escaping the relentless Inspector.")
    print("As you navigate through poorly illuminated passageways, your path to liberation is obstructed by locked doors and barred windows.")
    print("Your physical and mental strength are put to the test as you grapple with these obstacles.")
    print("A glimmer of hope emerges in Lady Elizabeth's message, assuring a rendezvous on the opposite side of the lake—a beacon of hope amidst this dire predicament.")
    print("The final obstacle is a heavy oak door secured firmly shut. Should you succeed in prying it open, a small boat awaits upon the tranquil waters ahead.")
    print("With fate hanging from your trembling hand, you cast forth the dice whilst praying for triumph; your very life and future hinge upon its outcome.")
    print()
    print("Final Challenge: The Great Escape")
    print("Your final challenge is to make a daring escape from Edencrest Manor. This challenge relies on your Strength (ST) to overcome obstacles in your path and slip away undetected.")

    challengeThree = input("Hit Enter to roll the dice: ")
    total = Game.rollDice()
    print(Murderer.getStrength(player))
    print("Making a strength check: ")
    print(results)
    player.int = player.int + Game.changeStats(results)
    if(results == "Critical Loss"):
        print("You draw suspicion to yourself. Your intelligence has been dropped.")
    elif(results == "Critical Win"):
        print("You successfully divert suspicion away from yourself. Your intelligence is raised")
    elif(results == "Loss"):
        print("You struggle to maintain your cover. No stats have changed.")
    else:
        print("You go unnoticed. No stats have changed.")
    print("Intelligence after challenge: " + str(player.int))

    challengeThreeEnd = input("Final challenge end, enter to continue: ")

    print("Making the final check: ")
    print(results)
    if(results == "Critical Loss"):
        print("You accuse the wrong person, letting the real killer go free.")
        isWin = False
    elif(results == "Critical Win"):
        print("You not only identify the killer but also capture them, ensuring justice is served.")
        isWin = True
    elif(results == "Loss"):
        print("You're close but not entirely correct.")
        isWin = False
    else:
        print("You correctly identify the murderer.")
        isWin = True

    if(isWin == False):
        print("You lost! You get caught by the inspector Lady Elizabeth leaves you in the dust. You have been sentenced to death for the murder of Lord Christian Dior.")
    else:
        print("You win! You made your great escape with Lady Elizabeth and received your inheritance!")

storyDecision = input("Do you want to be the detective or murderer?: ")
if(storyDecision == "murderer" or storyDecision == "Murderer"):
    print("I'm the murderer")
    strength = 2
    dex = 1
    int = -1
    player = Murderer(strength, dex, int)
else: 
    print("I'm the detective")
    isDetective = True
    strength = -1
    dex = 1
    int = 2
    player = Detective(strength, dex, int)
if isDetective == True:
    detectiveStory()

else:
    #murder story is here
   murdererStory()
