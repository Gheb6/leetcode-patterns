"""
Problem: Subsets II
LeetCode: 90 (https://leetcode.com/problems/subsets-ii/)
NeetCode 150: Subsets II (https://neetcode.io/problems/subsets-ii)
Difficulty: Medium
Pattern: Backtracking / Cascading
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        start_idx = 0
        previous_dim = len(res)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                start_idx = end_idx
            else:
                start_idx = 0
            end_idx = len(res)
            for j in range(start_idx, end_idx):
                res.append(res[j] + [nums[i]])            
        return res
