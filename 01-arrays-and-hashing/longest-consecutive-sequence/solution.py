"""
Problem: Longest Consecutive Sequence
LeetCode: 128 (https://leetcode.com/problems/longest-consecutive-sequence/)
NeetCode 150: Longest Consecutive Sequence (https://neetcode.io/problems/longest-consecutive-sequence)
Difficulty: Medium
Pattern: Arrays & Hashing (Hash Set / Sequence Building)
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        my_set = set(nums)
        best_res = 0
        for num in my_set:
            if ( num - 1 ) not in my_set:
                res = 0
                while ( num + res ) in my_set:
                    res += 1
                if res > best_res:
                    best_res = res
                res = 1
        return best_res


if __name__ == "__main__":
    sol = Solution()
    # Test cases
    assert sol.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4, "Failed on [100, 4, 200, 1, 3, 2]"
    assert sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9, "Failed on [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]"
    assert sol.longestConsecutive([1, 0, 1, 2]) == 3, "Failed on [1, 0, 1, 2]"
    assert sol.longestConsecutive([]) == 0, "Failed on empty array"
    assert sol.longestConsecutive([7]) == 1, "Failed on single element"
    print("All test cases for Longest Consecutive Sequence passed!")
