# Distinct Subsequences

- **Source**: LeetCode 115 / NeetCode 150
- **Links**: [LeetCode #115](https://leetcode.com/problems/distinct-subsequences/) | [NeetCode](https://neetcode.io/problems/distinct-subsequences)
- **Difficulty**: Hard
- **Pattern**: 2-D Dynamic Programming

---

## Problem Description
Given two strings `s` and `t`, return the number of distinct **subsequences** of `s` which equals `t`.

---

## Strategy & Approach
We use a 2D dynamic programming grid `matrix[i][j]` representing the number of distinct subsequences of `s[:i]` that equal `t[:j]`:

1. **Base Case**:
   - `matrix[i][0] = 1` for all `0 <= i <= len(s)`: an empty string `t` can always be formed exactly once (by deleting all characters from `s`).
   - `matrix[0][j] = 0` for all `j > 0`: a non-empty `t` cannot be formed from an empty `s`.

2. **Transitions**:
   - If `s[i - 1] != t[j - 1]`: we cannot use `s[i - 1]`, so we carry forward the count without it:
     $$\text{matrix}[i][j] = \text{matrix}[i - 1][j]$$
   - If `s[i - 1] == t[j - 1]`: we have two choices — either use `s[i - 1]` to match `t[j - 1]`, or skip it:
     $$\text{matrix}[i][j] = \text{matrix}[i - 1][j - 1] + \text{matrix}[i - 1][j]$$

3. **Result**: `matrix[len(s)][len(t)]`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(m \cdot n)$ — where $m = \text{len}(s)$ and $n = \text{len}(t)$. Each cell of the $(m+1) \times (n+1)$ table is filled in $\mathcal{O}(1)$ time.
- **Space Complexity**: $\mathcal{O}(m \cdot n)$ — for the 2D DP matrix table.
