class Skill():
    """docstring for Skill.
    Not sure if this will work like this having Skill
    dependant on Ability"""
    def __init__(self, ability, d=None):
        if not d:
            self.init_skills(ability)

        if d:
            self.athletics = d['athletics']
            self.acrobatics = d['acrobatics']
            self.sleight_of_hand = d['sleight_of_hand']
            self.stealth = d['stealth']
            self.arcana = d['arcana']
            self.history = d['history']
            self.investigation = d['investigation']
            self.nature = d['nature']
            self.religion = d['religion']
            self.animal_handling = d['animal_handling']
            self.insight = d['insight']
            self.medicine = d['medicine']
            self.perception = d['perception']
            self.survival = d['survival']
            self.deception = d['deception']
            self.intimidation = d['intimidation']
            self.performance = d['performance']
            self.persuasion = d['persuasion']

    def init_skills(self, ability):
        str_mod = int((sum(ability.strength) - 10) / 2)
        dex_mod = int((sum(ability.dexterity) - 10) / 2)
        int_mod = int((sum(ability.intelligence) - 10) / 2)
        wis_mod = int((sum(ability.wisdom) - 10) / 2)
        cha_mod = int((sum(ability.charisma) - 10) / 2)

        #Skills
        self.athletics = [str_mod]
        self.acrobatics = [dex_mod]
        self.sleight_of_hand = [dex_mod]
        self.stealth = [dex_mod]
        self.arcana = [int_mod]
        self.history = [int_mod]
        self.investigation = [int_mod]
        self.nature = [int_mod]
        self.religion = [int_mod]
        self.animal_handling = [wis_mod]
        self.insight = [wis_mod]
        self.medicine = [wis_mod]
        self.perception = [wis_mod]
        self.survival = [wis_mod]
        self.deception = [cha_mod]
        self.intimidation = [cha_mod]
        self.performance = [cha_mod]
        self.persuasion = [cha_mod]

    def p(self):
        for key in self.__dict__:
            print("{}: {}".format(key,self.__dict__[key]))
