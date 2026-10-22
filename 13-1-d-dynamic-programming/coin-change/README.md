# Coin Change

- **Source**: LeetCode 322 / NeetCode 150
- **Links**: [LeetCode #322](https://leetcode.com/problems/coin-change/) | [NeetCode](https://neetcode.io/problems/coin-change)
- **Difficulty**: Medium
- **Pattern**: 1-D Dynamic Programming (Bottom-Up)

---

## Problem Description
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the **fewest number of coins** that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

### Example 1
```text
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1 (3 coins)
```

### Example 2
```text
Input: coins = [2], amount = 3
Output: -1
```

### Example 3
```text
Input: coins = [1], amount = 0
Output: 0
```

### Constraints
- $1 \le \text{coins.length} \le 12$
- $1 \le \text{coins}[i] \le 2^{31} - 1$
- $0 \le \text{amount} \le 10^4$

---

## Intuition & Approach
A greedy approach (choosing the largest coin denomination first) fails for general coin systems (e.g. `coins = [1, 3, 4, 5]`, `amount = 7`: greedy gives $5 + 1 + 1 = 3$ coins, while optimal is $4 + 3 = 2$ coins). Therefore, we use **Dynamic Programming**:

### Recurrence Relation:
Let $dp[i]$ be the minimum number of coins needed to make amount $i$.
For each sub-amount $i$ from $1$ to `amount`:
$$dp[i] = \min_{c \in \text{coins}, i \ge c} (dp[i], 1 + dp[i - c])$$

### Algorithm (Bottom-Up DP):
1. **DP Array Initialization**:
   - Initialize an array `dp` of size `amount + 1` filled with $\infty$ (`float('inf')`).
   - Base case: `dp[0] = 0` (zero coins needed to form amount $0$).
2. **State Transitions**:
   - For each target value $i$ from $1$ to `amount`:
     - Iterate through each coin denomination $c$ in `coins`:
       - If $i \ge c$, update `dp[i] = min(dp[i], 1 + dp[i - c])`.
3. **Result**:
   - If `dp[amount]` is still $\infty$, the amount is unreachable; return `-1`.
   - Otherwise, return `dp[amount]`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(\text{amount} \cdot n)$ — Where $n = \text{len(coins)}$. For each value from $1$ to `amount`, we iterate over all $n$ coin denominations.
- **Space Complexity**: $\mathcal{O}(\text{amount})$ — Array `dp` of size `amount + 1`.

---

## Edge Cases Considered
- **Zero amount** (`amount = 0`): Base case `dp[0] = 0` returns immediately without running the outer loop.
- **Impossible amounts** (e.g. `coins = [2], amount = 3`): `dp[amount]` remains `float('inf')`, returning `-1`.
- **Large coin denomination exceeding amount** (e.g. `coins = [5], amount = 3`): Condition `i >= c` skips transitions, correctly returning `-1`.
- **Single denomination matching amount**: Returns `1`.
