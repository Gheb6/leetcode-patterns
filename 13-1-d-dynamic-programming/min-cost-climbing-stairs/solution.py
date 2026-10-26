"""
Problem: Min Cost Climbing Stairs
LeetCode: 746 (https://leetcode.com/problems/min-cost-climbing-stairs/)
NeetCode 150: Min Cost Climbing Stairs (https://neetcode.io/problems/min-cost-climbing-stairs)
Difficulty: Easy
Pattern: 1-D Dynamic Programming (State Transition / Space Optimized)
"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1:
            return cost[0]
        elif n == 2:
            return min(cost[0], cost[1])
        prev = cost[0]
        curr = cost[1]
        new_cost = 0
        for i in range(2, n):
            new_cost = min(prev, curr) + cost[i]
            prev = curr
            curr = new_cost
        return min(new_cost, prev)


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: [10, 15, 20] -> 15 (start on index 1, pay 15, reach top)
    assert sol.minCostClimbingStairs([10, 15, 20]) == 15, "Failed on [10, 15, 20]"

    # Test case 2: [1, 100, 1, 1, 1, 100, 1, 1, 100, 1] -> 6
    assert sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6, "Failed on test case 2"

    # Test case 3: Minimal length 2
    assert sol.minCostClimbingStairs([10, 15]) == 10, "Failed on [10, 15]"

    # Test case 4: All zeros
    assert sol.minCostClimbingStairs([0, 0, 0, 0]) == 0, "Failed on all zeros"

    print("All test cases for Min Cost Climbing Stairs passed!")
