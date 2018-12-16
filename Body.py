class Body():
    """docstring for Body."""
    def __init__(self, d=None):
        #Phyiscal
        if not d:
            self.race = "Human"
            self.age = 21
            self.height = 6 # feet
            self.weight = 200 # pounds
            self.eyes = "blue"
            self.skin = "scaly"
            self.hair = "wavy"
            self.appearance = "Fugly"

        if d:
            self.race = d['race']
            self.age = d['age']
            self.height = d['height']
            self.weight = d['weight']
            self.eyes = d['eyes']
            self.skin = d['skin']
            self.hair = d['hair']
            self.appearance = d['appearance']
