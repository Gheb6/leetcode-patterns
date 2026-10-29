# Subsets

- **Source**: LeetCode 78 / NeetCode 150
- **Links**: [LeetCode #78](https://leetcode.com/problems/subsets/) | [NeetCode](https://neetcode.io/problems/subsets)
- **Difficulty**: Medium
- **Pattern**: Backtracking (Include / Exclude Decision Tree)

---

## Problem Description
Given an integer array `nums` of **unique** elements, return all possible **subsets** (the power set).

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

### Example 1
```text
Input: nums = [1, 2, 3]
Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
```

### Example 2
```text
Input: nums = [0]
Output: [[], [0]]
```

### Constraints
- $1 \le \text{nums.length} \le 10$
- $-10 \le \text{nums}[i] \le 10$
- All the numbers of `nums` are **unique**.

---

## Strategy & Approach
We model the generation of the power set as a **binary decision tree** of depth $n$:

At each index $i$ ($0 \le i < n$), we make two mutually exclusive decisions:
1. **Include `nums[i]`**:
   - Append `nums[i]` to `subset`.
   - Recursively call `dfs(i + 1)`.
2. **Exclude `nums[i]` (Backtrack)**:
   - Pop `nums[i]` from `subset` to restore the state.
   - Recursively call `dfs(i + 1)` without adding `nums[i]`.

### Base Case:
When $i \ge \text{len(nums)}$, we have made a choice for every element in the array. Append a copy of `subset` to `res` (`res.append(subset.copy())`) and return.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n \cdot 2^n)$ — There are $2^n$ leaves in the recursion tree (total subsets). Copying each subset into the output list takes up to $\mathcal{O}(n)$ time.
- **Space Complexity**: $\mathcal{O}(n)$ — The recursion call stack reaches depth at most $n$, and the temporary `subset` list holds at most $n$ elements (excluding the $\mathcal{O}(n \cdot 2^n)$ memory required to store the returned answer).

---

## Edge Cases Considered
- **Single element** (`nums = [0]`): Yields $2^1 = 2$ subsets (`[[], [0]]`).
- **Empty input array** (`nums = []`): Base case triggers immediately at index 0, producing `[[]]`.
- **Negative numbers**: Unaffected since all elements in `nums` are distinct.
