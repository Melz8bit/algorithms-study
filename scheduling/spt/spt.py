### Shortest Processing Time


def get_task_duration(task: dict) -> int:
    return task["duration"]


def spt(tasks: list) -> list:
    return sorted(tasks, key=get_task_duration)


tasks = [
    {"name": "A", "duration": 3, "deadline": 6},
    {"name": "B", "duration": 2, "deadline": 3},
    {"name": "C", "duration": 1, "deadline": 4},
    {"name": "D", "duration": 4, "deadline": 8},
    {"name": "E", "duration": 2, "deadline": 5},
]

scheduled_tasks = spt(tasks)
for task in scheduled_tasks:
    print(task)
