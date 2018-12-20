class Person():
    """docstring for Person."""
    def __init__(self, d=None):
        if not d:
            self.backstory = None
            self.background = None
            self.personality = None
            self.features_traits = None
            self.proficiencies = None
            self.languages = ['Common']
            self.ideals = None
            self.bonds = None
            self.flaws = None
            self.alignment = None
            self.faction = None
            self.allies_organizations = None

        if d:
            self.backstory = d['backstory']
            self.background = d['background']
            self.personality = d['personality']
            self.features_traits = d['features_traits']
            self.proficiencies = d['proficiencies']
            self.languages = d['languages']
            self.ideals = d['ideals']
            self.bonds = d['bonds']
            self.flaws = d['flaws']
            self.alignment = d['alignment']
            self.faction = d['faction']
            self.allies_organizations = d['allies_organizations']

    def p(self):
        for key in self.__dict__:
            print("{}: {}".format(key,self.__dict__[key]))
