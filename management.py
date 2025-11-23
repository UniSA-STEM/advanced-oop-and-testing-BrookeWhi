'''
File: management.py
Description: Management Class Module
Author: Brooke Whitmore
ID: 110468647
Username: WHIBY031
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal
from enclosure import Enclosure

animal_environments = {
    "Silverback Gorilla": "Forest",
    "Tiger Snake": "Tropic",
    "Brown Snake": "Tropic",
    "Emperor Penguin": "Antarctic",
    "Humpback Whale": "Aquatic"
}

class Management:
    """
    Management Class
    Initialises zoo as a whole, contains lists of animals, staff and enclosures and methods to interchange and report.
    Attributes:
        - animals (list): List of animals
        - enclosures (list): List of enclosures
        - staff (list): List of staff
    """
    def __init__(self):
        self.__animals = []
        self.__enclosures = []
        self.__staff = []

    def reports(self, report_filter = None):
        """
        Displays list of animals, enclosures and staff, all or specific
        :param report_filter:
        :return: print statement
        """
        # Print all animals in list
        if report_filter == "animals":
            print("Filtered Report - Animals")
            print("-" * 70)
            for animal in self.__animals:
                print(f" - {animal.name}, {animal.type} \n")
            print("-" * 70)
        # Print all enclosures in list
        elif report_filter == "enclosures":
            print("Filtered Report - Enclosures")
            print("-" * 70)
            for enclosure in self.__enclosures:
                print(f" - {enclosure.__str__()}")
            print("-" * 70)
        # Print all staff in list
        elif report_filter == "staff":
            print("Filtered Report - Staff")
            print("-" * 70)
            for staff in self.__staff:
                print(f" - {staff.name}, {staff.role} \n")
            print("-" * 70)
        # Print all in lists
        else:
            print("Overall Report")
            print("-" * 70)
            print(f" Animals \n")
            for animal in self.__animals:
                print(f" - {animal.name}, {animal.type} \n")
            print(f" Enclosures \n")
            for enclosure in self.__enclosures:
                print(f" - {enclosure.__str__()}")
            print(f" Staff \n")
            for staff in self.__staff:
                print(f" - {staff.name}, {staff.role} \n")
            print("-" * 70)

    def health_reports(self, animal = None):
        """
        Displays health report of animals, all or specific
        :param animal:
        :return:
        """
        # Print all animals health report in list
        if animal is None:
            print("All Animals Health Report")
            print("-" * 70)
            for animal in self.__animals:
                animal.__str__()
        # Print specified animal health report
        else:
            print(f"{animal.name}, {animal.type} Health Report")
            print("-" * 70)
            animal.__str__()


    def add_animal(self, animal):
        """
        Adds an animal to zoo list
        :param animal:
        :return:
        """
        self.__animals.append(animal)
        print(f"{animal.name}, {animal.type} added to animals list")

    def remove_animal(self, animal):
        """
        Removes an animal from zoo list
        :param animal:
        :return:
        """
        self.__animals.remove(animal)
        print(f"{animal.name}, {animal.type} removed from animals list")

    def add_enclosure(self, enclosure):
        """
        Adds an enclosure to zoo list
        :param enclosure:
        :return:
        """
        self.__enclosures.append(enclosure)
        print(f"{enclosure.__str__()} added to enclosures list")

    def remove_enclosure(self, enclosure):
        """
        Removes an enclosure from zoo list
        :param enclosure:
        :return:
        """
        self.__enclosures.remove(enclosure)
        print(f"{enclosure.__str__()} removed from enclosures list")

    def add_animal_to_enclosure(self, animal, enclosure):
        """
        Adds an animal to an enclosure within the zoo lists
        :param animal:
        :param enclosure:
        :return:
        """
        # Check animal within animals list
        if animal in self.__animals:
            # Get suitable environment for animal
            correct_environment = animal_environments.get(animal.type)
            # Check if environment suitable
            if correct_environment == enclosure.environment_type:
                # Add animal to enclosure
                enclosure.add_animal(animal)
            else:
                print(f"{animal.name} ({animal.type}) cannot be placed in {enclosure.environment_type} enclosure")
        else:
            print(f"{animal.name} ({animal.type}) not in animals list")

    def remove_animal_from_enclosure(self, animal, enclosure):
        """
        Removes an animal from an enclosure within the zoo lists
        :param animal:
        :param enclosure:
        :return:
        """
        enclosure.remove_animal(animal)


    def hire_staff(self, staff):
        """
        Adds staff to the staff list
        :param staff:
        :return:
        """
        self.__staff.append(staff)
        print(f"{staff.name}, {staff.role} added to staff list")

    def remove_staff(self, staff):
        """
        Removes staff from the staff list
        :param staff:
        :return:
        """
        self.__staff.remove(staff)
        print(f"{staff.name}, {staff.role} removed from staff list")




