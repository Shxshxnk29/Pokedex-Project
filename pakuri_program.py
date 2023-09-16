# Shashank Navale
# COP 3502C - Professor Zhou
# 27 July 2023

from pakudex import Pakudex  # imports pakudex class

print("Welcome to Pakudex: Tracker Extraordinaire!")

capacity = input("Enter max capacity of the Pakudex: ")

while not isinstance(capacity, int):  # ensures capacity is an integer
    try:
        if isinstance(capacity, str):  # if input is string, tries to convert to integer
            capacity = int(capacity)

        if capacity > 0:  # runs if capacity is positive
            print(f"The Pakudex can hold {capacity} species of Pakuri.")

        else:  # runs if capacity is negative
            print("Please enter a valid size.")
            capacity = input("Enter max capacity of the Pakudex: ")

    except ValueError:  # raises value error when non integers is inputted
        print("Please enter a valid size.")
        capacity = input("Enter max capacity of the Pakudex: ")



pakudex = Pakudex(capacity)  # creates a pakudex object with user inputted capacity

menu_option = 0  # initializes menu_option

while menu_option != 6:  # loops while menu_option is not 6

    print("\nPakudex Main Menu")
    print("-----------------")
    print("1. List Pakuri")
    print("2. Show Pakuri")
    print("3. Add Pakuri")
    print("4. Evolve Pakuri")
    print("5. Sort Pakuri")
    print("6. Exit")
    # prints necessary menu options

    try:
        menu_option = int(input("What would you like to do? "))

        if 1 <= menu_option <= 6:
            if menu_option == 1:  # list species option
                pakudex.get_species_array()
                #  gets the list of pakuris in pakudex

            if menu_option == 2:  # show species option
                species_stats = input("Enter the name of the species to display: ")
                pakudex.get_stats(species_stats)  # returns stats for the species the user asks for



            if menu_option == 3:  # add pakuri option
                if pakudex.size == capacity:
                    print("Error: Pakudex is full!\n")  # checks if pakudex is full

                else:
                    new_species = input("Enter the name of the species to add: ")
                    pakudex.add_pakuri(new_species)  # adds user inputted species to pakudex

            if menu_option == 4:  # evolve pakuri option
                evolving_species = input("Enter the name of the species to evolve: ")
                pakudex.evolve_species(evolving_species)  # evolves the user inputted species

            if menu_option == 5:  # sort option
                # sorts pakuri in pakudex
                pakudex.sort_pakuri()

            if menu_option == 6:  # runs if menu_option is 6, prints thank you message and exits out of program
                print("Thanks for using Pakudex! Bye!")


        else:  # runs if menu_option is negative or more than 6
            print("Unrecognized menu selection!")

    except ValueError:  # raises value error when non integer is inputted for menu_option
        print("Unrecognized menu selection!")
