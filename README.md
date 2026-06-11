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
├── monte_carlo/
│   ├── README.md
│   └── pi_approximate.py
├── scheduling/
│   ├── edd/
│       ├── README.md
│       └── edd.py
│   ├── moore/
│       ├── README.md
│       └── moore.py
│   ├── spt/
│       ├── README.md
│       └── spt.py
├── searching/
│   ├── binary_search/
│       ├── README.md
│       └── binary_search.py
├── sorting/
│   ├── bubble_sort/
│       ├── README.md
│       └── bubble_sort.py
│   ├── bucket_sort/
│       ├── README.md
│       └── bucket_sort.py
│   ├── insertion_sort/
│       ├── README.md
│       └── insertion_sort.py
│   ├── merge_sort/
│       ├── README.md
│       └── merge_sort.py
│   ├── ...
├── ...

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

| Algorithm                                      | Category                     | Complexity |
| ---------------------------------------------- | ---------------------------  | ---------- |
| [Miller-Rabin Primality Test](./miller_rabin/) | Randomized / Number Theory   | O(log² n)  |
| [LRU Cache](./lru_cache/)                      | Data Structures / Caching    | O(1)       | 
| [Bubble Sort](./sorting/bubble_sort)           | Data Structures / Sorting    | O(n²)      | 
| [Insertion Sort](./sorting/insertion_sort)     | Data Structures / Sorting    | O(n²)      | 
| [Merge Sort](./sorting/merge_sort)             | Data Structures / Sorting    | O(n log n) | 
| [Bucket Sort](./sorting/bucket_sort)           | Data Structures / Sorting    | O(n + k)   | 
| [Binary Search](./searching/binary_search)     | Data Structures / Searching  | O(log n)   | 
| [Earliest Due Date](./scheduling/edd)          | Data Structures / Scheduling | O(n log n) | 
| [Moore's Algorithm](./scheduling/moore)        | Data Structures / Scheduling | O(n²)      | 
| [Shortest Processing Time](./scheduling/spt)   | Data Structures / Scheduling | O(n log n) | 

---

_Built with curiosity. Updated as I go._
