import Character
#import Dice
import pickle
import os
#Store Characters
#Get Characters from store
#Print Character

def character_list(character, subsheet=None):
    '''Creates list with all character attrs'''
    #add subsheet feature later
    if str(type(character))[1:-1] == "class 'Character.Character'":
        if not subsheet:
            ch_list = ['CHARACTER SHEET', '\n']
            ch_list += key_value_list(character)
            return ch_list


def character_dict(item, d=None):
    '''Recursive function to compile attrs from Character Class'''
    if not d:
        d = {}
    if '__dict__' in dir(item):
        for key in item.__dict__:
            if '__dict__' in dir(item.__dict__[key]):
                d[key] = character_dict(item.__dict__[key])
            else:
                d[key] = item.__dict__[key]
    return d


def key_value_list(item, l=None):
    '''Recursive function to compile attrs from Character Class
    Need to rename once its figured out
    Used by character_list and print_sheet for now'''
    if not l:
        l = []
    if '__dict__' in dir(item):
        for key in item.__dict__:
            if '__dict__' in dir(item.__dict__[key]):
                l += ['\n', key.upper()]
            else:
                l += [key]
            key_value_list(item.__dict__[key], l)
    else:
        l += [item]
    return l

def print_sheet(character, subsheet=None):
    '''Prints Character sheet from character_list'''
    ch_list = character_list(character, subsheet)
    for index in range(len(ch_list)):
        if type(ch_list[index]) is not str:
            ch_list[index] = str(ch_list[index])
    print('\n'.join(ch_list))


def load_character(name=None, filename='DungeonMaster.pickle'):
    '''Returns Character db dict from given pickle file
    if name is given returns that specific character dict'''
    with open(filename, 'rb') as f:
        if not name:
            return pickle.load(f)
        elif name:
            db = pickle.load(f)
            try:
                return db[name]
            except Exception as e:
                print(e, "Character name not found")
    #Should load direct to Character class
    #Need to figure out how to address differences in dict vs Character class 

def store_character(character, filename='DungeonMaster.pickle'):
    '''Stores Character as dict to given pickle file
    Uses character first name as dict key
    Stores Viola Vanish if no filename given for testing'''
    if not os.path.exists(filename):
        db ={}
        with open(filename, 'wb') as f:
            pickle.dump(db,f)
        store_character(character, filename)
    d = character_dict(character)
    if ' ' in character.name:
        key = character.name[0:character.name.find(' ')]
    else:
        key = character.name
    with open(filename, 'rb') as f:
        db = pickle.load(f)
        db[key] = d
    with open(filename, 'wb') as f:
        pickle.dump(db,f)


def ability_modifier(l, plus=[]):
    '''Takes your ability list to produce an ability modifier
    plus is to add/subtract anything from the ability modifier'''
    mod = int(sum(l) - 10 / 2)
    return mod + sum(plus)


def main():
    '''For testing purposes'''
    ch = load_character1(filename='rhea_galena.pickle')
    d = character_dict(ch)
    print(d)
    store_character(ch)
    db = load_character2()
    print(db)


if __name__ == '__main__':
    main()
