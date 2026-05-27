# Miller-Rabin Primality Test

A Python implementation of the Miller-Rabin probabilistic primality test — a foundational algorithm in cryptography used to efficiently identify large prime numbers.

---

## Background

Built as part of a self-directed study curriculum covering algorithms, data structures, and computational complexity. Implementation was derived from first principles, starting from modular arithmetic and Fermat's Little Theorem.

**Topics covered in this implementation:**
- Modular arithmetic and modular exponentiation
- Probabilistic algorithms and error margins
- Big-O complexity analysis
- Exponentiation by squaring — O(log d) vs naive O(d)
- Fermat's Little Theorem and Carmichael numbers
- Edge case handling and defensive programming

---

## How It Works

### 1. Decompose n - 1

Every even number can be written as **2^s × d** where d is odd. We factor out all 2s from n-1 to find s and d:

```
n - 1 = 2^s × d
```

### 2. Pick a random witness

For each of k rounds, pick a random integer `a` where `2 ≤ a ≤ n-2` and compute:

```
x = a^d mod n
```

### 3. Apply the three conditions

- **Condition 1:** If x = 1 or x = n-1 → witness passes, try next witness
- **Condition 2:** Square x repeatedly (s-1 times); if x hits n-1 → witness passes
- **Condition 3:** If x never hits n-1 → n is **definitively composite**

### 4. Repeat for k witnesses

If all k witnesses pass without finding evidence of compositeness → n is **probably prime**.

The probability of a false positive is at most **(1/4)^k** — with k = log₂(n) rounds this is astronomically small for any practical input.

---

## Complexity

| Operation | Complexity |
|-----------|------------|
| Factor out 2s (find s, d) | O(log n) |
| Modular exponentiation per witness | O(log d) |
| Full primality test (k witnesses) | O(k log n) = O(log² n) |

Using Python's built-in `pow(base, exp, mod)` for modular exponentiation is critical — the naive `base**exp % mod` approach runs in O(d) time and becomes unusable for cryptographic-scale numbers.

---

## Implementation

```python
import math
import random


def miller_rabin(n: int) -> bool:
    if n == 2 or n == 3:
        return True

    if n == 1 or n % 2 == 0:
        return False

    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    k = int(math.log2(n))
    for i in range(k):
        witness = random.randint(2, n - 2)

        # Modular exponentiation: O(k log d) vs naive O(d)
        x = pow(witness, d, n)

        if (x == 1) or (x == n - 1):
            continue

        for _ in range(1, s):
            x = (x**2) % n
            if x == 1:
                return False
            if x == (n - 1):
                return True

        return False

    return True
```

---

## Usage

```python
# Known primes
primes = [2, 3, 5, 7, 11, 13, 97, 104729]
for p in primes:
    print(f"{p} → {miller_rabin(p)}")  # All True

# Known composites
composites = [1, 4, 9, 15, 100, 104730]
for c in composites:
    print(f"{c} → {miller_rabin(c)}")  # All False
```

---

## Real World Application

Miller-Rabin is used in production cryptographic libraries (OpenSSL, Python's `secrets` module) to generate large prime numbers for:

- **RSA encryption** — key generation requires finding two large primes
- **Diffie-Hellman key exchange** — relies on large prime moduli
- **Digital signatures** — DSA and ECDSA both require prime field parameters

OpenSSL runs 64 rounds for cryptographic primes, reducing the false positive probability to effectively zero.

---

## Study Context

This implementation was built while reading *Algorithms to Live By* by Brian Christian and Tom Griffiths, as part of a broader curriculum covering:

- **Phase 1** — Arrays, Linked Lists, Stacks & Queues
- **Phase 2** — Hash Tables, Heaps, Binary Trees, BSTs
- **Phase 3** — Balanced BSTs, Tries, Graphs, Union-Find
- **Phase 4** — Recursion, Dynamic Programming, System Design

---

## References

- *Algorithms to Live By* — Brian Christian & Tom Griffiths
- Miller, G.L. (1976). Riemann's Hypothesis and Tests for Primality
- Rabin, M.O. (1980). Probabilistic Algorithm for Testing Primality
