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
        self.__under_treatment = False
        self.__health_issues = []
        self.__health_status = "Healthy"

    def __str__(self):

        print(f"- - - - - - - - - - - -\n"
              f">>>> Health Record <<<<\n"
              f"- - - - - - - - - - - -\n"
              f" Name: {self.__name} \n"
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
        print("- - - - - - - - - - -")
    @property
    def name(self):
        return self.__name

    def health_check(self):
        if not self.__health_issues:
            self.__health_status = "Healthy"
        else:
            self.__health_status = "Unwell"

        if self.__health_status == "Healthy":
            print(f"{self.__name} is healthy")
        else:
            print(f"{self.__name} is suffering from health issues")
            print(self.__str__())
            if self.__under_treatment:
                print(f"{self.__name} is being treated")
            else:
                print(f"{self.__name} has no treatment plan")

    def eating(self):
        return f"{self.__name} is eating {self.__diet}"

    def sleeping(self):
        return f"{self.__name} is sleeping"

    def feed(self):
        print (f"Currently feeding {self.__name} the {self.__species} \n"
               f"{self.eating()}")

    def add_to_health_record(self, description, date_reported, severity, treatment_plan = None, notes = None):
        issue = HealthIssues(description, date_reported, severity, treatment_plan, notes)
        self.__health_issues.append(issue.report())
        if treatment_plan:
            self.__under_treatment = True
        else:
            self.__under_treatment = False


class Mammal(Animal):
    def __init__(self, name, species, age, diet):
        Animal.__init__(self, name, species, age, diet)
        self.__category = "Mammal"

    def type(self):
        return self.__category

    def make_sound(self):
        return f"{self.__name} grunts"

class Bird(Animal):
    def __init__(self, name, species, age, diet):
        Animal.__init__(self, name, species, age, diet)
        self.__category = "Bird"

    def type(self):
        return self.__category

    def make_sound(self):
        return f"{self.__name} chirps"

class Reptile(Animal):
    def __init__(self, name, species, age, diet):
        Animal.__init__(self, name, species, age, diet)
        self.__category = "Reptile"

    def type(self):
        return self.__category

    def make_sound(self):
        return f"{self.__name} hisses"

class HealthIssues:
    def __init__(self, description, date_reported, severity, treatment_plan = None, notes = None):
        self.__description = description
        self.__date_reported = date_reported
        self.__severity = severity
        self.__treatment_plan = treatment_plan
        self.__notes = notes

    def report(self):
        return ({"Description": self.__description,
                "DateReported": self.__date_reported,
                "Severity": self.__severity,
                "TreatmentPlan": self.__treatment_plan,
                "Notes": self.__notes})