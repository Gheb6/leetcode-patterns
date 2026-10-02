"""
Problem: Contains Duplicate
LeetCode: 217 (https://leetcode.com/problems/contains-duplicate/)
NeetCode 150: Duplicate Integer (https://neetcode.io/problems/duplicate-integer)
Difficulty: Easy
Pattern: Arrays & Hashing (Hash Set)
"""

from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Determines if any value appears at least twice in the array.
        
        Time Complexity: O(N) where N is the length of nums (single pass lookup/insertion).
        Space Complexity: O(N) to store seen elements in the hash set.
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    sol = Solution()
    # Test cases
    assert sol.hasDuplicate([1, 2, 3, 1]) is True, "Failed on [1, 2, 3, 1]"
    assert sol.hasDuplicate([1, 2, 3, 4]) is False, "Failed on [1, 2, 3, 4]"
    assert sol.hasDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True, "Failed on multiple duplicates"
    assert sol.hasDuplicate([]) is False, "Failed on empty array"
    print("All test cases for Contains Duplicate passed!")
