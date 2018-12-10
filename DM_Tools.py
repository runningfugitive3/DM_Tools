#import Character
#import Dice
import pickle
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

def character_dict2(item, d=None):
    '''Testing - Recursive function to compile attrs from Character Class'''
    if not d:
        d = item.__dict__
    if '__dict__' in dir(item):
        for key in item.__dict__:
            d[key] = item[key].__dict__
    return d

def character_dict(item, d=None):
    '''Recursive function to compile attrs from Character Class
    Functioning but doesn't preserve hierarchy '''
    if not d:
        d = {}
    if '__dict__' in dir(item):
        for key in item.__dict__:
            d[key] = item.__dict__[key]
            character_dict(item.__dict__[key], d)
    return d


def key_value_list(item, l=None):
    '''Recursive function to compile attrs from Character Class
    Need to rename once its figured out'''
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

def load_character(filename='viola_vanish.pickle'):
    '''Loads Character from given pickle file
    Loads Viola Vanish if no filename given for testing'''
    with open(filename, 'rb') as f:
        return pickle.load(f)

def store_character(character, filename='viola_vanish.pickle'):
    '''Stores Character to given pickle file
    Stores Viola Vanish if no filename given for testing'''
    with open(filename, 'wb') as f:
        pickle.dump(character, filename)

def ability_modifier(l, plus=[]):
    '''Takes your ability list to produce an ability modifier
    plus is to add/subtract anything from the ability modifier'''
    mod = int(sum(l) - 10 / 2)
    return mod + sum(plus)

def main():
    '''For testing purposes'''
    viola = load_character()
    d = character_dict2(viola)
    print(d)

if __name__ == '__main__':
    main()
