# Best Time to Buy and Sell Stock

- **Source**: LeetCode 121 / NeetCode 150
- **Links**: [LeetCode #121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [NeetCode](https://neetcode.io/problems/buy-and-sell-crypto)
- **Difficulty**: Easy
- **Pattern**: Sliding Window / Two Pointers (Greedy)

---

## Problem Description
You are given an array `prices` where `prices[i]` is the price of a given stock on the $i^{\text{th}}$ day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

---

## Strategy & Approach
Use a **single pass (sliding window / greedy)** tracking the lowest buying price seen so far:
1. Initialize `min_price = prices[0]` and `gain = 0`.
2. Iterate through each price `prices[i]`:
   - If `prices[i] < min_price`, update `min_price = prices[i]` (found a cheaper buying point).
   - Otherwise, calculate potential profit `prices[i] - min_price` and update `gain = max(gain, tmp_gain)`.
3. Return `gain`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — We iterate through the `prices` array in a single pass.
- **Space Complexity**: $\mathcal{O}(1)$ — Only scalar variables (`min_price`, `gain`, `tmp_gain`) are used.

---

## Edge Cases Considered
- Monotonically decreasing prices (no profit possible, returns `0`).
- Single day price array (length 1: cannot sell in the future, returns `0`).
- Best selling day occurring before the lowest price day.
