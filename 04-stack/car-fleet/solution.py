"""
Problem: Car Fleet
LeetCode: 853 (https://leetcode.com/problems/car-fleet/)
NeetCode 150: Car Fleet (https://neetcode.io/problems/car-fleet)
Difficulty: Medium
Pattern: Stack (Sorting / Monotonic Stack)
"""

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        my_stack = []      
        for p in pair:
            time = (target - p[0]) / p[1]
            my_stack.append(time)
            if len(my_stack) >= 2 and my_stack[-1] <= my_stack[-2]:
                my_stack.pop()
        return len(my_stack)


if __name__ == "__main__":
    sol = Solution()
    # Test cases
    assert sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3, "Failed on [10, 8, 0, 5, 3]"
    assert sol.carFleet(10, [3], [3]) == 1, "Failed on single car"
    assert sol.carFleet(100, [0, 2, 4], [4, 2, 1]) == 1, "Failed on all catching up"
    assert sol.carFleet(10, [6, 8], [3, 2]) == 2, "Failed on two non-merging cars"
    print("All test cases for Car Fleet passed!")
