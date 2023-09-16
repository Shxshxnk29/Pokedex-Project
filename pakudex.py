# Shashank Navale
# COP 3502C - Professor Zhou
# 27 July 2023

from pakuri import Pakuri  # imports Pakuri class


class Pakudex:
    def __init__(self, capacity=20):  # initializes Pakudex class with necessary instance attributes
        self.capacity = capacity
        self.pakuris = []
        self.pakuris_str = []
        self.size = 0  # keeps track of pakuris array size
        self.stats_arr = []

    def get_size(self):  # getter function for the size of the Pakudex
        return self.size

    def get_capacity(self):  # getter function for the capacity of the Pakudex
        return self.capacity

    def get_species_array(self):  # getter function for the list of species
        if self.size == 0:
            print("No Pakuri in Pakudex yet!")
            return None

        print("Pakuri In Pakudex:")
        index = 0
        for pakuri in self.pakuris_str:
            print(f"{index + 1}. {pakuri}")
            index += 1

        return self.pakuris_str

    def get_stats(self, species):  # getter function for the stats of each species
        if species not in self.pakuris_str:  # checks if species is not in Pakudex
            print("Error: No such Pakuri!")
            return None

        for pakuri in self.pakuris:
            if pakuri.get_species() == species:
                self.stats_arr.clear()  # resets the stats_array
                self.stats_arr.append(pakuri.get_attack())
                self.stats_arr.append(pakuri.get_defense())
                self.stats_arr.append(pakuri.get_speed())
                print(f"Species: {species}")
                print(f"Attack: {self.stats_arr[0]}")
                print(f"Defense: {self.stats_arr[1]}")
                print(f"Speed: {self.stats_arr[2]}")
                # appends and prints necessary stats
                return self.stats_arr  # returns the int array with stats

    def sort_pakuri(self):  # sorts the list of species alphabetically
        if self.size != 0:  # ensures the Pakudex is not empty
            self.pakuris_str.sort()
            print("Pakuri have been sorted!")
        else:
            return None

    def add_pakuri(self, species):  # adds pakuri to pakudex

        for pakuri in self.pakuris:
            if pakuri.get_species() == species:
                print("Error: Pakudex already contains this species!")
                return False  # returns false if pakuri already in pakudex

        if self.size < self.capacity:
            self.pakuris.append(Pakuri(species))
            self.pakuris_str.append(species)
            self.size += 1
            print(f"Pakuri species {species} successfully added!")
            return True  # returns true when new pakuri has been added the pakudex

        print("Error: Pakudex full")  # notifies that pakudex is full and returns false
        return False

    def evolve_species(self, species):  # evolves species specified
        for pakuri in self.pakuris:
            if pakuri.get_species() == species:
                pakuri.evolve()  # matches the inputted species and evolves it

                print(f"{species} has evolved!\n")
                return True

        print("Error: No such Pakuri!\n")  # notifies that pakuri is not in pakudex
        return False
