#import Character
#import Dice
import pickle
#Store Characters
#Get Characters from store
#Print Character

def character_list(character, subsheet=None):
    '''Creates list with all character attrs'''
    if str(type(character))[1:-1] == "class 'Character.Character'":
        if not subsheet:
            ch_list = ['CHARACTER SHEET', '\n']
            ch_list += key_value_search(character)
            return ch_list


def print_sheet(character, subsheet=None):
    '''Prints Character sheet from character_list'''
    ch_list = character_list(character, subsheet)
    for index in range(len(ch_list)):
        if type(ch_list[index]) is not str:
            ch_list[index] = str(ch_list[index])
    print('\n'.join(ch_list))


def key_value_search(item, l=None):
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
            key_value_search(item.__dict__[key], l)
    else:
        l += [item]
    return l


def load_character(filename='viola_vanish.pickle'):
    '''Loads Character from given pickle file
    Loads Viola Vanish if no filename given for testing'''
    with open(filename, 'rb') as f:
        return pickle.load(f)


def main():
    viola = load_character()
    print_sheet(viola)

if __name__ == '__main__':
    main()