import random

#a constructor to set the name and attack strength for our Ability just like you did in the last section with name in our Dog classclass Ability:
    
class Ability:
#Poperty name, attack_strength
    def __init__(self, ability_name,  attack_strength):
        self.name = ability_name
        self.]max_damage = attack_strength
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
        self.armor = []
        self.starting_health = starting_health
        self.current_health= starting_health
        self.kills = 0
        self.deaths = 0
        

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armor.append(armor)

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
        for armor in self.armor:
            total_defense += armor.block()
        return total_defense

    def take_damage(self, damage):
        damage -= self.defend()
        if damage < 0:
            damage =0
        self.current_health -= damage

    def is_alive(self):
        return self.current_health > 0

    def fight(self, opponent):
        if self.abilities != [] or opponent.is_abilities != []:
            
            while self.is_alive() and opponent.is_alive():
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())
                print(f"{self.name} has {self.current_health} health!")

            if self.is_alive():
                print(f"{self.name} Wins!!")
                self.add_kill(1)
                opponent.add_deaths(1)
            else:
                print(f"{opponent.name} Wins!!")
                self.add_deaths(1)
                opponent.add_kills(1)
        else:
                print("Draw!")

    

#Class Team-
Class Team:

    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero) 
        return 0

    def view_all_heroes(self):
        for hero in self.heroes
    
    def fight (self, opponent):
        for hero in self.opponent:





    


















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

#testing take_damage
    # # hero = Hero("Grace Hopper", 200)
    # sheild = Armor("Shield", 50)
    # hero.add_armor(sheild)
    # hero.take_damage(50)
    # print(hero.current_health)

    #Testing is_Alive
    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())










