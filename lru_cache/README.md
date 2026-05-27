# LRU Cache

A Python implementation of a Least Recently Used (LRU) Cache — a foundational data structure used in operating systems, databases, web browsers, and CDNs to manage limited fast-access memory efficiently.

---

## Background

Built as part of a self-directed study curriculum covering algorithms and data structures. Implementation was derived from first principles, starting from the concept of temporal locality and working through the two-structure design that achieves O(1) performance for all operations.

**Topics covered in this implementation:**
- Doubly linked lists and sentinel node pattern
- Hash map integration for O(1) lookup
- Cache eviction policy (LRU)
- Temporal locality — recently used items are likely to be used again
- Private helper methods and encapsulation
- Edge case handling

---

## How It Works

### The problem

A cache has limited capacity. When it fills up, something must be evicted to make room for new items. LRU evicts the item that was used least recently — based on the observation that recently accessed items are statistically more likely to be accessed again.

### The two-structure design

Achieving O(1) for all operations requires two data structures working together:

**Doubly Linked List** — maintains recency order
- Head (most recent) ← → nodes ← → Tail (least recent)
- Sentinel head and tail nodes eliminate edge cases
- Every access moves the node to the front in O(1)

**Hash Map** — enables O(1) lookup
- Maps each key directly to its node in the linked list
- Without this, finding a node would require O(n) traversal

### Operations

**get(key)**
1. Look up key in hash map — O(1)
2. Move node to front of linked list — O(1)
3. Return node's value

**put(key, value)**
- Key exists → update value, move to front
- Cache full → evict tail node, insert new node at front, update map
- Cache has space → insert new node at front, update map, increment size

---

## Complexity

| Operation | Time | Space |
|-----------|------|-------|
| get | O(1) | — |
| put | O(1) | — |
| Overall space | — | O(capacity) |

---

## Implementation

```python
class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class lru_cache:
    def __init__(self, capacity):
        # Sentinel head and tail nodes — eliminate edge cases
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.lru_map = {}  # key → node, O(1) lookup
        self.capacity = capacity
        self.size = 0

    def _remove(self, node):
        # Pure linked list operation — detach node from current position
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert(self, node):
        # Pure linked list operation — insert node at front (most recent)
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.lru_map:
            return None

        node = self.lru_map[key]
        self._remove(node)
        self._insert(node)
        return node.value

    def put(self, key, value):
        node = Node(key, value)

        # Case 1: key already exists — update value and move to front
        if key in self.lru_map:
            node = self.lru_map[key]
            node.value = value
            self._remove(node)
            self._insert(node)

        # Case 2: cache is full — evict LRU node, insert new node
        elif self.size == self.capacity:
            last_node = self.tail.prev
            self._remove(last_node)
            self._insert(node)
            del self.lru_map[last_node.key]
            self.lru_map[key] = node

        # Case 3: cache has space — insert new node
        else:
            self._insert(node)
            self.lru_map[key] = node
            self.size += 1
```

---

## Usage

```python
cache = lru_cache(3)
cache.put("a", 1)
cache.put("b", 2)
cache.put("c", 3)

print(cache.get("a"))   # 1 — moves "a" to front
cache.put("d", 4)       # evicts "b" (least recently used)
print(cache.get("b"))   # None — was evicted
print(cache.get("c"))   # 3
print(cache.get("d"))   # 4
```

---

## Real World Applications

| System | How LRU is used |
|--------|----------------|
| Operating systems | Page replacement — evict least recently used memory pages |
| Web browsers | Cache recently visited pages and assets |
| CDNs | Keep frequently accessed content on edge servers near users |
| Databases | Buffer pool management — keep hot pages in memory |
| CPU hardware | L1/L2/L3 cache management |

---

## Design Decisions

**Sentinel nodes** — dummy head and tail nodes that never hold real data. Every real node always has a valid prev and next, eliminating all edge cases around empty lists or single-element operations.

**Private helpers** — `_remove` and `_insert` are pure linked list operations with no side effects on the map or size. Map and size management is handled explicitly by the callers (get and put), keeping responsibilities separated and the helpers reusable.

**Key stored on node** — when evicting the tail node, its key is needed to clean up the hash map entry. Storing the key on the node makes this O(1) without any reverse lookup.

---

## Study Context

This implementation was built while reading *Algorithms to Live By* by Brian Christian and Tom Griffiths (Chapter 4 — Caching), as part of a broader curriculum covering algorithms and data structures.

> *"Depend upon it there comes a time when for every addition of knowledge you forget something that you knew before. It is of the highest importance, therefore, not to have useless facts elbowing out the useful ones."* — Sherlock Holmes
