'''
File: animal.py
Description: Animal Class Module
Author: Brooke Whitmore
ID: 110468647
Username: WHIBY031
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Animal:
    def __init__(self, name, species, age, diet):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet
        self.__health_issues = []
        self.__under_treatment = False
        self.__health_status = "Healthy"

    def __str__(self):
        return (f"Animal Information \n"
                f"---------------------\n"
                f"Name: {self.__name} \n"
                f"Species: {self.__species} \n"
                f"Age: {self.__age} \n"
                f"Diet: {self.__diet} \n")

class Mammal(Animal):
    def __init__(self, name, species, age, diet):
        Animal.__init__(self, name, species, age, diet)
        self.__category = "Mammal"

class Bird(Animal):
    def __init__(self, name, species, age, diet):
        Animal.__init__(self, name, species, age, diet)
        self.__category = "Bird"

class Reptile(Animal):
    def __init__(self, name, species, age, diet):
        Animal.__init__(self, name, species, age, diet)
        self.__category = "Reptile"


# TODO:
#     - add functions
#         > making sounds
#         > eating
#         > sleeping
#     - health record - (functionality)
