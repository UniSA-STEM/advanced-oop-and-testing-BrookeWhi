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

    def reports(self):


    def add_animal(self, animal):
        self.__animals.append(animal)

    def add_enclosure(self, enclosure):
        self.__enclosures.append(enclosure)

    def add_staff(self, staff):
        self.__staff.append(staff)

    def add_animal_to_enclosure(self, animal, enclosure):
        enclosure.add_animal(animal)

    def remove_animal_from_enclosure(self, animal, enclosure):
        enclosure.remove_animal(animal)

    def hire_staff(self, staff):
        self.__staff.append(staff)

    def remove_staff(self, staff):
        self.__staff.remove(staff)




