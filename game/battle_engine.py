import random

def normal_attack(level):
    return random.randint(120,220) + level*10

def special_attack(level):
    return random.randint(300,420) + level*20
