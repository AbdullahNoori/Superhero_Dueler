
import random

#a constructor to set the name and attack strength for our Ability just like you did in the last section with name in our Dog classclass Ability:
    
class Ability:
    #Poperty (name, attack_strength)
    def __init__(self, ability_name,  attack_strength):
        self.name = ability_name
        self.max_damage = attack_strength
        #pass
    def attack(self):
        return random.randint(0, self.max_damage)

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block



if __name__ == "__main__":

    ability = Ability("fire", 50)
    print(ability)
    print(ability.attack())
