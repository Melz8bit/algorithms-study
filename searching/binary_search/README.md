# Binary Search

A Python implementation of Binary Search — a fundamental search algorithm that finds a target value in a sorted list by repeatedly halving the search space. Significantly more efficient than linear search for large sorted datasets.

---

## Background

Built as part of a self-directed study curriculum covering algorithms and data structures. Binary search is the natural companion to sorting — once a list is sorted, binary search makes repeated lookups dramatically faster.

**Topics covered in this implementation:**
- Divide and conquer search strategy
- Two-pointer technique (left/right boundaries)
- Midpoint calculation
- O(log n) complexity derivation
- Boundary conditions and edge cases

---

## How It Works

### Core operation

Maintain a left and right pointer defining the current search window. At each step:

1. Calculate the midpoint
2. If target equals mid → return index
3. If target is less than mid → search left half
4. If target is greater than mid → search right half
5. Repeat until found or pointers cross

```
Target: 25
List:   [11, 12, 22, 25, 34, 64, 90]
         L               R

Step 1: mid = index 3 → value 25 → target == mid → return 3 ✅
```

```
Target: 64
List:   [11, 12, 22, 25, 34, 64, 90]
         L                        R

Step 1: mid = index 3 → value 25 → 64 > 25 → move left pointer right
Step 2: mid = index 5 → value 64 → target == mid → return 5 ✅
```

### Why O(log n)?

Each iteration halves the search space. For a list of n elements:
- After 1 step: n/2 elements remain
- After 2 steps: n/4 elements remain
- After k steps: n/2^k elements remain

The search ends when n/2^k = 1, so k = log₂(n). For a list of 1,000,000 elements that's only 20 steps.

---

## Complexity

| Case | Time | Why |
|------|------|-----|
| Best case | O(1) | Target is at the midpoint on the first check |
| Average case | O(log n) | Search space halves each iteration |
| Worst case | O(log n) | Target at edge or not present |
| Space | O(1) | In-place, only two pointers needed |

---

## Implementation

```python
def binary_search(target: int, nums: list) -> int:
    if target < nums[0] or target > nums[-1]:
        return None

    left_pointer = 0
    right_pointer = len(nums) - 1

    while left_pointer <= right_pointer:
        mid = (left_pointer + right_pointer) // 2

        if target == nums[mid]:
            return mid

        if target < nums[mid]:
            right_pointer = mid - 1

        if target > nums[mid]:
            left_pointer = mid + 1

    return None
```

---

## Usage

```python
nums = [11, 12, 22, 25, 34, 64, 90]

print(binary_search(11, nums))   # 0  — first element
print(binary_search(90, nums))   # 6  — last element
print(binary_search(25, nums))   # 3  — middle element
print(binary_search(50, nums))   # None — not in list
print(binary_search(5, nums))    # None — below range
print(binary_search(100, nums))  # None — above range
```

---

## Requirements

**The list must be sorted.** Binary search produces incorrect results on unsorted input. Use any of the sorting implementations in this repo first if needed:

```python
from sorting.merge_sort.merge_sort import merge_sort

nums = merge_sort([64, 34, 25, 12, 22, 11, 90])
index = binary_search(25, nums)
```

---

## Comparison with Linear Search

| | Linear Search | Binary Search |
|--|--------------|---------------|
| Time complexity | O(n) | O(log n) |
| Requires sorted input | No | Yes |
| 1,000,000 elements | Up to 1,000,000 steps | Up to 20 steps |
| Best for | Small or unsorted lists | Large sorted lists |

---

## Connection to Sorting

Binary search is the payoff for sorting. From the study notes on Chapter 3 — Sorting:

- Sorting cost: O(n log n) upfront
- Each binary search after: O(log n)
- Linear scan unsorted: O(n) per lookup

If you search a list only once, skip sorting and scan linearly. If you search it many times, sort first and binary search — the upfront cost amortizes across every subsequent lookup. This is exactly the logic behind database indexes.

---

## Real World Applications

| System | How binary search is used |
|--------|--------------------------|
| Database indexes | B-tree traversal is binary search on a sorted tree structure |
| Git bisect | Binary searches commit history to find which commit introduced a bug |
| Dictionary lookups | Binary search on sorted word lists |
| Game mechanics | Finding a value in a sorted leaderboard |

---

## Study Context

This implementation was built while reading *Algorithms to Live By* by Brian Christian and Tom Griffiths (Chapter 3 — Sorting), as part of a broader curriculum covering algorithms and data structures.
