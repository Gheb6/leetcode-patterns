"""
Problem: Time Based Key-Value Store
LeetCode: 981 (https://leetcode.com/problems/time-based-key-value-store/)
NeetCode 150: Time Based Key-Value Store (https://neetcode.io/problems/time-based-key-value-store)
Difficulty: Medium
Pattern: Binary Search
"""

from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        new_list = [timestamp, value]
        self.store[key].append(new_list)        

    def get(self, key: str, timestamp: int) -> str:
        if not self.store[key]:
            return ""
        
        left = 0
        values = self.store[key]
        right = len(values) - 1
        best_res = ""
        while left <= right:
            mid = ( left + right ) // 2
            if values[mid][0] <= timestamp:
                best_res = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return best_res
