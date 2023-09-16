# Shashank Navale
# COP 3502C - Professor Zhou
# 27 July 2023
class Pakuri:
    def __init__(self, species):  # initializes the Pakuri class with attributes
        self.species = species
        self.attack = (len(species) * 7) + 9
        self.defense = (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13

    def get_species(self):    # getter function for species name
        return self.species

    def get_attack(self):  # getter function for pakuri's attack value
        return self.attack

    def get_defense(self):  # getter function for pakuri's defense value
        return self.defense

    def get_speed(self):  # getter function for pakuri's speed value
        return self.speed

    def set_attack(self, new_attack):   # setter function to update attack
        self.attack = new_attack

    def evolve(self):  # evolves (upgrades) the pakuri's attack, defense and speed
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3
