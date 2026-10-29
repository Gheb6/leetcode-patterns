# Combination Sum II

- **Source**: LeetCode 40 / NeetCode 150
- **Links**: [LeetCode #40](https://leetcode.com/problems/combination-sum-ii/) | [NeetCode](https://neetcode.io/problems/combination-target-sum-ii)
- **Difficulty**: Medium
- **Pattern**: Backtracking (Pruning & Duplicate Handling)

---

## Problem Description
Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note**: The solution set must not contain duplicate combinations.

### Example 1
```text
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
```

### Example 2
```text
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
```

### Constraints
- $1 \le \text{candidates.length} \le 100$
- $1 \le \text{candidates}[i] \le 50$
- $1 \le \text{target} \le 30$

---

## Strategy & Approach
Unlike *Combination Sum* (LeetCode 39), here:
1. Each element may only be chosen **once** per combination (advance index to `i + 1`).
2. The input array `candidates` can contain **duplicate numbers**, but the solution set must not contain duplicate combinations.

### Key Techniques:
1. **Initial Sorting**:
   - `candidates.sort()` groups identical elements together and ensures the array is non-decreasing.
2. **Early Pruning**:
   - Inside the loop starting at `start`: if `current_sum + candidates[i] > target`, we can immediately `break` because all subsequent candidates are $\ge \text{candidates}[i]$ and will also exceed `target`.
3. **Duplicate Combination Pruning**:
   - If `i > start and candidates[i] == candidates[i - 1]`, we `continue` (skip this branch). Picking the same value as the first choice at the current depth generates identical combinations to those already explored by the previous branch.
4. **Advance Index**:
   - Recurse with `dfs(i + 1, current_sum + candidates[i])` to guarantee each element index is visited at most once.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(2^n)$ in the worst case (where $n = \text{len(candidates)}$), because every element can either be included or excluded. Sorting takes $\mathcal{O}(n \log n)$ which is dominated by the backtracking tree.
- **Space Complexity**: $\mathcal{O}(n)$ — The recursion call stack reaches depth at most $n$, and the temporary combination list `subset` holds at most $n$ elements (excluding the space for the returned output).

---

## Edge Cases Considered
- **Duplicate candidates producing identical combinations**: Prevented by `i > start and candidates[i] == candidates[i - 1]`.
- **Target smaller than all elements**: The loop condition `current_sum + candidates[i] > target` breaks on the first candidate, returning `[]`.
- **All elements required to hit target**: Correctly explored down to depth $n$.

