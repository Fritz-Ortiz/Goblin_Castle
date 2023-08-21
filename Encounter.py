from Monsters import *
from Player import *

ready = input("Are you ready to fight? (Y/N) ")

if ready == "Y":
    print("You encounter a goblin with " + str(Goblin.Life_Points()) + " Hit Points. It attacks and " + Goblin.attacks())

else:
    print("Coward")
