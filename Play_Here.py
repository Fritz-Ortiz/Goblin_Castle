#Author: Fritz Ortiz
#Github repo: https://github.com/Fritz-Ortiz/Goblin_Castle.git
#LinkedIn: https://www.linkedin.com/in/fritz-ortiz-012388207/


#This is the file you want to run when running this game, for anyone that is trying it out: please do not change the source code unless you know 
#what you're doing and wish to do do a pull request to improve it. If you just wnat to play and don't know how the program works, 
#changing the code might break things. Enjoy!

import time

from Castle_Door_Scene import *
from Character_Creation import *

def main():
    print("Welcome to the Dungeon Crawler Game!")
    print("====================================")
    print("You find yourself in the ancient kingdom of Eldoria, a land once known for its prosperity and peace.")
    print("However, an evil sorcerer named Malifax has taken control of the kingdom and unleashed a horde of goblins.")
    print()
    print("These vile creatures have overrun the once majestic castle and taken hostages, spreading fear and chaos throughout the land.")
    print("As a brave adventurer, you have been chosen to enter the treacherous dungeon beneath the castle, where the goblins have made their lair.")
    print()
    print("Your mission is to navigate the labyrinthine corridors, fight off the goblins, and rescue the hostages to restore peace to Eldoria.")
    print("But be warned, the dungeon is filled with traps, dark magic, and powerful enemies.")
    print()
    print("Equip yourself with weapons, armor, and spells you find along the way, and use your wits and courage to overcome the challenges that lie ahead.")
    answer = input("Are you ready to embark on this perilous adventure and become the savior of Eldoria? (Yes/No) ")
    Decided = False
    while Decided == False:
        if answer.lower() == "no":
            Decided = True
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)

            print("Whether you are a coward or heartless i cannot determine, but i know your name will be forgotten to history...")
            print("Game Over")
        elif answer.lower() != "yes":
            print("Please enter a valid answer next time.")
        else:
            Decided = True
            print("====================================")
            print("====================================")
            print("I knew you were the right person for the job, may the gods bless you. Go forth and conquer those foul beasts")
            print("=================================================================")
            print("======First things first, Let's see what heat your carrying======")
            print("=================================================================")
            Make_Character()
            Entering_The_Castle()









##while(Game_Over != True):
main()