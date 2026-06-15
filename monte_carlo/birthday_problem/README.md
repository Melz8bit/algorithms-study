# Monte Carlo Simulation — Birthday Problem

A Python implementation of the Birthday Problem using Monte Carlo simulation — demonstrating one of probability's most counterintuitive results: how few people are needed before two share a birthday.

---

## Background

Built as part of a self-directed study curriculum covering algorithms and data structures. The Birthday Problem is a classic probability puzzle where human intuition dramatically underestimates the likelihood of a shared birthday.

**Topics covered in this implementation:**
- Monte Carlo method applied to combinatorial probability
- Early exit optimization
- Set vs list for O(1) lookup
- Convergence of simulated results to theoretical values

---

## The Problem

In a group of n people, what is the probability that at least two people share the same birthday?

Most people guess you'd need around 183 people (half of 365). The actual answer is surprising:

| People | Probability of shared birthday |
|--------|-------------------------------|
| 10 | ~11.7% |
| 23 | ~50.7% |
| 50 | ~97.0% |
| 70 | ~99.9% |

With just **23 people** there's already a 50% chance of a shared birthday.

---

## Why it's counterintuitive

Most people think about the probability that someone shares *their* birthday — which is indeed low. But the Birthday Problem asks whether *any pair* among the group shares a birthday.

With 23 people there are **253 possible pairs** (23 × 22 / 2). Each pair has a 1/365 chance of sharing a birthday. Those probabilities compound quickly across 253 pairs, pushing the overall probability to 50% much faster than intuition suggests.

---

## Complexity

| | Complexity |
|--|--|
| Time | O(n × p) — n iterations, each checking up to p people |
| Space | O(p) — set of birthdays per iteration |

Early exit on a match means most iterations terminate well before checking all p people.

---

## Implementation

```python
import random


def birthday_problem(num_people: int, iterations: int) -> float:
    hits = 0
    for i in range(iterations):
        bdays = set()
        for _ in range(num_people):
            bday = random.randint(1, 365)

            if bday in bdays:
                hits += 1
                break

            bdays.add(bday)

    return hits / iterations
```

### Design decisions

**Set instead of list** — checking `bday in bdays` is O(1) with a set vs O(n) with a list. Since order doesn't matter here, a set is the right structure.

**Early exit** — once a shared birthday is found in a trial, the iteration stops immediately. No need to generate all remaining birthdays.

**Outer iterations loop** — each iteration is one independent trial with a fresh group of n people. The fraction of trials with a shared birthday is the probability estimate.

---

## Usage

```python
print(birthday_problem(23, 100))        # rough — around 0.50
print(birthday_problem(23, 10000))      # better — converges to ~0.507
print(birthday_problem(70, 10000))      # converges to ~0.999
print(birthday_problem(10, 10000))      # converges to ~0.117
```

---

## Convergence

| Iterations | Result (23 people) | Variance |
|------------|-------------------|----------|
| 100 | 0.40 — 0.60 | High |
| 1,000 | 0.48 — 0.53 | Medium |
| 10,000 | 0.503 — 0.511 | Low |
| 100,000 | 0.5068 — 0.5072 | Very low |

---

## Connection to the Book

From *Algorithms to Live By* Chapter 9 — Randomness: Monte Carlo simulation replaces complex combinatorial calculations with direct sampling. Computing the exact Birthday Problem probability requires careful inclusion-exclusion math across hundreds of pairs — simulation sidesteps all of that and arrives at the same answer by just generating random birthdays and counting matches.

---

## Study Context

Built while reading *Algorithms to Live By* by Brian Christian and Tom Griffiths (Chapter 9 — Randomness), as part of a broader curriculum covering algorithms and data structures.
