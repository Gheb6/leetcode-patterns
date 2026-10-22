# House Robber

- **Source**: LeetCode 198 / NeetCode 150
- **Links**: [LeetCode #198](https://leetcode.com/problems/house-robber/) | [NeetCode](https://neetcode.io/problems/house-robber)
- **Difficulty**: Medium
- **Pattern**: 1-D Dynamic Programming

---

## Problem Description
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight **without alerting the police**.

### Example 1
```text
Input: nums = [1, 2, 3, 1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

### Example 2
```text
Input: nums = [2, 7, 9, 3, 1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
```

### Constraints
- $1 \le \text{nums.length} \le 100$
- $0 \le \text{nums}[i] \le 400$

---

## Intuition & Approach
For each house $i$, we face a binary choice:
1. **Rob house $i$**: We cannot rob house $i - 1$, so the maximum loot is the value of house $i$ plus the optimal loot from up to house $i - 2$:
   $$\text{loot}_{\text{rob}} = \text{nums}[i] + dp[i - 2]$$
2. **Skip house $i$**: The maximum loot is simply the optimal loot from up to house $i - 1$:
   $$\text{loot}_{\text{skip}} = dp[i - 1]$$

### Recurrence Relation:
$$dp[i] = \max(dp[i - 1], dp[i - 2] + \text{nums}[i])$$

### Implementation Details:
1. **Base cases**:
   - If `len(nums) == 1`, return `nums[0]`.
   - `dp[0] = nums[0]`
   - `dp[1] = max(nums[0], nums[1])`
2. **Transition**:
   - For $i$ from $2$ to $\text{len(nums)} - 1$, populate `dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])`.
3. Return `dp[-1]`.

*(Note: Because `dp[i]` only depends on the previous two values `dp[i - 1]` and `dp[i - 2]`, this can also be optimized to $\mathcal{O}(1)$ space using two variables).*

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Single linear iteration across the array of length $n$.
- **Space Complexity**: $\mathcal{O}(n)$ — Array `dp` of size $n$ storing optimal subproblem solutions.

---

## Edge Cases Considered
- **Single house** (`nums = [5]`): Immediately returns `nums[0] = 5`.
- **Two houses** (`nums = [2, 1]` or `nums = [1, 2]`): Returns the maximum of the two houses.
- **Houses with 0 money**: Handled seamlessly by $\max$.
- **Alternating equal values** (e.g. `[2, 1, 1, 2]`): Computes optimal non-adjacent sum of 4 (`2 + 2`).
