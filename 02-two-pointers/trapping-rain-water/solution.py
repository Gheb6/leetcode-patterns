"""
Problem: Trapping Rain Water
LeetCode: 42 (https://leetcode.com/problems/trapping-rain-water/)
NeetCode 150: Trapping Rain Water (https://neetcode.io/problems/trapping-rain-water)
Difficulty: Hard
Pattern: Two Pointers (Opposite Ends / Boundary Maxima)
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        area = 0
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                area += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                area += right_max - height[right]
        return area


if __name__ == "__main__":
    sol = Solution()
    # Test cases
    assert sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6, "Failed on [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]"
    assert sol.trap([4, 2, 0, 3, 2, 5]) == 9, "Failed on [4, 2, 0, 3, 2, 5]"
    assert sol.trap([1]) == 0, "Failed on single element"
    assert sol.trap([1, 2]) == 0, "Failed on two elements"
    assert sol.trap([3, 0, 2, 0, 4]) == 7, "Failed on [3, 0, 2, 0, 4]"
    print("All test cases for Trapping Rain Water passed!")
