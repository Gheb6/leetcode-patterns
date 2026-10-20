"""
Problem: Largest Rectangle in Histogram
LeetCode: 84 (https://leetcode.com/problems/largest-rectangle-in-histogram/)
NeetCode 150: Largest Rectangle In Histogram (https://neetcode.io/problems/largest-rectangle-in-histogram)
Difficulty: Hard
Pattern: Stack (Monotonic Increasing Stack)
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        my_stack = []
        for i, h in enumerate(heights):
            start = i
            while my_stack and my_stack[-1][1] > h:
                pop_i, pop_h = my_stack.pop()
                area = pop_h * (i - pop_i)
                max_area = max(max_area, area)
                start = pop_i
            my_stack.append((start, h))
        for start_i, h in my_stack:
            max_area = max(max_area, h * (len(heights) - start_i))
        return max_area


if __name__ == "__main__":
    sol = Solution()
    # Test cases
    assert sol.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10, "Failed on [2, 1, 5, 6, 2, 3]"
    assert sol.largestRectangleArea([2, 4]) == 4, "Failed on [2, 4]"
    assert sol.largestRectangleArea([1]) == 1, "Failed on single element"
    assert sol.largestRectangleArea([2, 1, 2]) == 3, "Failed on [2, 1, 2]"
    assert sol.largestRectangleArea([0]) == 0, "Failed on [0]"
    assert sol.largestRectangleArea([]) == 0, "Failed on empty array"
    print("All test cases for Largest Rectangle in Histogram passed!")
