# 3Sum

- **Source**: LeetCode 15 / NeetCode 150
- **Links**: [LeetCode #15](https://leetcode.com/problems/3sum/) | [NeetCode](https://neetcode.io/problems/three-integer-sum)
- **Difficulty**: Medium
- **Pattern**: Two Pointers (Sorting / Two Pointers / Duplicate Skipping)

---

## Problem Description
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

### Example 1
```text
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1, 0, 1] and [-1, -1, 2].
```

### Example 2
```text
Input: nums = [0, 1, 1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```

### Constraints
- $3 \le \text{nums.length} \le 3000$
- $-10^5 \le \text{nums}[i] \le 10^5$

---

## Intuition & Approach
- **Brute Force**: Checking every triplet requires $\mathcal{O}(n^3)$ time, which will result in Time Limit Exceeded (TLE) for $n = 3000$.
- **Sorting + Two Pointers (Optimal)**:
  1. Sort the input array `nums`. Sorting allows us to easily use two pointers and skip duplicates.
  2. Iterate through each element $a = \text{nums}[i]$:
     - **Early termination**: If $a > 0$, no subsequent numbers can sum to zero since the array is sorted in ascending order.
     - **Skip outer duplicates**: If $i > 0$ and $\text{nums}[i] == \text{nums}[i-1]$, skip this iteration to avoid duplicate triplets.
  3. For each fixed $a$, initialize two pointers: `b = i + 1` (left) and `c = len(nums) - 1` (right):
     - If $\text{nums}[b] + \text{nums}[c] == -a$ (i.e. $a + b + c = 0$):
       - Append $[a, \text{nums}[b], \text{nums}[c]]$ to the result.
       - Increment `b` and skip duplicate values of `nums[b]` while `b < c`.
     - If $a + \text{nums}[b] + \text{nums}[c] > 0$: decrement `c` to decrease the total sum.
     - Otherwise: increment `b` to increase the total sum.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n^2)$ — Sorting takes $\mathcal{O}(n \log n)$. The outer loop runs at most $n$ times, and each inner two-pointer pass runs in $\mathcal{O}(n)$ time.
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space (excluding the output list), or $\mathcal{O}(n)$ for the sorting algorithm (Timsort in Python).

---

## Edge Cases Considered
- Less than 3 elements: returns `[]`.
- All elements identical and zero (`[0, 0, 0]`): returns `[[0, 0, 0]]`.
- No triplets summing to zero (e.g. all positive numbers): early termination triggers immediately.
- Multiple repeated values with several identical triplets: properly skipped via duplicate pointer checks.
