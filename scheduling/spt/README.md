# Shortest Processing Time (SPT) Scheduler

A Python implementation of the Shortest Processing Time scheduling algorithm — a greedy algorithm that minimizes the number of tasks in the queue by always completing the quickest task first.

---

## Background

Built as part of a self-directed study curriculum covering algorithms and data structures. SPT optimizes for throughput and responsiveness rather than deadline adherence.

**Topics covered in this implementation:**
- Greedy scheduling strategy
- Minimizing average completion time
- Throughput vs deadline trade-offs
- O(n log n) complexity

---

## How It Works

Sort all tasks by duration in ascending order. The shortest task is always scheduled first.

```
Input:  A(dur=3), B(dur=2), C(dur=1), D(dur=4), E(dur=2)
Output: C(dur=1), B(dur=2), E(dur=2), A(dur=3), D(dur=4)
```

### Why it minimizes average wait time

Each task completed removes an item from the queue. Completing short tasks first keeps the queue short for the longest time, minimizing the average time any task spends waiting.

---

## Complexity

| | Complexity |
|--|--|
| Time | O(n log n) — sorting by duration |
| Space | O(n) — returns a new sorted list |

---

## Implementation

```python
def _get_task_duration(task: dict) -> int:
    return task["duration"]


def spt(tasks: list) -> list:
    return sorted(tasks, key=_get_task_duration)
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

scheduled = spt(tasks)
for task in scheduled:
    print(task)
# C, B, E, A, D
```

---

## Comparison with EDD

| | EDD | SPT |
|--|-----|-----|
| Sorts by | Deadline | Duration |
| Optimizes for | Minimizing lateness | Minimizing queue length |
| Ignores | Task duration | Task deadline |
| Best when | Deadlines matter | Throughput matters |

---

## When to use SPT

- Deadlines are not a concern
- Goal is to maximize throughput and keep the queue short
- Tasks feel roughly equally important

## Limitations

- Ignores deadlines entirely — a critical urgent task may be scheduled last
- Use EDD when deadlines matter, or Moore's Algorithm when minimizing late tasks is the goal

---

## Study Context

Built while reading *Algorithms to Live By* by Brian Christian and Tom Griffiths (Chapter 5 — Scheduling).
