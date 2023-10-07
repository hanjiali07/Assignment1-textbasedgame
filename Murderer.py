'''this module gives the murderer role it's stats'''
class Murderer():
    def __init__(self, strength, dex, int):
        self.strength = strength
        self.dex = dex
        self.int = int
    
    def getInt(self):
        print("Intelligence: ")
        return(self.int)
    
    def getStrength(self):
        print("Strength: ")
        return(self.strength)
    
    def getDex(self):
        print("Dexterity: ")
        return(self.dex)