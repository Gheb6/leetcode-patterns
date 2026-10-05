"""
Problem: Best Time to Buy and Sell Stock
LeetCode: 121 (https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
NeetCode 150: Best Time to Buy and Sell Stock (https://neetcode.io/problems/buy-and-sell-crypto)
Difficulty: Easy
Pattern: Sliding Window / Two Pointers
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        gain = 0
        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            tmp_gain = prices[i] - min_price
            if tmp_gain > gain:
                gain = tmp_gain
        return gain          