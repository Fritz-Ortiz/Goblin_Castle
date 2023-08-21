#from Character_Creation import *
class Stats:
    def __init__(self):
        self.attributes = {
            'Hit Points': 100,
            'Dexterity': 10,
            'Strength': 10,
            'Constitution': 10,
            'Fate': 10
        }

    def get_attribute(self, attribute_name):
        return self.attributes.get(attribute_name)

    def set_attribute(self, attribute_name, value):
        self.attributes[attribute_name] = value



#stats = Stats()

# Get the value of an attribute
#hit_points = stats.get_attribute('Hit Points')
#print("Hit Points:", hit_points)

# Set the value of an attribute
#stats.set_attribute('Dexterity', 15)
#dexterity = stats.get_attribute('Dexterity')
#print("Dexterity:", dexterity)