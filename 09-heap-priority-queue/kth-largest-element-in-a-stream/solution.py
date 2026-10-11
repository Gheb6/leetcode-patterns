"""
Problem: Kth Largest Element in a Stream
LeetCode: 703 (https://leetcode.com/problems/kth-largest-element-in-a-stream/)
NeetCode 150: Kth Largest Element in a Stream (https://neetcode.io/problems/kth-largest-element-in-a-stream)
Difficulty: Easy
Pattern: Heap / Priority Queue (Min-Heap of Size K)
"""

import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
