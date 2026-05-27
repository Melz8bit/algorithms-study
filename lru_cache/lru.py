class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class lru_cache:
    def __init__(self, capacity):
        # Create empty head and tail nodes
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.lru_map = {}  # Create an empty map; sentinel nodes aren't counted

        self.capacity = capacity
        self.size = 0  # Amount of items currently in the LRU map

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert(self, node):
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
        # Create new node
        node = Node(key, value)

        # Check if node exists in cache
        if key in self.lru_map:
            node = self.lru_map[key]
            node.value = value
            self._remove(node)
            self._insert(node)

        # LRU map is full
        elif self.size == self.capacity:
            # Remove last node
            last_node = self.tail.prev
            self._remove(last_node)

            # Insert new node at the start
            self._insert(node)

            # Update lru_map
            del self.lru_map[last_node.key]
            self.lru_map[key] = node

        # LRU map still has space
        else:
            self._insert(node)
            self.lru_map[key] = node
            self.size += 1


## Test
cache = lru_cache(3)
cache.put("a", 1)
cache.put("b", 2)
cache.put("c", 3)
print(cache.get("a"))  # 1, moves a to front
cache.put("d", 4)  # evicts b (LRU)
print(cache.get("b"))  # None
print(cache.get("c"))  # 3
print(cache.get("d"))  # 4
