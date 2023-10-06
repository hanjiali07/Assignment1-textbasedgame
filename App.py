from Detective import Detective
from Murderer import Murderer
from Game import Game

intro = "You stand at the mansion's threshold, facing a choice: : Will you succumb to darkness by assuming the role of The Murderer—determined to outsmart Inspector Montgomery and evade justice’s clutches—or will you step into Detective shoes instead?"
print(intro)

isDetective = False
isMurderer = False

storyDecision = input("Do you want to be the detective or murderer?: ")
if(storyDecision == "murderer"):
    print("I'm the murderer")
    strength = 2
    dex = 1
    int = 1
    player = Murderer(strength, dex, int)
else: 
    print("I'm the detective")
    isDetective = True
    strength = -1
    dex = 1
    int = 2
    player = Detective(strength, dex, int)

if isDetective == True:
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


    challenge = input("Hit Enter to roll the dice: ")
    total = Game.rollDice()
    print("Player Intelligence: " + str(player.int))

    results = Game.challenge_outcome(total, player.int)
    print("Making a int check: ")
    print(results)
    player.int = player.int + Game.changeStats(results)
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


    challenge2 = input("Hit Enter to roll the dice: ")
    total = Game.rollDice()
    print("Player Dexterity: " + str(player.dex))

    results = Game.challenge_outcome(total, player.dex)
    print("Making a dex check: ")
    print(results)
    player.dex = player.dex + Game.changeStats(results)
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

    challenge3 = input("Hit Enter to roll the dice: ")
    total = Game.rollDice()
    print("Player Dexterity: " + str(player.dex))
    print("Player Strength: " + str(player.strength))
    print("Player Intelligence: " + str(player.int))

    finalStatsTotal = player.dex + player.strength + player.int

    results = Game.challenge_outcome(total, finalStatsTotal)

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
        print("Wow you won. Slay.")

else:
    #murder story goes here.
    print("pick the other option :D")

print("this is a testing commit")


