'''
File: testing.py
Description: Testing Module
Author: Brooke Whitmore
ID: 110468647
Username: WHIBY031
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Bird, Mammal, Reptile
from enclosure import Enclosure
from healthissues import HealthIssues
from management import Management
from staff import Veterinarian, Zookeeper, Staff
from schedule import Schedule


def test_initialisation():
    animal = Bird("Gerald", "Emperor Penguin", 8, "Fish")
    assert animal.name == "Gerald"
    assert animal.type == "Emperor Penguin"
    assert animal.under_treatment is False

def test_animal_functions():
    animal = Bird("Gerald", "Emperor Penguin", 8, "Fish")
    mammal = Mammal("Dogbert", "Lion", 9, "Red Meat")
    assert animal.make_sound() == "Gerald, the Emperor Penguin chirps"
    assert animal.sleeping() == "Gerald, the Emperor Penguin is sleeping"
    assert mammal.make_sound() == "Dogbert, the Lion grunts"

def test_health_check_healthy():
    penguin = Bird("Gerald", "Emperor Penguin", 8, "Fish")
    penguin.health_check()
    assert penguin.health_status == "Healthy"

def test_health_check_unwell():
    penguin = Bird("Gerald", "Emperor Penguin", 8, "Fish")
    penguin.add_to_health_record("Disease", "11-03-1989", "Mild", "Medication")
    penguin.health_check()
    assert penguin.health_status == "Unwell"
    assert penguin.under_treatment is True

def test_enclosure_initialisation():
    enclosure = Enclosure("20m2", "Tropic", "Reptile")
    assert enclosure.cleanliness_status == "Clean"
    assert enclosure.environment_type == "Tropic"

def test_enclosure_methods():
    enclosure = Enclosure("20m2", "Tropic", "Reptile")
    reptile = Reptile("Ethyl", "Tiger Snake", 3, "Rodents")
    enclosure.add_animal(reptile)
    assert enclosure.animals == [reptile]

def test_staff_initialisation():
    staff = Zookeeper("Jamos")
    assert staff.name == "Jamos"
    assert staff.role == "Zookeeper"

def test_staff_methods():
    staff = Zookeeper("Jamos")
    enclosure = Enclosure("20m2", "Tropic", "Reptile")
    enclosure.reduce_cleanliness()
    assert enclosure.cleanliness_status == "Dirty"
    staff.clean_enclosure(enclosure)
    assert enclosure.cleanliness_status == "Clean"

def test_health_issues():
    issue = HealthIssues("Sickness", "15-10-1380", "Moderate", None, "Notes")
    report = issue.report()
    assert report["Description"] == "Sickness"
    assert report["DateReported"] == "15-10-1380"
    assert report["Severity"] == "Moderate"
    assert report["TreatmentPlan"] is None
    assert report["Notes"] == "Notes"

def test_zoo_initialisation():
    zoo = Management()
    assert zoo._Management__animals == []
    assert zoo._Management__enclosures == []
    assert zoo._Management__staff == []

def test_zoo_animal_methods():
    zoo = Management()
    animal = Bird("Gerald", "Emperor Penguin", 8, "Fish")
    zoo.add_animal(animal)
    assert animal in zoo._Management__animals
    zoo.remove_animal(animal)
    assert animal not in zoo._Management__animals

def test_zoo_enclosure_methods():
    zoo = Management()
    enclosure = Enclosure("20m2", "Tropic", "Reptile")
    zoo.add_enclosure(enclosure)
    assert enclosure in zoo._Management__enclosures
    zoo.remove_enclosure(enclosure)
    assert enclosure not in zoo._Management__enclosures

def test_add_task():
    schedule = Schedule()
    staff = Zookeeper("Alice")
    animal = Bird("Gerald", "Emperor Penguin", 8, "Fish")
    schedule.add_task("Feed Penguins", "09:00", staff, animal)
    tasks = schedule._Schedule__tasks
    assert tasks[0]["task"] == "Feed Penguins"
    assert tasks[0]["time"] == "09:00"
    assert tasks[0]["staff"] == "Alice - Zookeeper"
    assert tasks[0]["assignment"] == "Gerald"