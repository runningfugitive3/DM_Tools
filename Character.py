import pickle
import os
import ast
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
    def __init__(self, player_name='Dungeon Master', name=None, d=None, roll=False):
        #Basics
        if not d:
            self.player_name = player_name
            self.name = name
            self._class = "No Class"
            self.level = 1
            self.xp = 0
            self.alive = True
            self.armor_class = 0
            self.hp = 1
            self.hp_max = 1
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
            self.level = int(d['level'])
            self.xp = int(d['xp'])
            self.alive = d['alive']
            self.armor_class = d['armor_class']
            self.hp = int(d['hp'])
            self.hp_max = int(d['hp_max'])
            self.initiative = int(d['initiative'])
            self.speed = int(d['speed'])

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

    def p(self):
        print("\nCHARACTER SHEET\n")
        for key in self.__dict__:
            if '__dict__' not in dir(self.__dict__[key]):
                print("{}: {}".format(key,self.__dict__[key]))
        print("\nABILITIES")
        self.ability.p()
        print("\nSKILLS")
        self.skill.p()
        print("\nAPPEARANCE")
        self.body.p()
        print("\nPERSONALITY")
        self.person.p()
        print("\nINVENTORY")
        self.inventory.p()

        #Actions
        #Attacks & Spellcasting


    def make_dict(self):
        d = {}
        for key in self.__dict__:
            if '__dict__' not in dir(self.__dict__[key]):
                d[key] = self.__dict__[key]
        d['ability'] = self.ability.__dict__
        d['skill'] = self.skill.__dict__
        if 'ability' in d['skill']:
            del d['skill']['ability']
        d['body'] = self.body.__dict__
        d['person'] = self.person.__dict__
        d['inventory'] = self.inventory.__dict__
        return d

    def load_from_db(self, name, filename='DungeonMaster.pickle'):
        '''Returns character as class from filename by first name'''
        with open(filename, 'rb') as f:
            db = pickle.load(f)
            try:
                return self.__init__(db[name]['player_name'], db[name]['name'], db[name])
            except Exception as e:
                print(e)


    def store_to_db(self, filename='DungeonMaster.pickle'):
        '''Stores Character as dict to given pickle file
        Uses character first name as dict key
        Stores Viola Vanish if no filename given for testing'''
        if not os.path.exists(filename):
            db ={}
            with open(filename, 'wb') as f:
                pickle.dump(db,f)
            store_to_db(self, filename)
        d = self.make_dict()
        if ' ' in self.name:
            key = self.name[0:self.name.find(' ')].lower()
        else:
            key = self.name.lower()
        with open(filename, 'rb') as f:
            db = pickle.load(f)
            db[key] = d
        with open(filename, 'wb') as f:
            pickle.dump(db,f)


    def make_tsv(self):
        '''Make a tab separated values file of character class'''
        d = self.make_dict()
        s = ''
        for key in d:
            if type(d[key]) is dict:
                s += '{}\n'.format(key.upper())
                for k in d[key]:
                    s += '{}\t{}\n'.format(k, d[key][k])
            else:
                s += '{}\t{}\n'.format(key, d[key])
        name = self.name.replace(' ','_').lower()
        with open(name + '.tsv', 'w') as f:
            f.write(s)


    def read_tsv(self, filename):
        '''Reads a character csv, returns a character class'''
        with open(filename, 'r') as f:
            l = f.readlines()
        d = {}
        sub_d = None
        for item in l:
            i = item.replace('\n','')
            if '\t' in i and not sub_d:
                d[i.split('\t')[0]] = i.split('\t')[1]
            elif '\t' in i and sub_d:
                if ':' in i or '[' in i:
                    d[sub_d][i.split('\t')[0]] = ast.literal_eval(i.split('\t')[1])
                else:
                    d[sub_d][i.split('\t')[0]] = i.split('\t')[1]
            else:
                sub_d = i.lower()
                d[sub_d] = {}
        return Character(d['player_name'], d['name'], d=d)


def load_from_db(name, filename='DungeonMaster.pickle'):
    '''Returns character as class from filename by first name'''
    with open(filename, 'rb') as f:
        db = pickle.load(f)
        try:
            return Character(db[name]['player_name'], db[name]['name'], db[name])
        except Exception as e:
            print("Didn't find anything for ", e)


def read_tsv(filename):
    '''Reads a character csv, returns a character class'''
    with open(filename, 'r') as f:
        l = f.readlines()
    d = {}
    sub_d = None
    for item in l:
        i = item.replace('\n','')
        if '\t' in i and not sub_d:
            d[i.split('\t')[0]] = i.split('\t')[1]
        elif '\t' in i and sub_d:
            if ':' in i or '[' in i:
                d[sub_d][i.split('\t')[0]] = ast.literal_eval(i.split('\t')[1])
            else:
                d[sub_d][i.split('\t')[0]] = i.split('\t')[1]
        else:
            sub_d = i.lower()
            d[sub_d] = {}
    return Character(d['player_name'], d['name'], d=d)


def main():
    '''For testing purposes'''
    rhea = load_from_db('rhea')
    rhea.p()
    rhea.make_tsv()
    rhea.read_tsv('rhea_galena.tsv')
    rhea.p()


if __name__ == '__main__':
    main()
