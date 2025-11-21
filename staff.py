'''
File: staff.py
Description: Staff Class Module
Author: Brooke Whitmore
ID: 110468647
Username: WHIBY031
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Staff:
    def __init__(self, name, role = None):
        self.__name = name
        self.__role = role

    @property
    def name(self):
        return self.__name


class Zookeeper(Staff):
    def __init__(self, name):
        super().__init__(name)
        self.__role = "Zookeeper"

    def __str__(self):
        return f"{self.name} - Zookeeper"

    @property
    def role(self):
        return self.__role

    def clean_enclosure(self, enclosure):
        enclosure.clean()

    def feed_animal(self, animal):
        animal.feed()

class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name)
        self.__role = "Veterinarian"

    @property
    def role(self):
        return self.__role

    def __str__(self):
        return f"{self.name} - Veterinarian"


    def checkup(self, animal):
        print(f"{self.name} conducting checkup on {animal.name}")
        animal.health_check()

