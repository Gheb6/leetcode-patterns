"""
Problem: Search in Rotated Sorted Array
LeetCode: 33 (https://leetcode.com/problems/search-in-rotated-sorted-array/)
NeetCode 150: Search in Rotated Sorted Array (https://neetcode.io/problems/find-target-in-rotated-sorted-array)
Difficulty: Medium
Pattern: Binary Search (Rotated Sorted Array)
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: Target in right portion of rotated array
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 0) == 4, "Failed on [4, 5, 6, 7, 0, 1, 2], target = 0"

    # Test case 2: Target not in array
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 3) == -1, "Failed on [4, 5, 6, 7, 0, 1, 2], target = 3"

    # Test case 3: Single element not found
    assert sol.search([1], 0) == -1, "Failed on [1], target = 0"

    # Test case 4: Single element found
    assert sol.search([1], 1) == 0, "Failed on [1], target = 1"

    # Test case 5: Two elements rotated, target in second position
    assert sol.search([3, 1], 1) == 1, "Failed on [3, 1], target = 1"

    # Test case 6: Target at start of rotated array
    assert sol.search([5, 1, 3], 5) == 0, "Failed on [5, 1, 3], target = 5"

    print("All test cases for Search in Rotated Sorted Array passed!")
