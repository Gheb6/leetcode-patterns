"""
Problem: House Robber II
LeetCode: 213 (https://leetcode.com/problems/house-robber-ii/)
NeetCode 150: House Robber II (https://neetcode.io/problems/house-robber-ii)
Difficulty: Medium
Pattern: 1-D Dynamic Programming (Circular Array)
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def Robber_house(nums: List[int]) -> int:
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            dp = [0] * (len(nums))
            dp[0] = nums[0]
            dp[1] = max(dp[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            return dp[-1]
            
        res_1 = Robber_house(nums[:-1])
        res_2 = Robber_house(nums[1:])
        return max(res_1, res_2)


if __name__ == "__main__":
    sol = Solution()

    # Test cases
    assert sol.rob([2, 3, 2]) == 3, "Failed on [2, 3, 2]"
    assert sol.rob([1, 2, 3, 1]) == 4, "Failed on [1, 2, 3, 1]"
    assert sol.rob([1, 2, 3]) == 3, "Failed on [1, 2, 3]"
    assert sol.rob([1]) == 1, "Failed on single house [1]"
    assert sol.rob([0]) == 0, "Failed on [0]"
    assert sol.rob([200, 3, 140, 20, 10]) == 340, "Failed on [200, 3, 140, 20, 10]"

    print("All test cases for House Robber II passed!")
