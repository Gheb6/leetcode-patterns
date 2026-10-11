"""
Problem: Find Median from Data Stream
LeetCode: 295 (https://leetcode.com/problems/find-median-from-data-stream/)
NeetCode 150: Find Median in a Data Stream (https://neetcode.io/problems/find-median-in-a-data-stream)
Difficulty: Hard
Pattern: Heap / Priority Queue (Two Heaps)
"""

import heapq


class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []


    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, - num)
        value = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, value)
        if len(self.min_heap) > len(self.max_heap):
            value = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, - value)


    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return ( ( - self.max_heap[0]) + self.min_heap[0]) / 2
        else:
            return - self.max_heap[0]
