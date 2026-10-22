"""
Problem: Find Minimum in Rotated Sorted Array
LeetCode: 153 (https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
NeetCode 150: Find Minimum in Rotated Sorted Array (https://neetcode.io/problems/find-minimum-in-rotated-sorted-array)
Difficulty: Medium
Pattern: Binary Search (Rotated Sorted Array / Inflection Point)
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


if __name__ == "__main__":
    sol = Solution()

    # Test cases
    assert sol.findMin([3, 4, 5, 1, 2]) == 1, "Failed on [3, 4, 5, 1, 2]"
    assert sol.findMin([4, 5, 6, 7, 0, 1, 2]) == 0, "Failed on [4, 5, 6, 7, 0, 1, 2]"
    assert sol.findMin([11, 13, 15, 17]) == 11, "Failed on unrotated array [11, 13, 15, 17]"
    assert sol.findMin([2, 1]) == 1, "Failed on [2, 1]"
    assert sol.findMin([1]) == 1, "Failed on single element [1]"

    print("All test cases for Find Minimum in Rotated Sorted Array passed!")
