'''
File: staff.py
Description: Staff Class Module
Author: Brooke Whitmore
ID: 110468647
Username: WHIBY031
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Staff:
    def __init__(self, name):
        self.name = name



class Zookeeper(Staff):
    def __str__(self):
        return f"{self.name} - Zookeeper"

    def clean_enclosure(self, enclosure):
        enclosure.clean()

    def feed_animal(self, animal):
        animal.feed()

class Veterinarian(Staff):
    def __str__(self):
        return f"{self.name} - Veterinarian"
    def get_name(self):
        return self.name

    def checkup(self, animal):
        print(f"{self.name} conducting checkup on {animal.name}")
        animal.health_check()

