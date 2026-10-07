"""
Problem: Maximum Product Subarray
LeetCode: 152 (https://leetcode.com/problems/maximum-product-subarray/)
NeetCode 150: Maximum Product Subarray (https://neetcode.io/problems/maximum-product-subarray)
Difficulty: Medium
Pattern: 1-D Dynamic Programming
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n) where n is the length of nums.
        Space Complexity: O(1) auxiliary space using constant variables.
        """
        if not nums:
            return 0
        curr_max = nums[0]
        curr_min = nums[0]
        global_max = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                curr_max, curr_min = curr_min, curr_max
            curr_max = max(nums[i], curr_max * nums[i])
            curr_min = min(nums[i], curr_min * nums[i])
            global_max = max(global_max, curr_max)
        return global_max
