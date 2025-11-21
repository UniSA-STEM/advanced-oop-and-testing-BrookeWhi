class Schedule:
    def __init__(self):
        self.__tasks = []

    def add_task(self, task_name, time, staff, assigment):
        self.__tasks.append({
            "task": task_name,
            "time": time,
            "staff": staff.__str__(),
            "assignment": assigment.name
        })

    def print_schedule(self):
        print(f"{"- "*35}\n"
              f"{"Schedule":^70}\n"
              f"{"- "*35}\n"
              f"{"Task":<14}  {"Time":<10} {"Staff":<30} {"Assigment":<5}\n"
              f"{"- "*35}")
        for task in self.__tasks:
            print(f"{task['task']:<15} {task['time']:<10} {task['staff']:<30} {task['assignment']:<5}")
        print(f"{"- "*35}\n")

