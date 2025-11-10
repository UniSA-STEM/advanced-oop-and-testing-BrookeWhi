'''
File: enclosure.py
Description: Enclosure Class Module
Author: Brooke Whitmore
ID: 110468647
Username: WHIBY031
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:
    def __init__(self, size, environment_type, animal_type):
        self.__size = size
        self.__environment_type = environment_type
        self.__animals = []
        self.__animal_type = animal_type
        self.__cleanliness_level = 100

    def __str__(self):
        return (f"{self.__animal_type} Enclosure \n"
                f"-----------------------\n"
                f"Cleanliness Level: {self.__cleanliness_level}\n"
                f"Animals: {self.__animals}\n"
            )