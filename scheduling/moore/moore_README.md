# Moore's Algorithm

A Python implementation of Moore's Algorithm — a scheduling algorithm that minimizes the number of late tasks by selectively dropping the most time-consuming task whenever a deadline would be missed.

---

## Background

Built as part of a self-directed study curriculum covering algorithms and data structures. Moore's Algorithm builds directly on top of EDD and introduces the concept of deliberate task elimination as a scheduling strategy.

**Topics covered in this implementation:**
- Greedy scheduling with elimination
- Minimizing number of late tasks
- Building on EDD as a foundation
- Trade-off between completeness and timeliness
- O(n log n) complexity

---

## How It Works

1. Sort tasks by deadline (EDD order)
2. Process tasks one at a time, tracking current time
3. If adding a task would cause it to be late, drop the longest task seen so far
4. Continue until all remaining tasks are on schedule

```
EDD order: B(d=3), C(d=4), E(d=5), A(d=6), D(d=8)

t=0:  Add B (dur=2) → t=2, deadline=3 ✅
t=2:  Add C (dur=1) → t=3, deadline=4 ✅
t=3:  Add E (dur=2) → t=5, deadline=5 ✅
t=5:  Add A (dur=3) → t=8 > deadline=6 ❌ → drop longest (A, dur=3), t stays at 5
t=5:  Add D (dur=4) → t=9 > deadline=8 ❌ → drop longest (D, dur=4), t stays at 5

Result: B, C, E
```

### The key insight

When a deadline is missed, dropping the longest task frees the most time for subsequent tasks. The dropped task was going to be late anyway — better to sacrifice one large task than let it cause a cascade of late completions.

---

## Complexity

| | Complexity |
|--|--|
| Time | O(n log n) — EDD sort + max search per task |
| Space | O(n) — stores scheduled tasks |

---

## Implementation

```python
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
```

### Tie-breaking

When two tasks have equal duration, the one with the later deadline is dropped. This preserves the more urgent task and is encoded in the sort key `(duration, deadline)`.

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

scheduled = moore(tasks)
for task in scheduled:
    print(task)
# B, C, E  (A and D dropped)
```

---

## Test Cases

```python
# All on time — nothing dropped
tasks2 = [{"name": "A", "duration": 1, "deadline": 1},
          {"name": "B", "duration": 1, "deadline": 2},
          {"name": "C", "duration": 1, "deadline": 3}]
# → A, B, C

# All late — only shortest survives
tasks3 = [{"name": "A", "duration": 3, "deadline": 2},
          {"name": "B", "duration": 2, "deadline": 2},
          {"name": "C", "duration": 1, "deadline": 2}]
# → C

# Duration tie — later deadline dropped
tasks4 = [{"name": "A", "duration": 2, "deadline": 2},
          {"name": "B", "duration": 2, "deadline": 3},
          {"name": "C", "duration": 2, "deadline": 4}]
# → A, C
```

---

## Comparison of Scheduling Algorithms

| | EDD | SPT | Moore's |
|--|-----|-----|---------|
| Sorts by | Deadline | Duration | Deadline (EDD) |
| Drops tasks | No | No | Yes |
| Optimizes for | Min lateness | Min queue length | Min late tasks |
| All tasks completed | Yes | Yes | No |

---

## When to use Moore's Algorithm

- Some tasks can be sacrificed to keep the rest on schedule
- Goal is to maximize the number of on-time completions
- A few late tasks are acceptable but many late tasks are not

## Limitations

- Dropped tasks are not rescheduled — they are lost entirely
- Does not account for task priority or importance weights
- The dropped task may be more important than the ones kept

---

## Study Context

Built while reading *Algorithms to Live By* by Brian Christian and Tom Griffiths (Chapter 5 — Scheduling).
