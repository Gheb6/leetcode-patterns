"""
Problem: Koko Eating Bananas
LeetCode: 875 (https://leetcode.com/problems/koko-eating-bananas/)
NeetCode 150: Eating Bananas (https://neetcode.io/problems/eating-bananas)
Difficulty: Medium
Pattern: Binary Search on the Answer Space (Predicate / Feasibility Search)
"""

import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Finds the minimum integer speed k such that Koko can eat all bananas within h hours.
        
        Search space: k in [1, max(piles)]
        Monotonic condition: if speed k is sufficient, all speeds > k are also sufficient.
        
        Time Complexity: O(N * log M) where N = len(piles) and M = max(piles).
        Space Complexity: O(1) extra space.
        """
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            k = left + (right - left) // 2
            hours_needed = sum(math.ceil(p / k) for p in piles)

            if hours_needed <= h:
                res = k
                right = k - 1  # Try to find a smaller valid speed
            else:
                left = k + 1   # Speed too slow, must increase k

        return res


if __name__ == "__main__":
    sol = Solution()
    # Test cases
    assert sol.minEatingSpeed([3, 6, 7, 11], 8) == 4, "Failed on [3, 6, 7, 11], h=8"
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30, "Failed on [30, 11, 23, 4, 20], h=5"
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23, "Failed on [30, 11, 23, 4, 20], h=6"
    print("All test cases for Koko Eating Bananas passed!")
