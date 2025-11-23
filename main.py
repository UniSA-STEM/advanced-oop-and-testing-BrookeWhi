'''
File: main.py
Description: Main Module
Author: Brooke Whitmore
ID: 110468647
Username: WHIBY031
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Mammal, Reptile, Bird
from management import Management
from enclosure import Enclosure
from schedule import Schedule
from staff import Zookeeper, Veterinarian

animal_environments = {
    "Silverback Gorilla": "Forest",
    "Tiger Snake": "Tropic",
    "Brown Snake": "Tropic",
    "Emperor Penguin": "Antarctic",
    "Humpback Whale": "Aquatic"
}

a_gorilla = Mammal("Alpha", "Silverback Gorilla", "16", "Vegetables")
b_gorilla = Mammal("Bravo", "Silverback Gorilla", "9", "Vegetables")
c_snake = Reptile("Charlie", "Tiger Snake", "11", "Rodents")
d_snake = Reptile("Delta", "Brown Snake", "4", "Rodents")
e_penguin = Bird("Echo", "Emperor Penguin", "8", "Fish")
f_whale = Mammal("Foxtrot", "Humpback Whale", "21", "Fish")
g_platypus = Mammal("Golf", "Platypus", "6", "Fish")

antarctic_enclosure = Enclosure("20m2", "Antarctic", "Bird")
tropic_enclosure = Enclosure("10m2", "Tropic", "Reptile")
forest_enclosure = Enclosure("50m2", "Forest", "Mammal")
aquatic_enclosure = Enclosure("80m2", "Aquatic", "Mammal")

animals = [a_gorilla, b_gorilla, c_snake, d_snake, e_penguin, f_whale]
enclosures = [antarctic_enclosure, tropic_enclosure, forest_enclosure, aquatic_enclosure]
keeper = Zookeeper("Zulu")
vet = Veterinarian("Victor")
zoo = Management()

def form_zoo():
    """
    Creating the zoo and adding animals and enclosures
    """

    for animal in animals:
        zoo.add_animal(animal)

    for enclosure in enclosures:
        zoo.add_enclosure(enclosure)

    zoo.add_animal_to_enclosure(a_gorilla, forest_enclosure)
    zoo.add_animal_to_enclosure(b_gorilla, forest_enclosure)
    zoo.add_animal_to_enclosure(c_snake, tropic_enclosure)
    zoo.add_animal_to_enclosure(d_snake, tropic_enclosure)
    zoo.add_animal_to_enclosure(e_penguin, antarctic_enclosure)
    zoo.add_animal_to_enclosure(f_whale, aquatic_enclosure)


    zoo.hire_staff(keeper)
    zoo.hire_staff(vet)
    zoo.reports("animals")
    zoo.reports("enclosures")
    zoo.remove_animal_from_enclosure(d_snake, tropic_enclosure)
    zoo.remove_animal(d_snake)
    zoo.reports("animals")


print("-"*70)
print("Running: form_zoo()")
print("-"*70)
form_zoo()


def day_schedule():
    """
    Scheduling tasks

    """
    day1 = Schedule()
    day1.add_task("Feeding", "9.00", keeper, a_gorilla)
    day1.add_task("Checkup", "9.00", vet, a_gorilla)
    day1.add_task("Feeding", "9.30", keeper, b_gorilla)
    day1.add_task("Checkup", "9.30", vet, e_penguin)
    day1.add_task("Clean", "10.00", keeper, forest_enclosure)
    day1.add_task("Clean", "10.30", keeper, tropic_enclosure)
    day1.print_schedule()


print("-"*70)
print("Running: day_schedule()")
print("-"*70)
day_schedule()


def staff_action():
    """
    Staff actioning tasks
    + Example of health reports

    """
    keeper.feed_animal(a_gorilla)
    vet.checkup(a_gorilla)
    keeper.feed_animal(b_gorilla)
    e_penguin.add_to_health_record("Skin Infection", "11-02-1982", "Moderate")
    c_snake.add_to_health_record("Infection", "01-03-1982", "Severe", "Fluid Therapy")
    vet.checkup(e_penguin)
    a_gorilla.__str__()
    keeper.clean_enclosure(forest_enclosure)
    keeper.clean_enclosure(tropic_enclosure)


print("-"*70)
print("Running: staff_action()")
print("-"*70)
staff_action()


def animal_action():
    """
    Different animal basic actions

    """
    b_gorilla.make_sound()
    c_snake.make_sound()
    f_whale.sleeping()
    e_penguin.sleeping()


print("-"*70)
print("Running: animal_action()")
print("-"*70)
animal_action()

def reporting():
    """
    Zoo reports

    """
    zoo.reports()
    zoo.reports("animals")
    zoo.reports("staff")

print("-"*70)
print("Running: reporting()")
print("-"*70)
reporting()

def health_reports():
    """
    Animal health reports
    :return:
    """
    zoo.health_reports()
    zoo.health_reports(a_gorilla)

print("-"*70)
print("Running: health_reports()")
print("-"*70)
health_reports()

def incorrect_attempts():
    """
    Functions that are unable to be completed when validating
    :return:
    """
    zoo.remove_animal_from_enclosure(c_snake, tropic_enclosure)
    zoo.remove_animal_from_enclosure(c_snake, forest_enclosure)
    zoo.add_animal_to_enclosure(c_snake, aquatic_enclosure)
    zoo.add_animal_to_enclosure(g_platypus, tropic_enclosure)

print("-"*70)
print("Running: incorrect_attempts()")
print("-"*70)
incorrect_attempts()

