# Monte Carlo Simulation — Monty Hall Problem

A Python implementation of the Monty Hall problem using Monte Carlo simulation — demonstrating how randomized sampling can confirm a counterintuitive probability result.

---

## Background

Built as part of a self-directed study curriculum covering algorithms and data structures. The Monty Hall problem is one of the most famous probability puzzles — the simulation result surprises most people even after they understand the math.

**Topics covered in this implementation:**
- Monte Carlo method applied to probability
- Conditional probability
- Simulating two strategies simultaneously
- Convergence of simulated results to theoretical values

---

## The Problem

A game show host presents three doors. Behind one is a prize; the other two are empty. You pick a door. The host — who knows where the prize is — always opens one of the other doors to reveal an empty one. You are then offered a choice: stay with your original door or switch to the remaining unopened door.

**Should you switch?**

Most people say it doesn't matter — 50/50. They're wrong.

---

## The Math

When you first pick a door:
- **1/3 chance** you picked the prize door
- **2/3 chance** the prize is behind one of the other two doors

When the host reveals an empty door, that 2/3 probability doesn't disappear — it transfers entirely to the remaining unpicked door.

| Strategy | Win probability |
|----------|----------------|
| Stay | 1/3 ≈ 33.3% |
| Switch | 2/3 ≈ 66.7% |

### Why switching wins 2/3 of the time

| Your pick | Prize location | Host reveals | Stay result | Switch result |
|-----------|---------------|--------------|-------------|---------------|
| Door 1 (prize) | Door 1 | Door 2 or 3 | ✅ Win | ❌ Lose |
| Door 1 (empty) | Door 2 | Door 3 | ❌ Lose | ✅ Win |
| Door 1 (empty) | Door 3 | Door 2 | ❌ Lose | ✅ Win |

Staying wins in 1 out of 3 cases. Switching wins in 2 out of 3 cases.

---

## Implementation

```python
import random


def monty_hall(iterations: int):
    stay, swap = 0, 0

    for i in range(iterations):
        doors = [None] * 3
        doors[random.randint(0, 2)] = "x"

        # Player selects a door
        user_door = random.randint(0, 2)
        is_winning = doors[user_door] == "x"

        # Host removes a losing door
        doors.remove(None)

        # Reassign user's door index after removal
        user_door = doors.index("x") if is_winning else doors.index(None)

        # Stay strategy
        if doors[user_door] == "x":
            stay += 1

        # Switch strategy — other door in the 2-item list
        if doors[1 - user_door] == "x":
            swap += 1

    return {
        "stayed": stay / iterations,
        "swapped": swap / iterations,
    }
```

---

## Usage

```python
print(monty_hall(100))      # rough — high variance
print(monty_hall(1000))     # better
print(monty_hall(10000))    # good
print(monty_hall(100000))   # converges clearly to ~0.333 and ~0.667
```

Sample output:
```
{'stayed': 0.338, 'swapped': 0.662}
{'stayed': 0.334, 'swapped': 0.666}
{'stayed': 0.333, 'swapped': 0.667}
{'stayed': 0.3328, 'swapped': 0.6672}
```

---

## Key Design Decision

Both strategies are evaluated on the same trial — same door setup, same initial pick, same revealed door. This allows direct comparison without running the simulation twice and eliminates any variance between separate runs.

After the host removes a losing door, two doors remain at indices 0 and 1. The switch door is always `1 - user_door` since those are the only two possible indices.

---

## Connection to the Book

From *Algorithms to Live By* Chapter 9 — Randomness: the Monte Carlo method replaces exhaustive probability calculations with simulation. The Monty Hall result is mathematically provable, but simulation makes it viscerally real — watching 100,000 trials converge to exactly 1/3 and 2/3 is more convincing than any proof.

---

## Study Context

Built while reading *Algorithms to Live By* by Brian Christian and Tom Griffiths (Chapter 9 — Randomness), as part of a broader curriculum covering algorithms and data structures.
