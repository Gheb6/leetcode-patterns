"""
Problem: Binary Search
LeetCode: 704 (https://leetcode.com/problems/binary-search/)
NeetCode 150: Binary Search (https://neetcode.io/problems/binary-search)
Difficulty: Easy
Pattern: Binary Search
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Searches for target in a sorted ascending array using standard binary search.
        
        Time Complexity: O(log N) where N is the number of elements.
        Space Complexity: O(1) constant extra space.
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2  # Prevents integer overflow in static-typed languages
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


if __name__ == "__main__":
    sol = Solution()
    # Test cases
    assert sol.search([-1, 0, 3, 5, 9, 12], 9) == 4, "Failed finding 9"
    assert sol.search([-1, 0, 3, 5, 9, 12], 2) == -1, "Failed when target is absent"
    assert sol.search([5], 5) == 0, "Failed on single-element match"
    assert sol.search([5], -5) == -1, "Failed on single-element non-match"
    print("All test cases for Binary Search passed!")
