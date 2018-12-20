from Dice import Dice

class Ability():
    """docstring for Ability."""
    def __init__(self, d=None, roll=False):
        if not roll:
            if d:
                self.strength = d['strength']
                self.dexterity = d['dexterity']
                self.constitution = d['constitution']
                self.intelligence = d['intelligence']
                self.wisdom = d['wisdom']
                self.charisma = d['charisma']

            if not d:
                self.strength = [0]
                self.dexterity = [0]
                self.constitution = [0]
                self.intelligence = [0]
                self.wisdom = [0]
                self.charisma = [0]

        if roll:
            roll = Dice('character').throw()
            self.strength = [roll[0]]
            self.dexterity = [roll[1]]
            self.constitution = [roll[2]]
            self.intelligence = [roll[3]]
            self.wisdom = [roll[4]]
            self.charisma = [roll[5]]

    def p(self):
        for key in self.__dict__:
            print("{}: {}".format(key,self.__dict__[key]))
