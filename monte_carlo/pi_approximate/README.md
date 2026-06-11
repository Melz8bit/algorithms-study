# Monte Carlo Simulation — π Approximation

A Python implementation of the Monte Carlo method applied to estimating π — demonstrating how random sampling can approximate values that would be difficult or impossible to calculate exhaustively.

---

## Background

Built as part of a self-directed study curriculum covering algorithms and data structures. This is the first implementation in a Monte Carlo simulation series, each demonstrating a different application of randomized sampling.

**Topics covered in this implementation:**
- Monte Carlo method fundamentals
- Geometric probability
- Random sampling and convergence
- Law of large numbers
- Probabilistic vs deterministic algorithms

---

## How It Works

### The geometry

Imagine a unit circle (radius = 1) inscribed inside a square with sides from -1 to 1. The areas are:

- Circle area: πr² = π
- Square area: (2r)² = 4
- Ratio: π/4

### The simulation

Throw random darts at the square. Count how many land inside the circle. The ratio of hits to total throws approximates π/4 — multiply by 4 to get π.

```
Total darts thrown:  1,000,000
Darts inside circle: ~785,398
Ratio:               ~0.7854
π approximation:     ~3.1416
```

### Determining if a point is inside the circle

A point (x, y) is inside the unit circle if:

**x² + y² ≤ 1**

This follows directly from the equation of a circle with radius 1 centered at the origin.

---

## Convergence

The more darts thrown, the closer the approximation gets to the true value of π:

| Simulations | Typical result | Accuracy |
|-------------|---------------|----------|
| 100 | ~3.08–3.50 | ±0.1 |
| 1,000 | ~3.10–3.18 | ±0.05 |
| 10,000 | ~3.12–3.16 | ±0.02 |
| 1,000,000 | ~3.140–3.143 | ±0.001 |

Results vary each run due to randomness — this is expected and intentional.

---

## Complexity

| | Complexity |
|--|--|
| Time | O(n) — one iteration per dart thrown |
| Space | O(1) — only a counter is maintained |

---

## Implementation

```python
import random


def pi_approximate(num_darts: int) -> float:
    circle_hits = 0
    for i in range(num_darts):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if (x**2) + (y**2) <= 1:
            circle_hits += 1

    return (circle_hits / num_darts) * 4
```

---

## Usage

```python
import math

print(pi_approximate(100))       # rough approximation
print(pi_approximate(1_000))     # better
print(pi_approximate(10_000))    # good
print(pi_approximate(1_000_000)) # very close
print(math.pi)                   # 3.141592653589793
```

---

## What is the Monte Carlo Method?

The Monte Carlo method replaces exhaustive probability calculations with random sample simulations. Instead of calculating the exact probability mathematically, you simulate the scenario thousands or millions of times and observe the outcome frequency.

**When to use it:**
- Exhaustive calculation is too complex or computationally expensive
- An approximate answer is acceptable
- The problem can be modeled with random sampling

**Real world applications:**
- Physics simulations (particle behavior, nuclear reactions)
- Financial risk modeling (stock price forecasting)
- Game AI (estimating win probabilities in chess/Go)
- Drug trial simulations (from Chapter 9 — Algorithms to Live By)

---

## Connection to the Book

From *Algorithms to Live By* Chapter 9 — Randomness: the Monte Carlo method demonstrates that randomness isn't just noise to be eliminated — it can be a deliberate tool for solving problems that deterministic approaches can't handle efficiently. Sampling gives you an answer when exact calculation won't.

---

## Study Context

Built while reading *Algorithms to Live By* by Brian Christian and Tom Griffiths (Chapter 9 — Randomness), as part of a broader curriculum covering algorithms and data structures.
