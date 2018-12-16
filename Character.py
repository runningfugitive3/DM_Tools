from Ability import Ability
from Body import Body
from Person import Person
from Skill import Skill
from Inventory import Inventory

class Character():
    """docstring for Character. This can be used for Monsters and NPCs, also.
    Just replace player_name with Monster or NPC.
    Add dict of character for d to load character
    roll=True to have auto assigned stats"""
    def __init__(self, player_name, name, d=None, roll=False):
        #Basics
        if not d:
            self.player_name = player_name
            self.name = name
            self._class = "No Class"
            self.level = 1
            self.XP = 0
            self.alive = True
            self.armor_class = 0
            self.HP = 1
            self.initiative = 0
            self.speed = 0

            self.ability = Ability(roll=roll)
            self.body = Body()
            self.person = Person()
            self.skill = Skill(self.ability)
            self.inventory = Inventory()

        if d:
            self.player_name = d['player_name']
            self.name = d['name']
            self._class = d['_class']
            self.level = d['level']
            self.XP = d['XP']
            self.alive = d['alive']
            self.armor_class = d['armor_class']
            self.HP = d['HP']
            self.initiative = d['initiative']
            self.speed = d['speed']

            if 'ability' in d.keys():
                self.ability = Ability(d=d['ability'], roll=roll)
            else:
                self.ability = Ability(roll=roll)

            if 'body' in d.keys():
                self.body = Body(d=d['body'])
            else:
                self.body = Body()

            if 'person' in d.keys():
                self.person = Person(d=d['person'])
            else:
                self.person = Person()

            if 'skill' in d.keys():
                self.skill = Skill(self.ability, d=d['skill'])
            else:
                self.skill = Skill(self.ability)

            if 'inventory' in d.keys():
                self.inventory = Inventory(d=d['inventory'])
            else:
                self.inventory = Inventory()

        #Actions
        #Attacks & Spellcasting




#csv parser to build Character?
        #def ch_load(self) use pickle
        #with open(first and last.pickle,'rb') as f:
        #character = pickle.load(f)

        #def ch_store(self) use pickle
        #with open(first_last.pickle,'rb') as f:
        #pickle.dump(self, f)

        #def sheet(self, keyword=none):
        #if not keyword:
            #self.
        #[i for i in dir(viola.ability) if not callable(i) and i[1] is not '_']

# Build function that would go through each attr in d
# And find corresponding class attr instead of having to hard type it in each class?

def main():
    '''For testing purposes'''
    test1 = Character("No One", "Char Tere", roll=True)
    print("Name: {}\nStrength: {}\nAthletics: {}".format(test1.name, test1.ability.strength, test1.skill.athletics))

if __name__ == '__main__':
    main()
