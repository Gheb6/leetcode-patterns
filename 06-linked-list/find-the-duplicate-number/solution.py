"""
Problem: Find the Duplicate Number
LeetCode: 287 (https://leetcode.com/problems/find-the-duplicate-number/)
NeetCode 150: Find the Duplicate Number (https://neetcode.io/problems/find-duplicate-integer)
Difficulty: Medium
Pattern: Linked List (Floyd's Tortoise and Hare / Cycle Detection)
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        fast = nums[fast]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: Standard cycle
    assert sol.findDuplicate([1, 3, 4, 2, 2]) == 2, "Failed on [1, 3, 4, 2, 2]"

    # Test case 2: Duplicate at the beginning/middle
    assert sol.findDuplicate([3, 1, 3, 4, 2]) == 3, "Failed on [3, 1, 3, 4, 2]"

    # Test case 3: All elements identical
    assert sol.findDuplicate([3, 3, 3, 3, 3]) == 3, "Failed on [3, 3, 3, 3, 3]"

    # Test case 4: Two-element array
    assert sol.findDuplicate([1, 1]) == 1, "Failed on [1, 1]"

    print("All test cases for Find the Duplicate Number passed!")
