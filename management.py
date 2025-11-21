'''
File: management.py
Description: Management Class Module
Author: Brooke Whitmore
ID: 110468647
Username: WHIBY031
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Management:
    def __init__(self):
        self.__animals = []
        self.__enclosures = []
        self.__staff = []

    def reports(self, report_filter):
        print("--------------------")
        if report_filter == "animals":
            print(f" Animals \n")
            for animal in self.__animals:
                print(f" - {animal.name}, {animal.type} \n")
        elif report_filter == "enclosures":
            print(f" Enclosures \n")
            for enclosure in self.__enclosures:
                print(f" - {enclosure.__str__()}")
        elif report_filter == "staff":
            print(f" Staff \n")
            for staff in self.__staff:
                print(f" - {staff.name}, {staff.role} \n")


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
        enclosure.add_animal(animal)
        print(f"{animal.name}, {animal.type} added to {enclosure.__str__()}")

    def remove_animal_from_enclosure(self, animal, enclosure):
        enclosure.remove_animal(animal)
        print(f"{animal.name}, {animal.type} removed from {enclosure.__str__()}")

    def hire_staff(self, staff):
        self.__staff.append(staff)
        print(f"{staff.name}, {staff.role} added to staff list")

    def remove_staff(self, staff):
        self.__staff.remove(staff)
        print(f"{staff.name}, {staff.role} removed from staff list")




