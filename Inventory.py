class Inventory():
    """docstring for Inventory."""
    def __init__(self, d=None):
        if not d:
            self.coin = {'cp': 0, 'sp': 0, 'ep': 0, 'gp': 0, 'pp': 0}
            self.weapon = {'spife': 'It\'s a spoon-knife imbued with flavor from the inside of the last person\'s mouth who owned it.'}
            self.armor = {'rags':'You\'re poor. At least, you\'re not naked?'}
            self.other = {'trinket': 'Because for some reason, DnD really wants you to have some weird kitchy piece of shit with a inordinately complex backstory-- also it\'s fun!'}

        if d:
            self.coin = d['coin']
            self.weapon = d['weapon']
            self.armor = d['armor']
            self.other = d['other']
