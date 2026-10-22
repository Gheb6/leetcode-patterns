# House Robber II

- **Source**: LeetCode 213 / NeetCode 150
- **Links**: [LeetCode #213](https://leetcode.com/problems/house-robber-ii/) | [NeetCode](https://neetcode.io/problems/house-robber-ii)
- **Difficulty**: Medium
- **Pattern**: 1-D Dynamic Programming (Circular Array)

---

## Problem Description
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are **arranged in a circle**. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight **without alerting the police**.

### Example 1
```text
Input: nums = [2, 3, 2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
```

### Example 2
```text
Input: nums = [1, 2, 3, 1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

### Example 3
```text
Input: nums = [1, 2, 3]
Output: 3
```

### Constraints
- $1 \le \text{nums.length} \le 100$
- $0 \le \text{nums}[i] \le 1000$

---

## Intuition & Approach
The circular arrangement introduces a single new restriction compared to [House Robber](../house-robber/):
- **House 0 and House $n - 1$ are adjacent**, meaning we cannot rob both.

This mutual exclusivity allows us to break the circular problem down into **two linear House Robber subproblems**:
1. **Exclude the last house**: Rob optimally within `nums[:-1]` (houses $0$ to $n - 2$).
2. **Exclude the first house**: Rob optimally within `nums[1:]` (houses $1$ to $n - 1$).

The global optimal answer is simply:
$$\text{ans} = \max(\text{rob}(nums[:-1]), \text{rob}(nums[1:]))$$

### Base Case:
- If `len(nums) == 1`, return `nums[0]`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — We run the standard linear DP twice, each taking $\mathcal{O}(n)$ operations, resulting in $\mathcal{O}(n)$ total time.
- **Space Complexity**: $\mathcal{O}(n)$ — For slicing the lists and allocating the DP arrays of length $n - 1$.

---

## Edge Cases Considered
- **Single house** (`nums = [1]`): Explicit base case returns `nums[0] = 1`.
- **Two houses** (`nums = [1, 2]`): Slices produce single-element lists, correctly returning `max(1, 2) = 2`.
- **Three houses with equal ends** (`nums = [2, 3, 2]`): Prevents taking both ends, correctly returning `3`.
- **All houses have 0 value**: Correctly returns `0`.
