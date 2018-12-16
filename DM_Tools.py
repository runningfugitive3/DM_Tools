import Character
import pickle
import os

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


def character_list(item, l=None):
    '''Recursive function to compile attrs from Character Class
    Need to rename once its figured out
    Used by character_list and print_sheet for now'''
    if not l:
        l = []
    if '__dict__' in dir(item):
        for key in item.__dict__:
            if '__dict__' in dir(item.__dict__[key]):
                l += [key.upper()]
            else:
                l += [key]
            character_list(item.__dict__[key], l)
    else:
        l += [item]
    return l


def print_sheet(character, subsheet=None):
    '''Prints Character sheet from character_list'''
    if str(type(character))[1:-1] == "class 'Character.Character'":
        if not subsheet:
            ch_list = ['CHARACTER SHEET']
            ch_list += character_list(character)
    for index in range(len(ch_list)):
        if type(ch_list[index]) is not str:
            ch_list[index] = str(ch_list[index])
    print('\n'.join(ch_list))


def load_character(name=None, filename='DungeonMaster.pickle'):
    '''Returns character from filename by first name
    if no name given returns entire db as dict'''
    with open(filename, 'rb') as f:
        if not name:
            return pickle.load(f)
        elif name:
            db = pickle.load(f)
            try:
                return Character.Character(db[name]['player_name'], db[name]['name'], db[name])
            except Exception as e:
                print(e)


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


def character_csv(character):
    '''Creates CSV of Character attrs from character_list
    if item in list is UPPER, skips to next line'''
    l = character_list(character)
    name = character.name.replace(' ','_')
    s = ''
    flip = False
    for i in range(0,len(l)-1):
        if str(l[i]).isupper():
            s += '{}\n'.format(l[i])
            flip = not flip
            print(l[i], flip)
        else:
            if i % 2 == 0:
                if not flip:
                    s += '"{}","{}"\n'.format(l[i],l[i+1])
                if flip:
                    s += '"{}","{}"\n'.format(l[i-1],l[i])
    with open(name + '.csv', 'w') as f:
        f.write(s)

def read_character_csv(filename):
    '''Reads a character csv, returns a character dict
    character dict doesnt preserve hierarchy
    Will return a character class soon'''
    with open(filename, 'r') as f:
        l = f.readlines()
    d = {}
    for item in l:
        i = item.replace('"','').replace('\n','')
        if ',' in item:
            d[i.split(',')[0]] = i.split(',')[1]
    return d


def main():
    '''For testing purposes'''
    d = read_character_csv('Viola_Vanish.csv')
    print(d)

if __name__ == '__main__':
    main()
