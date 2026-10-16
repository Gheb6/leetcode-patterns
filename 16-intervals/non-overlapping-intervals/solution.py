"""
Problem: Non-overlapping Intervals
LeetCode: 435 (https://leetcode.com/problems/non-overlapping-intervals/)
NeetCode 150: Non-overlapping Intervals (https://neetcode.io/problems/non-overlapping-intervals)
Difficulty: Medium
Pattern: Intervals (Greedy)
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        counter = 0
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            if prev_end > start:
                    counter += 1
                    prev_end = min(end, prev_end)
            else:
                prev_end = end
        return counter
