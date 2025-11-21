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
        self.__cleanliness_status = "Clean"

    @property
    def animal_type(self):
        return self.__animal_type
    @property
    def environment_type(self):
        return self.__environment_type

    @property
    def name(self):
        return f"{self.__animal_type} Enclosure"

    def __str__(self):
        if not self.__animals:
            return f"Vacant {self.__environment_type} enclosure"
        else:
            animals = '\n'.join([str(animal.info) for animal in self.__animals])
            return (f"{self.__animal_type} Enclosure \n"
                f"-----------------------\n"
                f" Cleanliness Level: {self.__cleanliness_level}\n"
                f" Animals: \n{animals}\n"
                )

    def add_animal(self, animal):
        if animal.category == self.__animal_type:
            self.__animals.append(animal)
            print(f"{animal.name} added to {self.__animal_type} Enclosure")
            self.reduce_cleanliness()
        else:
            print("Cannot add animal to this type of enclosure")

    def remove_animal(self, animal):
        if animal in self.__animals:
            if animal.health_status:
                print(f"{animal.name} under treatment and cannot be removed from {self.__animal_type} Enclosure")
            else:
                self.__animals.remove(animal)
                print(f"{animal.name} removed from {self.__animal_type} Enclosure")
        else:
            print("Animal not in enclosure")

    def reduce_cleanliness(self):
        self.__cleanliness_level += -10
        if self.__cleanliness_level < 100:
            self.__cleanliness_status = "Dirty"
        elif self.__cleanliness_level < 50:
            self.__cleanliness_status = "Filthy"

    def clean(self):
        if self.__cleanliness_status == "Clean":
            print("Already clean")
        else:
            self.__cleanliness_status = "Clean"
            self.__cleanliness_level = 100
            print(f"{self.__animal_type} Enclosure has been cleaned")

