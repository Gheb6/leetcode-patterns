# Happy Number (Non-Cyclical Number)

- **Source**: LeetCode 202 / NeetCode 150
- **Links**: [LeetCode #202](https://leetcode.com/problems/happy-number/) | [NeetCode](https://neetcode.io/problems/non-cyclical-number)
- **Difficulty**: Easy
- **Pattern**: Math & Geometry (Cycle Detection / Hash Set)

---

## Problem Description
A **happy number** is a number defined by the following process:
- Replace the number with the sum of the squares of its digits.
- Repeat the process until the number equals 1 (happy), or it loops endlessly in a cycle that does not include 1 (unhappy).

Given an integer `n`, return `true` if it is a happy number, and `false` if not.

---

## Strategy & Approach
- Compute the sum of the squared digits of `n` using modulo `% 10` and integer division `// 10`.
- If the sum equals 1, the number is happy (`True`).
- Use a `seen` set to track intermediate sums:
  - If a sum has already been seen, a cycle is detected, meaning it will never reach 1 (`False`).
  - Otherwise, add the sum to `seen` and repeat with the new value.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(\log n)$ — Calculating the sum of squares of digits takes time proportional to the number of digits ($\mathcal{O}(\log_{10} n)$). Once the number falls below 243, it enters a small, bounded sequence.
- **Space Complexity**: $\mathcal{O}(\log n)$ / $\mathcal{O}(1)$ — Storing intermediate numbers in the `seen` hash set (the set size is strictly bounded by the small cycle range).
