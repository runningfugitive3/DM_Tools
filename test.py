import Character as ch
from Dice import Dice

viola = ch.Character("Sean Avitt", "Viola Vanish")
print("Hi!, I'm {}".format(viola.name))
print("My owner is {}".format(viola.player_name))
print("My wisdom score is {}".format(viola.ability.wisdom))
print("My stealth score is {}".format(viola.skill.stealth))

d = Dice("character")
print(d.throw())
