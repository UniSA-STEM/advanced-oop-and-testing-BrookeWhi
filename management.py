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
    def __init__(self):
        self.__animals = []
        self.__enclosures = []
        self.__staff = []

    def reports(self, report_filter = None):
        if report_filter == "animals":
            print("Filtered Report - Animals")
            print("-" * 70)
            for animal in self.__animals:
                print(f" - {animal.name}, {animal.type} \n")
            print("-" * 70)
        elif report_filter == "enclosures":
            print("Filtered Report - Enclosures")
            print("-" * 70)
            for enclosure in self.__enclosures:
                print(f" - {enclosure.__str__()}")
            print("-" * 70)
        elif report_filter == "staff":
            print("Filtered Report - Staff")
            print("-" * 70)
            for staff in self.__staff:
                print(f" - {staff.name}, {staff.role} \n")
            print("-" * 70)
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
        if animal is None:
            print("All Animals Health Report")
            print("-" * 70)
            for animal in self.__animals:
                animal.__str__()
        else:
            print(f"{animal.name}, {animal.type} Health Report")
            print("-" * 70)
            animal.__str__()


    def add_animal(self, animal):
        self.__animals.append(animal)
        print(f"{animal.name}, {animal.type} added to animals list")

    def remove_animal(self, animal):
        self.__animals.remove(animal)
        print(f"{animal.name}, {animal.type} removed from animals list")

    def add_enclosure(self, enclosure):
        self.__enclosures.append(enclosure)
        print(f"{enclosure.__str__()} added to enclosures list")

    def remove_enclosure(self, enclosure):
        self.__enclosures.remove(enclosure)
        print(f"{enclosure.__str__()} removed from enclosures list")

    def add_animal_to_enclosure(self, animal, enclosure):
        correct_environment = animal_environments.get(animal.type)
        if correct_environment == enclosure.environment_type:
                enclosure.add_animal(animal)
        else:
            print(f"{animal.name} ({animal.type}) cannot be placed in {enclosure.environment_type} enclosure")


    def remove_animal_from_enclosure(self, animal, enclosure):
        enclosure.remove_animal(animal)
        print(f"{animal.name}, {animal.type} removed from {enclosure.environment_type} enclosure")

    def hire_staff(self, staff):
        self.__staff.append(staff)
        print(f"{staff.name}, {staff.role} added to staff list")

    def remove_staff(self, staff):
        self.__staff.remove(staff)
        print(f"{staff.name}, {staff.role} removed from staff list")




