# Combination Sum

- **Source**: LeetCode 39 / NeetCode 150
- **Links**: [LeetCode #39](https://leetcode.com/problems/combination-sum/) | [NeetCode](https://neetcode.io/problems/combination-target-sum)
- **Difficulty**: Medium
- **Pattern**: Backtracking (Unbounded Knapsack / Decision Tree)

---

## Problem Description
Given an array of **distinct** integers `nums` (or `candidates`) and a target integer `target`, return a list of all **unique combinations** of `nums` where the chosen numbers sum to `target`. You may return the combinations in **any order**.

The **same** number may be chosen from `nums` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to `target` is less than 150 combinations for the given input.

### Example 1
```text
Input: nums = [2, 3, 6, 7], target = 7
Output: [[2, 2, 3], [7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
```

### Example 2
```text
Input: nums = [2, 3, 5], target = 8
Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
```

### Example 3
```text
Input: nums = [2], target = 1
Output: []
```

### Constraints
- $1 \le \text{nums.length} \le 30$
- $2 \le \text{nums}[i] \le 40$
- All elements of `nums` are **distinct**.
- $1 \le \text{target} \le 40$

---

## Strategy & Approach
We model the problem as a **backtracking decision tree** where each element can be chosen multiple times:

At each state $(i, \text{current\_sum})$:
1. **Pruning & Base Cases**:
   - If $\text{current\_sum} == \text{target}$: Valid combination found. Append a copy of `subset` to `res` and return.
   - If $\text{current\_sum} > \text{target}$: Exceeded target; prune this branch.
   - If $i \ge \text{len(nums)}$: Out of candidates; return.
2. **Choice 1: Include `nums[i]` (Reuse Allowed)**:
   - Append `nums[i]` to `subset`.
   - Update `current_sum += nums[i]`.
   - Recurse on the **same index** $i$: `dfs(i, current_sum)`.
   - Backtrack: `subset.pop()`, `current_sum -= nums[i]`.
3. **Choice 2: Exclude `nums[i]` (Advance to Next Candidate)**:
   - Recurse on the next index: `dfs(i + 1, current_sum)`.

This guarantees that each combination is generated in a canonical non-decreasing order of candidate indices, eliminating duplicate permutations naturally without sorting or hash sets.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(2^{T/M})$ where $T = \text{target}$ and $M = \min(\text{nums})$. The maximum depth of the recursion tree is $T/M$ (achieved when repeatedly adding the smallest candidate), yielding an upper bound on operations of $\mathcal{O}(2^{T/M})$.
- **Space Complexity**: $\mathcal{O}(T/M)$ — Maximum recursion stack depth and size of the current combination list `subset`.

---

## Edge Cases Considered
- **Target smaller than smallest candidate** (`nums = [2], target = 1`): Early pruning returns `[]`.
- **Target equals single element** (e.g. `7` in `[2, 3, 6, 7]`): Accurately captured as `[7]`.
- **Multiple candidate reuses** (e.g. `[2, 2, 2, 2]` for target 8): Handled correctly through `dfs(i, ...)`.
