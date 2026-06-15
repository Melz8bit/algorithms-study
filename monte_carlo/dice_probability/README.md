# Monte Carlo Simulation — Dice Probability

A Python implementation of dice probability estimation using Monte Carlo simulation — demonstrating how random sampling approximates theoretical probability for any number of dice, sides, and target sums.

---

## Background

Built as part of a self-directed study curriculum covering algorithms and data structures. This simulation generalizes across any dice configuration, making it useful for tabletop gaming, probability education, and demonstrating Monte Carlo convergence.

**Topics covered in this implementation:**
- Monte Carlo method applied to dice probability
- List comprehensions for concise simulation
- Convergence of simulated results to theoretical values
- O(n × d) complexity analysis

---

## How It Works

For each iteration, roll `num_dice` dice with `sides` sides each and sum the results. Count how many rolls hit the target sum. Divide by total iterations to get the estimated probability.

```
2d6, target = 7, iterations = 1,000,000

Possible combinations that sum to 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1 = 6 combinations
Total combinations: 6 × 6 = 36
Theoretical probability: 6/36 = 1/6 ≈ 0.1667

Simulated result: ~0.1670
```

---

## Complexity

| | Complexity |
|--|--|
| Time | O(n × d) — n iterations, each rolling d dice |
| Space | O(d) — list of d dice rolls per iteration |

For small fixed d (e.g. 2 dice), effectively O(n) in practice.

---

## Implementation

```python
import random


def dice_probability(num_dice: int, sides: int, target: int, iterations: int) -> float:
    hit = 0
    for x in range(iterations):
        roll = [random.randint(1, sides) for _ in range(num_dice)]

        if sum(roll) == target:
            hit += 1

    return hit / iterations
```

---

## Usage

```python
# Probability of rolling 7 with 2d6
print(dice_probability(2, 6, 7, 100))        # rough
print(dice_probability(2, 6, 7, 10000))      # better
print(dice_probability(2, 6, 7, 1_000_000))  # converges to ~0.1667
# Theoretical: 6/36 = 0.1667

# Probability of rolling 12 with 2d6 (snake eyes inverse)
print(dice_probability(2, 6, 12, 1_000_000))
# Theoretical: 1/36 = 0.0278

# Probability of rolling 10 with 3d6
print(dice_probability(3, 6, 10, 1_000_000))
# Theoretical: 27/216 = 0.125
```

---

## Convergence

| Iterations | Typical result (2d6, target=7) | Variance |
|------------|-------------------------------|----------|
| 100 | 0.10 — 0.22 | High |
| 1,000 | 0.14 — 0.19 | Medium |
| 10,000 | 0.161 — 0.172 | Low |
| 1,000,000 | 0.1664 — 0.1670 | Very low |

Some variance always remains — this is expected. Monte Carlo approximates but never eliminates randomness.

---

## Theoretical Verification — 2d6

| Target | Combinations | Probability | Simulated (1M) |
|--------|-------------|-------------|----------------|
| 2 | 1 | 1/36 ≈ 0.028 | ~0.028 |
| 7 | 6 | 6/36 ≈ 0.167 | ~0.167 |
| 12 | 1 | 1/36 ≈ 0.028 | ~0.028 |

---

## Connection to the Book

From *Algorithms to Live By* Chapter 9 — Randomness: the Monte Carlo method replaces exhaustive probability calculations with simulation. Rather than enumerating all 36 combinations of 2d6, the simulation throws a million virtual dice and observes the frequency — the same principle used in nuclear physics simulations, financial modeling, and drug trial design.

---

## Study Context

Built while reading *Algorithms to Live By* by Brian Christian and Tom Griffiths (Chapter 9 — Randomness), as part of a broader curriculum covering algorithms and data structures.
