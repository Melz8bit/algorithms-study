### Moore's Algorithm

"""
- Start with EDD order
- Track current time as you schedule tasks
- If a task will be late (current time + duration > deadline), drop the longest task seen so far
- Continue until all remaining tasks are on time
"""


def _get_task_deadline(task: dict) -> int:
    return task["deadline"]


def _edd(tasks: list) -> list:
    return sorted(tasks, key=_get_task_deadline)


def moore(tasks: list) -> list:
    current_time = 0
    edd_tasks = _edd(tasks)
    moore_tasks = []

    for task in edd_tasks:
        moore_tasks.append(task)

        if current_time + task["duration"] > task["deadline"]:
            max_dict = max(moore_tasks, key=lambda x: (x["duration"], x["deadline"]))
            moore_tasks.remove(max_dict)
            continue

        current_time += task["duration"]

    return moore_tasks


tasks = [
    {"name": "A", "duration": 3, "deadline": 6},
    {"name": "B", "duration": 2, "deadline": 3},
    {"name": "C", "duration": 1, "deadline": 4},
    {"name": "D", "duration": 4, "deadline": 8},
    {"name": "E", "duration": 2, "deadline": 5},
]

moore_tasks = moore(tasks)
print("Tasks")
for _ in moore_tasks:
    print(_)

# All tasks on time — nothing should be dropped
tasks2 = [
    {"name": "A", "duration": 1, "deadline": 1},
    {"name": "B", "duration": 1, "deadline": 2},
    {"name": "C", "duration": 1, "deadline": 3},
]
moore_tasks = moore(tasks2)
print("Tasks2")
for _ in moore_tasks:
    print(_)

# All tasks late — only shortest survives
tasks3 = [
    {"name": "A", "duration": 3, "deadline": 2},
    {"name": "B", "duration": 2, "deadline": 2},
    {"name": "C", "duration": 1, "deadline": 2},
]
moore_tasks = moore(tasks3)
print("Tasks3")
for _ in moore_tasks:
    print(_)

# Tie in duration — one gets dropped
tasks4 = [
    {"name": "A", "duration": 2, "deadline": 2},
    {"name": "B", "duration": 2, "deadline": 3},
    {"name": "C", "duration": 2, "deadline": 4},
]

moore_tasks = moore(tasks4)
print("Tasks4")
for _ in moore_tasks:
    print(_)
