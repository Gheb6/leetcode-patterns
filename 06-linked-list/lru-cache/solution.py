"""
Problem: LRU Cache
LeetCode: 146 (https://leetcode.com/problems/lru-cache/)
NeetCode 150: LRU Cache (https://neetcode.io/problems/lru-cache)
Difficulty: Medium
Pattern: Linked List / Hash Map (OrderedDict)
"""

from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = value
