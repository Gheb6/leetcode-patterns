"""
Problem: K Closest Points to Origin
LeetCode: 973 (https://leetcode.com/problems/k-closest-points-to-origin/)
NeetCode 150: K Closest Points to Origin (https://neetcode.io/problems/k-closest-points-to-origin)
Difficulty: Medium
Pattern: Heap / Priority Queue (Max-Heap)
"""

from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Time Complexity: O(n log k) where n is the number of points and k is the heap capacity.
        Space Complexity: O(k) to store the heap elements.
        """
        min_heap = []
        for i in range(len(points)):
            length = - ( points[i][0] ** 2 + points[i][1] ** 2 )
            my_tuple = [length, points[i]]
            if len(min_heap) < k:
                heapq.heappush(min_heap, my_tuple)
            else:
                if (min_heap[0][0]) < length:
                    # heapq.heappop(min_heap)
                    # heapq.heappush(min_heap, my_tuple)
                    # alternatively
                    heapq.heappushpop(min_heap, my_tuple)
        return [point for dist, point in min_heap]
