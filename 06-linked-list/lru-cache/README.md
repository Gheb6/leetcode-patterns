# LRU Cache

- **Source**: LeetCode 146 / NeetCode 150
- **Links**: [LeetCode #146](https://leetcode.com/problems/lru-cache/) | [NeetCode](https://neetcode.io/problems/lru-cache)
- **Difficulty**: Medium
- **Pattern**: Linked List / Hash Map (OrderedDict)

---

## Problem Description
Design a data structure that follows the constraints of a **Least Recently Used (LRU) cache**.

Implement the `LRUCache` class:
- `LRUCache(int capacity)`: Initialize the LRU cache with positive size `capacity`.
- `int get(int key)`: Return the value of the `key` if the key exists, otherwise return `-1`.
- `void put(int key, int value)`: Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, **evict** the least recently used key.

The functions `get` and `put` must each run in $\mathcal{O}(1)$ average time complexity.

---

## Strategy & Approach
An LRU Cache combines fast $\mathcal{O}(1)$ lookups with $\mathcal{O}(1)$ ordering updates. Using Python's `collections.OrderedDict` (which internally implements a doubly linked list + hash map):
1. **`get(key)`**:
   - If not found, return `-1`.
   - If found, move the key to the end using `cache.move_to_end(key)` to designate it as most recently used, then return its value.
2. **`put(key, value)`**:
   - If key already exists: update its value and call `move_to_end(key)`.
   - If new key: if `len(cache) >= capacity`, evict the oldest entry using `cache.popitem(last=False)`, then insert the new key.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(1)$ for both `get` and `put` operations.
- **Space Complexity**: $\mathcal{O}(\text{capacity})$ — to store at most `capacity` key-value pairs in the cache.
