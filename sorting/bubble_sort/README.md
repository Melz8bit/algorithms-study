# Bubble Sort

A Python implementation of Bubble Sort — one of the most fundamental sorting algorithms, used as a foundational teaching tool for understanding comparison-based sorting and algorithmic optimization.

---

## Background

Built as part of a self-directed study curriculum covering algorithms and data structures. Implementation includes an early stopping optimization that detects when the list is already sorted and exits before completing all passes.

**Topics covered in this implementation:**
- Comparison-based sorting
- In-place sorting (no extra space required)
- Early stopping optimization with boolean flag
- Big-O complexity analysis
- Best vs worst case behavior

---

## How It Works

### Core operation

Compare each adjacent pair of elements. If they are out of order, swap them. Repeat for the entire list. After each full pass, the largest unsorted element has "bubbled up" to its correct position.

```
Pass 1: [64, 34, 25, 12, 22, 11, 90] → [34, 25, 12, 22, 11, 64, 90]
Pass 2: [34, 25, 12, 22, 11, 64, 90] → [25, 12, 22, 11, 34, 64, 90]
...
Pass 6: [11, 12, 22, 25, 34, 64, 90] → no swaps → sorted, exit early
```

### Early stopping optimization

A `had_swap` flag is initialized to `False` at the start of each pass. If any swap occurs it is set to `True`. If an entire pass completes without a swap, the list is already sorted and the algorithm exits immediately — avoiding unnecessary passes.

Without this optimization, Bubble Sort always runs n passes regardless of input order. With it, an already sorted list exits after a single pass.

---

## Complexity

| Case | Time | Why |
|------|------|-----|
| Worst case | O(n²) | Reverse sorted input — maximum swaps every pass |
| Average case | O(n²) | Random input |
| Best case | O(n) | Already sorted — exits after one pass with early stopping |
| Space | O(1) | In-place, no extra memory needed |

---

## Implementation

```python
def bubble_sort(nums):
    for _ in nums:
        had_swap = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                had_swap = True

        if not had_swap:
            break

    return nums
```

---

## Usage

```python
nums = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(nums))
# [11, 12, 22, 25, 34, 64, 90]

# Already sorted — exits after one pass
nums2 = [11, 12, 22, 25, 34, 64, 90]
print(bubble_sort(nums2))
# [11, 12, 22, 25, 34, 64, 90]
```

---

## When to use Bubble Sort

Bubble Sort is rarely used in production due to its O(n²) average case. It is most useful when:

- The list is nearly sorted — early stopping makes it efficient
- Simplicity is more important than performance
- Teaching or demonstrating sorting concepts

For general purpose sorting, Merge Sort (O(n log n)) or Python's built-in `sorted()` (Timsort, O(n log n)) are significantly better choices.

---

## Study Context

This implementation was built while reading *Algorithms to Live By* by Brian Christian and Tom Griffiths (Chapter 3 — Sorting), as part of a broader curriculum covering algorithms and data structures.
