# Climbing Stairs

- **Source**: LeetCode 70 / NeetCode 150
- **Links**: [LeetCode #70](https://leetcode.com/problems/climbing-stairs/) | [NeetCode](https://neetcode.io/problems/climbing-stairs)
- **Difficulty**: Easy
- **Pattern**: 1-D Dynamic Programming (Fibonacci / Space Optimized)

---

## Problem Description
You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

### Example 1
```text
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

### Example 2
```text
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

### Constraints
- $1 \le n \le 45$

---

## Intuition & Approach
To reach step $i$, you must arrive from either:
1. Step $i - 1$ (by taking 1 step).
2. Step $i - 2$ (by taking 2 steps).

Therefore, the number of distinct ways to reach step $i$ is:
$$\text{ways}(i) = \text{ways}(i - 1) + \text{ways}(i - 2)$$

This is identical to the Fibonacci recurrence:
- **Base Cases**:
  - $\text{ways}(1) = 1$
  - $\text{ways}(2) = 2$
- **Space Optimization**:
  - We only need the previous two values (`prev` and `curr`) to calculate `new_step`, reducing space complexity from $\mathcal{O}(n)$ to $\mathcal{O}(1)$.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Single linear pass from step 3 up to $n$.
- **Space Complexity**: $\mathcal{O}(1)$ — Only two scalar variables (`prev` and `curr`) are maintained in memory.

---

## Edge Cases Considered
- **$n = 1$**: Handled by the guard `if n <= 2: return n`, returning 1 directly.
- **$n = 2$**: Returns 2 directly.
- **Maximum constraint ($n = 45$)**: The result fits comfortably within standard integer representations.
