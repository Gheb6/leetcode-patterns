"""
Problem: Daily Temperatures
LeetCode: 739 (https://leetcode.com/problems/daily-temperatures/)
NeetCode 150: Daily Temperatures (https://neetcode.io/problems/daily-temperatures)
Difficulty: Medium
Pattern: Stack (Monotonic Decreasing Stack)
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        my_stack = []
        res = [0] * len(temperatures)
        for index, temperature in enumerate(temperatures):
            while my_stack and temperature > my_stack[-1][1]:
                prev_idx, prev_temp = my_stack.pop()
                res[prev_idx] = index - prev_idx
            my_stack.append((index, temperature))
        return res


if __name__ == "__main__":
    sol = Solution()
    # Test cases
    assert sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0], "Failed on standard case"
    assert sol.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0], "Failed on strictly increasing"
    assert sol.dailyTemperatures([30, 60, 90]) == [1, 1, 0], "Failed on increasing case"
    assert sol.dailyTemperatures([90, 80, 70]) == [0, 0, 0], "Failed on strictly decreasing"
    assert sol.dailyTemperatures([]) == [], "Failed on empty array"
    print("All test cases for Daily Temperatures passed!")
