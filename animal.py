'''
File: animal.py
Description: Animal Class Module
Author: Brooke Whitmore
ID: 110468647
Username: WHIBY031
This is my own work as defined by the University's Academic Integrity Policy.
'''
from healthissues import HealthIssues
class Animal:
    """
    Class for Animal attributes and functions
    Contains methods for initialising animal, animal actions and reporting on status
    Attributes:
        - name: Name of the animal
        - species: Species of the animal
        - age: Age of the animal
        - diet: Diet of the animal
        - under_treatment: Whether the animal is under treatment
        - health_status: Health status of the animal
        - health_issues: Health issues of the animal
    """
    def __init__(self, name, species, age, diet):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet
        self.__under_treatment = False
        self.__health_issues = []
        self.__health_status = "Healthy"

    def __str__(self):
        """
        Compiles a string representation of the animal descriptors and status
        :return: (str)
        """
        print(">>> Animal Details <<<")
        print("- " * 35)
        print(f" Name: {self.__name} \n"
              f" Species: {self.__species} \n"
              f" Age: {self.__age} \n"
              f" Diet: {self.__diet}\n"
              f" Under-treatment: {self.__under_treatment} \n"
              f" Health Status: {self.__health_status} \n"
              f" Health Issues:")
        if not self.__health_issues:
            print(" None")
        else:
            for i in self.__health_issues:
                print("\n  - Health Issue:")
                for k, v in i.items():
                    print(f"    {k}: {v}")
        print("- "*35)


    @property
    def name(self):
        return self.__name

    @property
    def health_status(self):
        return self.__health_status

    @property
    def under_treatment(self):
        return self.__under_treatment

    @property
    def type(self):
        return self.__species

    @property
    def info(self):
        return f"{self.__name}, the {self.__species}"

    @property
    def eating(self):
        return f"{self.info} is eating {self.__diet}"

    def health_check(self):
        """
        Checks health status, updates information and prints status
        :return: (str)
        """
        # Check if animal has any health issues adjust status accordingly
        if not self.__health_issues:
            self.__health_status = "Healthy"
        else:
            self.__health_status = "Unwell"
        # Print statement depending on status
        if self.__health_status == "Healthy":
            print(f"{self.__name} is healthy")
        else:
            print(f"{self.__name} is suffering from health issues")
            self.__str__()
            if self.__under_treatment:
                print(f"{self.__name} is being treated")
            else:
                print(f"{self.__name} has no treatment plan")



    def sleeping(self):
        """
        Print status of sleeping
        :return:
        """
        return f"{self.info} is sleeping"

    def feed(self):
        """
        Print status of feeding
        :return: print statement
        """
        print (f"Currently feeding {self.info} \n"
               f"{self.eating}")

    def add_to_health_record(self, description, date_reported, severity, treatment_plan = None, notes = None):
        """
        Adds health issue to health record
        :param description:
        :param date_reported:
        :param severity:
        :param treatment_plan:
        :param notes:
        :return: (Class, boolean)
        """
        issue = HealthIssues(description, date_reported, severity, treatment_plan, notes)
        # Add health issue to animals list of health issues
        self.__health_issues.append(issue.report())
        if treatment_plan:
            self.__under_treatment = True
        else:
            self.__under_treatment = False


class Mammal(Animal):
    """
    Mammal child class
    Inherits from Animal class and adds methods and attribute
    Attributes:
        - name
        - species
        - age
        - diet
        - category
    """
    def __init__(self, name, species, age, diet):
        Animal.__init__(self, name, species, age, diet)
        self.__category = "Mammal"

    def make_sound(self):
        """
        Makes sound
        :return:
        """
        return f"{self.info} grunts"

    @property
    def category(self):
        return "Mammal"

class Bird(Animal):
    """
    Bird child class
    Inherits from Animal class and adds methods and attribute
    Attributes:
        - name
        - species
        - age
        - diet
        - category
    """
    def __init__(self, name, species, age, diet):
        Animal.__init__(self, name, species, age, diet)
        self.__category = "Bird"

    def make_sound(self):
        """
        Makes sound
        :return:
        """
        return f"{self.info} chirps"

    @property
    def category(self):
        return "Bird"

class Reptile(Animal):
    """
    Reptile child class
    Inherits from Animal class and adds methods and attribute
    Attributes:
        - name
        - species
        - age
        - diet
        - category
    """
    def __init__(self, name, species, age, diet):
        Animal.__init__(self, name, species, age, diet)
        self.__category = "Reptile"

    def make_sound(self):
        """
        Makes sound
        :return:
        """
        return f"{self.info} hisses"

    @property
    def category(self):
        return "Reptile"

