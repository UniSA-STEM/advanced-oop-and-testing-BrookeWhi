'''
File: staff.py
Description: Staff Class Module
Author: Brooke Whitmore
ID: 110468647
Username: WHIBY031
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Staff:
    """
    Class for staff attributes and methods
    Attributes:
        - name
        - role
    """
    def __init__(self, name, role = None):
        self.__name = name
        self.__role = role

    @property
    def name(self):
        return self.__name


class Zookeeper(Staff):
    """
    Child class of staff for zookeeper methods
    Attributes:
        - name
        - role (Zookeeper)
    """
    def __init__(self, name):
        super().__init__(name)
        self.__role = "Zookeeper"

    def __str__(self):
        return f"{self.name} - Zookeeper"

    @property
    def role(self):
        return self.__role

    def clean_enclosure(self, enclosure):
        """
        Calls clean enclosure method on enclosure
        :param enclosure:
        :return:
        """
        enclosure.clean()

    def feed_animal(self, animal):
        """
        Calls feed animal method on animal
        :param animal:
        :return:
        """
        animal.feed()

class Veterinarian(Staff):
    """
    Child class of staff for veterinarian methods
    Attributes:
        - name
        - role (Veterinarian)
    """
    def __init__(self, name):
        super().__init__(name)
        self.__role = "Veterinarian"

    @property
    def role(self):
        return self.__role

    def __str__(self):
        return f"{self.name} - Veterinarian"


    def checkup(self, animal):
        """
        Calls checkup method on animal
        :param animal:
        :return:
        """
        print(f"{self.name} conducting checkup on {animal.name}")
        animal.health_check()

