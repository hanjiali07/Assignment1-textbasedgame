
class Detective():
    def __init__(self, strength, dex, int):
        self.strength = strength
        self.dex = dex
        self.int = int
    
    def getStats(self):
        print("Stats:")
        return(self.strength, self.dex, self.int)