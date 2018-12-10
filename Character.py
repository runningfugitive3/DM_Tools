from Ability import Ability
from Body import Body
from Person import Person
from Skill import Skill

class Character():
    """docstring for Character. This can be used for Monsters and NPCs, also.
    Just replace player_name with Monster or NPC."""
    def __init__(self, player_name, name):
        #Basics
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

        self.ability = Ability()
        self.body = Body()
        self.person = Person()
        self.skill = Skill(self.ability)
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
