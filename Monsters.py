import random
from Attacks import *

class Goblin:
    def Life_Points():
        health = random.randint(40,65)
        return health
    def attacks():
        Which_Attack = random.randint(1,3)
        if Which_Attack == 1: 
            return "Punches for " + str(Light_Punch()) + " Hit Points"
        elif Which_Attack == 2:
            return "Slashes for " + str(Shortsword_Slash()) + " Hit Points"
        else:
            return "Bites for " + str(Sick_bite()) + " Hit Points"

