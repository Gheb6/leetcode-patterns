"""
Problem: Merge Intervals
LeetCode: 56 (https://leetcode.com/problems/merge-intervals/)
NeetCode 150: Merge Intervals (https://neetcode.io/problems/merge-intervals)
Difficulty: Medium
Pattern: Intervals
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            last_end = res[-1][1]
            if start <= last_end:
                res[-1][1] = max(last_end, end)
            else:
                res.append([start, end])
        return res
