'''
File: healthissues.py
Description: Health Issues Class Module
Author: Brooke Whitmore
ID: 110468647
Username: WHIBY031
This is my own work as defined by the University's Academic Integrity Policy.
'''

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