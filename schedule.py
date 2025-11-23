'''
File: schedule.py
Description: Schedule Class Module
Author: Brooke Whitmore
ID: 110468647
Username: WHIBY031
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Schedule:
    """
    Schedule class
    Initialises schedule and contains methods to add tasks and display schedule
    Attributes:
        tasks (list): list of tasks
    """
    def __init__(self):
        self.__tasks = []

    def add_task(self, task_name, time, staff, assigment):
        """
        Add task to schedule
        :param task_name:
        :param time:
        :param staff:
        :param assigment:
        :return:
        """
        self.__tasks.append({
            "task": task_name,
            "time": time,
            "staff": staff.__str__(),
            "assignment": assigment.name
        })

    def print_schedule(self):
        """
        Displays formatted schedule
        :return:
        """
        print(f"{"- "*35}\n"
              f"{"Schedule":^70}\n"
              f"{"- "*35}\n"
              f"{"Task":<14}  {"Time":<10} {"Staff":<30} {"Assigment":<5}\n"
              f"{"- "*35}")
        for task in self.__tasks:
            print(f"{task['task']:<15} {task['time']:<10} {task['staff']:<30} {task['assignment']:<5}")
        print(f"{"- "*35}\n")

