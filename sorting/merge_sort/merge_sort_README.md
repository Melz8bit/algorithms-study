# Merge Sort

A Python implementation of Merge Sort — a divide and conquer sorting algorithm that recursively splits a list in half, sorts each half, then merges them back together in sorted order. One of the most practically useful sorting algorithms with a guaranteed O(n log n) performance.

---

## Background

Built as part of a self-directed study curriculum covering algorithms and data structures. Implementation separates the split/recurse logic (`merge_sort`) from the merge logic (`_merge`) for clarity and testability.

**Topics covered in this implementation:**
- Divide and conquer strategy
- Recursion and base cases
- Two-pointer merging technique
- O(n log n) complexity derivation
- Stable sorting behavior
- Space vs time trade-offs

---

## How It Works

### Phase 1 — Split

Recursively divide the list in half until every sublist contains a single element. A single element is always sorted by definition.

```
[64, 34, 25, 12, 22, 11, 90]
        /               \
[64, 34, 25]         [12, 22, 11, 90]
   /      \            /          \
[64]    [34, 25]    [12, 22]    [11, 90]
         /    \      /    \      /    \
       [34]  [25]  [12]  [22]  [11]  [90]
```

### Phase 2 — Merge

Compare the front elements of two sorted lists, take the smaller one, and repeat until both lists are exhausted.

```
Merge [34] and [25]  → [25, 34]
Merge [12] and [22]  → [12, 22]
Merge [11] and [90]  → [11, 90]
Merge [25, 34] and [64]        → [25, 34, 64]
Merge [12, 22] and [11, 90]    → [11, 12, 22, 90]
Merge [25, 34, 64] and [11, 12, 22, 90] → [11, 12, 22, 25, 34, 64, 90]
```

### Why O(n log n)?

- Splitting produces **log n** levels of recursion
- Each level of merging does **O(n)** total work across all sublists
- Combined: **O(n log n)**

---

## Complexity

| Case | Time | Why |
|------|------|-----|
| Worst case | O(n log n) | Always splits and merges regardless of input |
| Average case | O(n log n) | Consistent regardless of input order |
| Best case | O(n log n) | No early exit — always does the full work |
| Space | O(n) | New lists created at each merge step |

---

## Implementation

```python
def _merge(left_list: list, right_list: list) -> list:
    sorted_nums = []

    while left_list and right_list:
        if right_list[0] < left_list[0]:
            sorted_nums.append(right_list.pop(0))
        elif left_list[0] < right_list[0]:
            sorted_nums.append(left_list.pop(0))
        else:
            sorted_nums.append(left_list.pop(0))
            sorted_nums.append(right_list.pop(0))

    sorted_nums.extend(left_list)
    sorted_nums.extend(right_list)

    return sorted_nums


def merge_sort(nums: list) -> list:
    if not nums:
        return []

    if len(nums) == 1:
        return nums

    halfway = len(nums) // 2
    left_list = nums[0:halfway]
    right_list = nums[halfway:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    return _merge(left_list, right_list)
```

---

## Usage

```python
nums = [64, 34, 25, 12, 22, 11, 90]
print(merge_sort(nums))
# [11, 12, 22, 25, 34, 64, 90]

# Works on already sorted lists
nums2 = [11, 12, 22, 25, 34, 64, 90]
print(merge_sort(nums2))
# [11, 12, 22, 25, 34, 64, 90]

# Works on lists with duplicates
nums3 = [5, 3, 5, 1, 3]
print(merge_sort(nums3))
# [1, 3, 3, 5, 5]
```

---

## Comparison with Other Sorting Algorithms

| | Bubble Sort | Insertion Sort | Merge Sort |
|--|-------------|----------------|------------|
| Worst case | O(n²) | O(n²) | O(n log n) |
| Best case | O(n) | O(n) | O(n log n) |
| Space | O(1) | O(1) | O(n) |
| Stable | Yes | Yes | Yes |
| Strategy | Compare adjacent | Walk left | Divide & conquer |

Merge Sort trades space (O(n)) for consistently better time complexity. For large datasets it significantly outperforms Bubble and Insertion Sort.

---

## Design Decisions

**Separate `_merge` function** — keeping the merge logic isolated from the split/recurse logic makes each function easier to reason about and test independently.

**`extend` for remainders** — after the while loop, one list may still have elements. `extend` appends them all in one operation rather than looping.

**`pop(0)` approach** — consuming elements from the front of each list as they're compared keeps the logic clean. The trade-off is that `pop(0)` on a list is O(n) — for performance-critical code, a deque or index pointer would be more efficient.

---

## Study Context

This implementation was built while reading *Algorithms to Live By* by Brian Christian and Tom Griffiths (Chapter 3 — Sorting), as part of a broader curriculum covering algorithms and data structures.
