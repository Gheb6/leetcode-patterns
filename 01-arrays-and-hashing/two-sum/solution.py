"""
Problem: Two Sum
LeetCode: 1 (https://leetcode.com/problems/two-sum/)
NeetCode 150: Two Integer Sum (https://neetcode.io/problems/two-integer-sum)
Difficulty: Easy
Pattern: Arrays & Hashing (Hash Map / One-pass)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time Complexity: O(n) where n is the length of nums.
        Space Complexity: O(n) for the hash map storing seen complements.
        """
        my_dict = {}
        for i in range(len(nums)):
            if nums[i] in my_dict:
                return [my_dict[nums[i]], i]
            else:
                comp = target - nums[i]
                my_dict[comp] = i
