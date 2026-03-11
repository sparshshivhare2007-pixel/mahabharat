import random
from weapons.astras import ASTRAS

def random_weapon():

    weapons = list(ASTRAS.keys())

    drop = random.choice(weapons)

    return drop
