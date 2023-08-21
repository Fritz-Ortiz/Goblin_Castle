from Player import Stats
stats = Stats()
def Make_Character():
    print("======First things first, Let's see what heat your carrying======")
    print("These are your current stats:")
    print("Health: " + str(stats.get_attribute('Hit Points')) + "         [Your Life energy, if it reaches zero you'll be crossing the river Styx soon after.]")
    print("Dexterity: " + str(stats.get_attribute('Dexterity')) + "       [Your hand-eye coordination, agility, reflexes, and balance. Helps you sneak into the bakery AND dodge the baker's knife.]")
    print("Strength: " + str(stats.get_attribute('Strength'))+ "        [Self-explanatory, do you even lift bro?]")
    print("Constitutuion: " + str(stats.get_attribute('Constitution'))+ "   [Your ability to block damage and resist negative statuses, doesn't fix your alcoholism sadly.]")
    print("Luck: " + str(stats.get_attribute('Fate'))+ "            [How much does fate care about you? flip off the king and find out.]")
    print("===========================================================================================================")
    print("")





    print("|￣￣￣￣￣￣￣￣￣ |  ")
    print("|    Looking Hot    |  ")
    print("|＿＿＿＿＿______＿_|  ")
    print("(\__/) || ")
    print("(•ㅅ•) || ")
    print("/ 　 づ")
    print("========================================")
    print("Character Made ")

Make_Character()