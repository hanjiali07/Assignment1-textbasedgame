import random

''' implements the game data and logic.
this module rolls the dice and changes the stats and determines whether its a win/loss.'''

class Game():
    def rollDice():
        '''rolling the dice'''
        result = []
        roll = random.randint(1,6)
        print("Dice 1: " + str(roll))
        roll2 = random.randint(1,6)
        print("Dice 2: " + str(roll2))
        result = roll + roll2
        return(result)
    
    def challenge_outcome(total, modifier):
        '''calculates whether its a win/loss'''
        total = total + modifier
        print("The modified total: " + str(total))
        if total == 2 or total == 3:
            return ("Critical Loss")
        elif total <= 4 or total <= 7:
            return ("Loss")
        elif total <= 8 or total <= 10:
            return ("Win")
        elif total == 11 or total >= 12:
            return("Critical Win")
        
    def changeStats(result):
        '''determine whether or not to change stats'''
        if result == "Critical Loss":
            return -1
        elif result == "Critical Win":
            return 1
        else:
            return 0
    