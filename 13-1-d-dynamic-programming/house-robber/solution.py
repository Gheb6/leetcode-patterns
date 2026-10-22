"""
Problem: House Robber
LeetCode: 198 (https://leetcode.com/problems/house-robber/)
NeetCode 150: House Robber (https://neetcode.io/problems/house-robber)
Difficulty: Medium
Pattern: 1-D Dynamic Programming
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()

    # Test cases
    assert sol.rob([1, 2, 3, 1]) == 4, "Failed on [1, 2, 3, 1]"
    assert sol.rob([2, 7, 9, 3, 1]) == 12, "Failed on [2, 7, 9, 3, 1]"
    assert sol.rob([5]) == 5, "Failed on single house [5]"
    assert sol.rob([2, 1]) == 2, "Failed on two houses [2, 1]"
    assert sol.rob([1, 2]) == 2, "Failed on two houses [1, 2]"
    assert sol.rob([2, 1, 1, 2]) == 4, "Failed on [2, 1, 1, 2]"

    print("All test cases for House Robber passed!")
