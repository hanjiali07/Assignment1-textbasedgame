from Detective import Detective
from Murderer import Murderer
from Game import Game
print("In the quiet town of Stars Hallow, the Edencrest Manor, a magnificent mansion,held dark secrets. One fateful night, a chilling scream shattered the peace as LordChristian Dior was found murdered in his study.")
print("-------")
print("The Stars Hollow Constabulary, led by Inspector Montgomery, was summoned toinvestigate the crime. Suspicion hung heavy as they interrogated staff and scoured themansion for clues.")
print("-------")
print("Meanwhile, in the shadows of the mansion, a figure lurked—the Murderer. Amaster of disguise and deceit, the Murderer had been living in the shadows of the manor,observing the unfolding events with bated breath. Their aim was to eliminate any tracethat could lead to their apprehension and make a daring escape from the mansionunnoticed.")
print("-------")
print("You stand at the mansion's threshold, facing a choice: Will you embrace thedarkness as the Murderer, seeking to outwit the Inspector and escape the clutches ofjustice, or will you step into the shoes of the Detective, determined to unravel the secretsof Eboncrest Manor and bring the murderer to justice? The choice is yours, and the fateof stars hallow hangs in the balance.")
print("-------")

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

   # total = Game.rollDice()
    total = 12
    print("Current Player Strenght: ")
    print("Rolling Dice: ")
    print(total)
    print(player.strength)

    results = Game.challenge_outcome(total, player.strength)
    print("Making a str check")
    print(results)
    player.strength = player.strength + Game.changeStats(results)
    print("Strength " + str(player.strength))