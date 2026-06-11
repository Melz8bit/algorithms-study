# Earliest Due Date (EDD) Scheduler

A Python implementation of the Earliest Due Date scheduling algorithm — a greedy algorithm that minimizes lateness by scheduling tasks in order of their deadlines.

---

## Background

Built as part of a self-directed study curriculum covering algorithms and data structures. EDD is the foundation for more complex scheduling algorithms like Moore's Algorithm, which builds directly on top of it.

**Topics covered in this implementation:**
- Greedy scheduling strategy
- Minimizing maximum lateness
- Sorting as a scheduling tool
- O(n log n) complexity

---

## How It Works

Sort all tasks by deadline in ascending order. The task with the earliest deadline is always scheduled first.

```
Input:  A(d=6), B(d=3), C(d=4), D(d=8), E(d=5)
Output: B(d=3), C(d=4), E(d=5), A(d=6), D(d=8)
```

### Why it minimizes lateness

If any task is going to be late, doing the earliest-deadline task first minimizes how late the latest task will be across the entire schedule. Swapping any two adjacent tasks in any other order can only make things worse.

---

## Complexity

| | Complexity |
|--|--|
| Time | O(n log n) — sorting by deadline |
| Space | O(n) — returns a new sorted list |

---

## Implementation

```python
def _get_task_deadline(task: dict) -> int:
    return task["deadline"]


def edd(tasks: list) -> list:
    return sorted(tasks, key=_get_task_deadline)
```

---

## Usage

```python
tasks = [
    {"name": "A", "duration": 3, "deadline": 6},
    {"name": "B", "duration": 2, "deadline": 3},
    {"name": "C", "duration": 1, "deadline": 4},
    {"name": "D", "duration": 4, "deadline": 8},
    {"name": "E", "duration": 2, "deadline": 5},
]

scheduled = edd(tasks)
for task in scheduled:
    print(task)
# B, C, E, A, D
```

---

## When to use EDD

- All tasks must be completed — you can't drop any
- Goal is to minimize how late the latest task finishes
- Tasks have fixed deadlines but no priority weights

## Limitations

- Does not account for task importance or priority weights
- Does not drop late tasks — use Moore's Algorithm if minimizing the *number* of late tasks is the goal

---

## Study Context

Built while reading *Algorithms to Live By* by Brian Christian and Tom Griffiths (Chapter 5 — Scheduling).
