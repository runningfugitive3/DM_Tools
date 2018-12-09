import random as r

class Dice():
    """docstring for Dice.
    Put in the number of the sides for the dice_type or
    'character' for an abilities roll"""
    def __init__(self, dice_type):
        self.dice_type = dice_type

    def throw(self):
        roll = []
        if type(self.dice_type) == int:
            roll.append(r.randint(1, self.dice_type))
            return roll
        elif type(self.dice_type) == str:
            if self.dice_type.lower() == "character":
                for ability in range(6):
                    die = [r.randint(1,6) for num in range(4)]
                    die.sort()
                    print(die)
                    roll.append(sum(die[1:4]))
                print(roll)
                return roll
        else:
            print("I don't recognize '{}' as a dice_type. You need to generate a new Dice.".format(self.dice_type))
