import Character
import pickle
import os
import ast

#Need to send most of these to Character Class as methods

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
    Used by character_tsv'''
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


def load_character(name=None, filename='DungeonMaster.pickle'):
    '''Returns character as class from filename by first name
    if no name given returns entire db as dict'''
    if name:
        name = name.lower()
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
        key = character.name[0:character.name.find(' ')].lower()
    else:
        key = character.name.lower()
    with open(filename, 'rb') as f:
        db = pickle.load(f)
        db[key] = d
    with open(filename, 'wb') as f:
        pickle.dump(db,f)


def ability_modifier(l, plus=[]):
    '''Takes your ability as a list to produce an ability modifier
    minus 10 divide by two round down
    plus attr is used to add/subtract anything from the ability modifier'''
    mod = int(sum(l) - 10 / 2)
    return mod + sum(plus)


def character_tsv(character):
    '''Creates TSV of Character attrs from character_list
    if item in list is UPPER, skips to next line'''
    l = character_list(character)
    name = character.name.replace(' ','_').lower()
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
                    s += '{}\t{}\n'.format(l[i],l[i+1])
                if flip:
                    s += '{}\t{}\n'.format(l[i-1],l[i])
    with open(name + '.tsv', 'w') as f:
        f.write(s)


def read_character_tsv(filename):
    '''Reads a character csv, returns a character dict
    character dict doesnt preserve hierarchy
    Will return a character class soon'''
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
    return Character.Character(d['player_name'], d['name'], d=d)


def main():
    '''For testing purposes'''
    rhea = read_character_tsv('rhea_galena.tsv')
    viola = read_character_tsv('viola_vanish.tsv')
    viola.p()
    rhea.p()

if __name__ == '__main__':
    main()
