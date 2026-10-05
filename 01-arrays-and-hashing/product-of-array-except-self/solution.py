"""
Problem: Product of Array Except Self
LeetCode: 238 (https://leetcode.com/problems/product-of-array-except-self/)
NeetCode 150: Products of Array Discluding Self (https://neetcode.io/problems/products-of-array-discluding-self)
Difficulty: Medium
Pattern: Arrays & Hashing (Prefix & Suffix Products)
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Time Complexity: O(n) where n is the length of nums.
        Space Complexity: O(1) auxiliary space (output array left does not count towards space complexity).
        """
        left = [1] * len(nums)
        partial = 1
        for i in range(len(nums)):
            if i == 0:
                left[i] = 1 
            else:
                partial = nums[i - 1] * partial
                left[i] = partial
        right_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums):
                continue 
            else:
                left[i] = right_prod * left[i]
                right_prod = right_prod * nums[i]
        return left
