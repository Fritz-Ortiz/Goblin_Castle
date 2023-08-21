def Entering_The_Castle():
    print("====================================")
    print("Approaching the castle doors, you notice that the environment is silent. Too silent.")
    print("In front of you now are the doors, and you can see that they open just enough for you to get through quietly if you're careful.")
    
    decided=False
    while decided == False:
        decision = input("What do you do? (Sneak in/Rush in/Escape)")
        if decision.lower().replace(" ", "") ==  "sneakin":
            decided = True
            Sneak_Into_Castle()
        elif decision.lower().replace(" ", "") == "rushin":
            decided = True
            Rush_Into_Castle()
        elif decision.lower().replace(" ", "") == "escape":
            decided = True
            print("You decide this line of work is not for you, you kinda have to go to the bathroom too. Someone will take care of this.... right?")
            print("Game Over")
        else:
            print("Invalid command, try again")

def Sneak_Into_Castle():
    print("you sneak in")

def Rush_Into_Castle():
    print("you rush in")

