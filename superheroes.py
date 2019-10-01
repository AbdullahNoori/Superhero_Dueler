
import random

#a constructor to set the name and attack strength for our Ability just like you did in the last section with name in our Dog classclass Ability:
    
class Ability:
#Poperty name, attack_strength
    def __init__(self, ability_name,  attack_strength):
        self.name = ability_name
        self.max_damage = attack_strength
        #pass
    
    def attack(self):
        return random.randint(0, self.max_damage)
#ADD CLASS ARMOR-
class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    
    def block(self):
        return random.randint(0, self.max_block)
#ADD CLASS HERO-
class Hero:
    def __init__(self, name, starting_health= 100):
        """Instance properties:
        abilities: List
        armor: List
        name: String
        starting_health: Integer
        current_health: Integer
        """
        self.name = name
        self.abilities = []
        self.starting_armor = []
        self.starting_health = starting_health
        self.current_health= starting_health
        self.kills = 0
        self.deaths = 0
        

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)
        
    def add_deaths(self, number_deaths):
        self.deaths += number_deaths
    
    def add_kills(self, number_kills):
        self.kills += number_kills

    def attack(self):
        total = 0 
        for ability in self.abilities:
            total = total + ability.attack()
        return total
    
    def defend(self):
        total_defense = 0
        for armor in self.starting_armor:
            total_defense += armor.block()
        return total_defense

    def take_damage(self, damage):
        self.damage -= self.defend()
        if damage < 0:
            damage =0
        self.current_health -= damage



if __name__ == "__main__":
# If you run this file from the terminal
# this block is executed.
    # ability = Ability("fire", 50)
    # print(ability)
    # print(ability.attack())

    #test2 - class Hero
#   my_hero = Hero("Grass Hopper", 200)
#     print(my_hero.name)
#     print(my_hero.current_health)
#     #test abilities  
    # hero = Hero("Grace Hopper", 200)
    # ability = Ability("Great Debugging", 50)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # print(hero.abilities)

    
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())









