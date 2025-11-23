'''
File: enclosure.py
Description: Enclosure Class Module
Author: Brooke Whitmore
ID: 110468647
Username: WHIBY031
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:
    """
    Enclosure Class
    Initialises enclosure and contains methods to add and remove animals and adjust cleanliness
    Attributes:
        - size
        - environment_type
        - animals
        - animal_type
        - cleanliness_level
        - cleanliness_status
    """
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

    @property
    def cleanliness_status(self):
        return self.__cleanliness_status

    @property
    def animals(self):
        return self.__animals


    def __str__(self):
        """
        Displays enclosure information
        :return:
        """
        # Check if any animals in enclosure and print accordingly
        if not self.__animals:
            return f"Vacant {self.__environment_type} enclosure\n"
        else:
            # Join animals in list of animals base info into string
            animals = '\n'.join([str(animal.info) for animal in self.__animals])
            return (f"{self.__animal_type} Enclosure \n"
                f"{" ":<3}Cleanliness Level: {self.__cleanliness_level}\n"
                f"{" ":<3}Animals: \n"
                f"{" ":<3}{animals}\n"
                )

    def add_animal(self, animal):
        """
        Adds an animal to the enclosure and reduces cleanliness upon doing so
        :param animal:
        :return:
        """
        # Check animal type matches enclosure
        if animal.category == self.__animal_type:
            self.__animals.append(animal)
            print(f"{animal.name} ({animal.type}) added to {self.__environment_type} Enclosure")
            # Reduce cleanliness of enclosure
            self.reduce_cleanliness()
        else:
            print("Cannot add animal to this type of enclosure")

    def remove_animal(self, animal):
        """
        Removes an animal from the enclosure
        :param animal:
        :return:
        """
        # Check animal in animals list
        if animal in self.__animals:
            # Check if under treatment
            if animal.under_treatment == True:
                print(f"{animal.name} ({animal.type}) under treatment and cannot be removed from {self.__animal_type} Enclosure")
            else:
                self.__animals.remove(animal)
                print(f"{animal.name} ({animal.type}) removed from {self.__animal_type} Enclosure")
        else:
            print(f"{animal.name} ({animal.type}) is not in {self.__environment_type} enclosure")

    def reduce_cleanliness(self):
        """
        Reduces cleanliness of enclosure
        :return:
        """
        # Reduce cleanliness level by 10
        self.__cleanliness_level += -10
        # Determine cleanliness status from level
        if self.__cleanliness_level < 100:
            self.__cleanliness_status = "Dirty"
        elif self.__cleanliness_level < 50:
            self.__cleanliness_status = "Filthy"

    def clean(self):
        """
        Cleans enclosure
        :return:
        """
        # Check cleanliness status
        if self.__cleanliness_status == "Clean":
            print(f"{self.__animal_type} Enclosure does not need cleaning")
        else:
            # Update status and level to max
            self.__cleanliness_status = "Clean"
            self.__cleanliness_level = 100
            print(f"{self.__animal_type} Enclosure has been cleaned")

