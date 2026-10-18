"""
Problem: Container With Most Water
LeetCode: 11 (https://leetcode.com/problems/container-with-most-water/)
NeetCode 150: Max Water Container (https://neetcode.io/problems/max-water-container)
Difficulty: Medium
Pattern: Two Pointers (Greedy / Opposite Ends)
"""

from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        best_area = 0
        while left < right:
            area = (right - left) * min(heights[left], heights[right]) 
            best_area = max(best_area, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return best_area


if __name__ == "__main__":
    sol = Solution()
    # Test cases
    assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49, "Failed on [1, 8, 6, 2, 5, 4, 8, 3, 7]"
    assert sol.maxArea([1, 1]) == 1, "Failed on [1, 1]"
    assert sol.maxArea([4, 3, 2, 1, 4]) == 16, "Failed on [4, 3, 2, 1, 4]"
    assert sol.maxArea([1, 2, 1]) == 2, "Failed on [1, 2, 1]"
    assert sol.maxArea([1, 2, 4, 3]) == 4, "Failed on [1, 2, 4, 3]"
    print("All test cases for Container With Most Water passed!")
