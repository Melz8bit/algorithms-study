# Bucket Sort

A Python implementation of Bucket Sort — a distribution-based sorting algorithm that divides elements into range-based buckets, sorts each bucket individually, then concatenates the results. Efficient when values are distributed across a known range.

---

## Background

Built as part of a self-directed study curriculum covering algorithms and data structures. Implementation uses Insertion Sort for internal bucket sorting, leveraging its efficiency on small lists.

**Topics covered in this implementation:**
- Distribution-based sorting
- Bucket width and index calculation
- Range-based partitioning
- Internal bucket sorting with Insertion Sort
- O(n + k) space complexity
- When bucket sort outperforms comparison-based sorts

---

## How It Works

### Core operation

1. Find the min and max values to determine the range
2. Calculate bucket width: `(max - min) // n`
3. Assign each element to a bucket: `(value - min) // bucket_width`
4. Sort each bucket internally using Insertion Sort
5. Concatenate all sorted buckets in order

```
Input:  [64, 34, 25, 12, 22, 11, 90]
min=11, max=90, width=11

Bucket 0 (11-21):  [12, 11]  → sorted: [11, 12]
Bucket 1 (22-32):  [25, 22]  → sorted: [22, 25]
Bucket 2 (33-43):  [34]      → sorted: [34]
Bucket 3 (44-54):  []
Bucket 4 (55-65):  [64]      → sorted: [64]
Bucket 5 (66-76):  []
Bucket 6 (77-90):  [90]      → sorted: [90]

Output: [11, 12, 22, 25, 34, 64, 90]
```

### Edge case — maximum value

The maximum value always overflows to bucket n (out of bounds). It's explicitly assigned to the last bucket instead:

```python
if num == max_num:
    bucket_index -= 1
```

---

## Complexity

| Case | Time | Why |
|------|------|-----|
| Best case | O(n + k) | Uniform distribution — each bucket has ~1 element |
| Average case | O(n + k) | Reasonably distributed values |
| Worst case | O(n²) | All elements land in one bucket — degrades to Insertion Sort |
| Space | O(n + k) | n elements across k buckets |

Where k = number of buckets (equal to n in this implementation).

### Book's O(nm) vs standard O(n+k)

The book's O(nm) accounts for sorting *within* each bucket — if each bucket requires internal sorting, the work per bucket multiplies. The standard O(n+k) assumes items are read back out without internal sorting. Both are correct for their respective assumptions.

---

## Implementation

```python
from insertion_sort import insertion_sort


def bucket_sort(nums: list) -> list:
    max_num = max(nums)
    min_num = min(nums)
    bucket_width = (max_num - min_num) // len(nums)

    buckets = [[] for _ in range(len(nums))]
    for num in nums:
        bucket_index = (num - min_num) // bucket_width
        if num == max_num:
            bucket_index -= 1

        buckets[bucket_index].append(num)

    sorted_list = []
    for bucket in buckets:
        if bucket:
            sorted_list += insertion_sort(bucket)

    return sorted_list
```

---

## Usage

```python
nums = [64, 34, 25, 12, 22, 11, 90]
print(bucket_sort(nums))
# [11, 12, 22, 25, 34, 64, 90]
```

---

## Dependencies

Requires `insertion_sort.py` from the `insertion_sort` folder:

```python
from insertion_sort import insertion_sort
```

---

## Comparison with Other Sorting Algorithms

| | Bubble Sort | Insertion Sort | Merge Sort | Bucket Sort |
|--|-------------|----------------|------------|-------------|
| Worst case | O(n²) | O(n²) | O(n log n) | O(n²) |
| Average case | O(n²) | O(n²) | O(n log n) | O(n + k) |
| Best case | O(n) | O(n) | O(n log n) | O(n + k) |
| Space | O(1) | O(1) | O(n) | O(n + k) |
| Strategy | Compare adjacent | Walk left | Divide & conquer | Distribute & sort |

---

## When to use Bucket Sort

- Values are uniformly distributed across a known range
- The range of values is not significantly larger than the number of elements
- You need linear average-case performance and can accept O(n²) worst case
- Floating point numbers in a known range — bucket sort excels here

## When NOT to use Bucket Sort

- Values are heavily clustered — all elements land in one bucket
- Range is unknown or extremely large relative to n
- You need guaranteed O(n log n) — use Merge Sort instead

---

## Real World Connections

- **Panini sticker sorting** — opening a pack and distributing stickers into country piles before placing them in the book is bucket sort followed by insertion sort
- **Sports divisions** — teams assigned to divisions (buckets) by geography or ranking, then sorted within each division

---

## Study Context

This implementation was built while reading *Algorithms to Live By* by Brian Christian and Tom Griffiths (Chapter 3 — Sorting), as part of a broader curriculum covering algorithms and data structures.
