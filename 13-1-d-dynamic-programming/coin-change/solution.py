"""
Problem: Coin Change
LeetCode: 322 (https://leetcode.com/problems/coin-change/)
NeetCode 150: Coin Change (https://neetcode.io/problems/coin-change)
Difficulty: Medium
Pattern: 1-D Dynamic Programming (Bottom-Up)
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], 1 + dp[i - c])
                    
        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == "__main__":
    sol = Solution()

    # Test cases
    assert sol.coinChange([1, 2, 5], 11) == 3, "Failed on [1, 2, 5] amount 11"
    assert sol.coinChange([2], 3) == -1, "Failed on [2] amount 3"
    assert sol.coinChange([1], 0) == 0, "Failed on [1] amount 0"
    assert sol.coinChange([2, 5, 10, 1], 27) == 4, "Failed on [2, 5, 10, 1] amount 27"
    assert sol.coinChange([186, 419, 83, 408], 6249) == 20, "Failed on large inputs"

    print("All test cases for Coin Change passed!")
