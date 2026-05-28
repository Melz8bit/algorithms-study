# Algorithms & Data Structures

A self-directed study repository documenting my journey through algorithms, data structures, and computational theory. Each implementation is built from first principles with a focus on understanding the underlying math before writing a single line of code.

---

## Structure

Each algorithm lives in its own folder with its own README, implementation, and tests.

```
algorithms-study/
├── lru_cache/
│   ├── README.md
│   └── lru.py
├── miller_rabin/
│   ├── README.md
│   └── miller_rabin.py
├── sorting/
│   ├── bubble_sort/
│       ├── README.md
│       └── bubble_sort.py
│   ├── insertion_sort/
│       ├── README.md
│       └── insertion_sort.py
│   ├── ...
├── ...
```

---

## Curriculum

| Phase | Topics                                         | Status      |
| ----- | ---------------------------------------------- | ----------- |
| 1     | Arrays, Linked Lists, Stacks & Queues, Strings | In progress |
| 2     | Hash Tables, Heaps, Binary Trees, BSTs         | Upcoming    |
| 3     | Balanced BSTs, Tries, Graphs, Union-Find       | Upcoming    |
| 4     | Recursion, Dynamic Programming, System Design  | Upcoming    |

---

## Reading List

Study is supplemented by:

- _Algorithms to Live By_ — Brian Christian & Tom Griffiths
- _The Algorithm Design Manual_ — Steven Skiena
- _How to Solve It_ — George Pólya

---

## Implementations

| Algorithm                                      | Category                   | Complexity |
| ---------------------------------------------- | -------------------------- | ---------- |
| [Miller-Rabin Primality Test](./miller_rabin/) | Randomized / Number Theory | O(log² n)  |
| [LRU Cache](./lru_cache/)                      | Data Structures / Caching  | O(1)       | 
| [Bubble Sort](./sorting/bubble_sort)           | Data Structures / Sorting  | O(n²)      | 
| [Insertion Sort](./sorting/insertion_sort)     | Data Structures / Sorting  | O(n²)      | 
| [Merge Sort](./sorting/merge_sort)             | Data Structures / Sorting  | O(n log n) | 

---

_Built with curiosity. Updated as I go._
