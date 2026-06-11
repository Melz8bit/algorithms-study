# Insertion Sort

A Python implementation of Insertion Sort — a simple, intuitive sorting algorithm that builds a sorted portion of the list one element at a time by walking each new element backwards into its correct position.

---

## Background

Built as part of a self-directed study curriculum covering algorithms and data structures. Implementation uses the shift-based approach rather than swapping, which is more efficient as each shift requires one assignment instead of three.

**Topics covered in this implementation:**
- Comparison-based in-place sorting
- Sorted vs unsorted region boundary tracking
- Shift vs swap distinction
- Big-O complexity analysis
- Best vs worst case behavior

---

## How It Works

### Core operation

Treat the list as two regions — a sorted left portion and an unsorted right portion. The sorted region starts as just the first element. For each subsequent element:

1. Store the current element as `key`
2. Walk backwards through the sorted region
3. Shift each element that is larger than `key` one position to the right
4. Place `key` in the gap left behind

```
Initial:  [64, 34, 25, 12, 22, 11, 90]
Step 1:   [34, 64, 25, 12, 22, 11, 90]  ← 34 walks left past 64
Step 2:   [25, 34, 64, 12, 22, 11, 90]  ← 25 walks left past 64, 34
Step 3:   [12, 25, 34, 64, 22, 11, 90]  ← 12 walks left past 64, 34, 25
Step 4:   [12, 22, 25, 34, 64, 11, 90]  ← 22 walks left past 64, 34, 25
Step 5:   [11, 12, 22, 25, 34, 64, 90]  ← 11 walks all the way to front
Step 6:   [11, 12, 22, 25, 34, 64, 90]  ← 90 already in place
```

### Shift vs swap

Rather than swapping elements, each larger element is shifted one position right to make room. This requires one assignment per shift instead of three, making it more efficient in practice even though the Big-O is the same.

---

## Complexity

| Case | Time | Why |
|------|------|-----|
| Worst case | O(n²) | Reverse sorted — every element walks all the way to the front |
| Average case | O(n²) | Random input |
| Best case | O(n) | Already sorted — inner while loop never executes |
| Space | O(1) | In-place, no extra memory needed |

---

## Implementation

```python
def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1  # Last item of sorted portion

        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]  # Shift element right
            j -= 1

        nums[j + 1] = key  # Place key in correct position

    return nums
```

---

## Usage

```python
nums = [64, 34, 25, 12, 22, 11, 90]
print(insertion_sort(nums))
# [11, 12, 22, 25, 34, 64, 90]
```

---

## Comparison with Bubble Sort

| | Bubble Sort | Insertion Sort |
|--|-------------|----------------|
| Mechanism | Swap adjacent pairs | Shift elements, place key |
| Best case | O(n) with early stopping | O(n) naturally |
| Assignments per step | 3 (swap) | 1 (shift) |
| Practical speed | Slower | Faster in practice |

Insertion sort is generally preferred over Bubble Sort for small lists or nearly sorted data. Python's built-in Timsort uses Insertion Sort internally for small subarrays.

---

## When to use Insertion Sort

- Small lists (typically n < 20)
- Nearly sorted data — performs close to O(n)
- Online sorting — can sort elements as they arrive, one at a time
- As a component of more complex algorithms (e.g. Timsort)

---

## Study Context

This implementation was built while reading *Algorithms to Live By* by Brian Christian and Tom Griffiths (Chapter 3 — Sorting), as part of a broader curriculum covering algorithms and data structures.
