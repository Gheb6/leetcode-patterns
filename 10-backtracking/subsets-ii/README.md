# Subsets II

- **Source**: LeetCode 90 / NeetCode 150
- **Links**: [LeetCode #90](https://leetcode.com/problems/subsets-ii/) | [NeetCode](https://neetcode.io/problems/subsets-ii)
- **Difficulty**: Medium
- **Pattern**: Backtracking / Cascading

---

## Problem Description
Given an integer array `nums` that may contain duplicates, return all possible **subsets** (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

---

## Strategy & Approach
Iterative cascading generation with duplicate pruning:
1. **Sort `nums`**: ensures identical elements are adjacent.
2. Initialize `res = [[]]`.
3. For each element `nums[i]`:
   - If `nums[i] == nums[i - 1]`, only append `nums[i]` to subsets created in the previous step (from `start_idx = previous end_idx`). Appending to older subsets would recreate duplicates.
   - If `nums[i]` is distinct, append `nums[i]` to all existing subsets (`start_idx = 0`).
4. Update `end_idx = len(res)` and repeat.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n \cdot 2^n)$ — Sorting takes $\mathcal{O}(n \log n)$. In the worst case (all unique elements), there are $2^n$ subsets, each taking up to $\mathcal{O}(n)$ time to copy.
- **Space Complexity**: $\mathcal{O}(n \cdot 2^n)$ — To store all $2^n$ subsets in the output list `res`.
