# Min Cost Climbing Stairs

- **Source**: LeetCode 746 / NeetCode 150
- **Links**: [LeetCode #746](https://leetcode.com/problems/min-cost-climbing-stairs/) | [NeetCode](https://neetcode.io/problems/min-cost-climbing-stairs)
- **Difficulty**: Easy
- **Pattern**: 1-D Dynamic Programming (State Transition / Space Optimized)

---

## Problem Description
You are given an integer array `cost` where `cost[i]` is the cost of $i$-th step on a staircase. Once you pay the cost, you can either climb `1` or `2` steps.

You can either start from the step with index `0`, or the step with index `1`.

Return the *minimum cost to reach the top of the floor*.

### Example 1
```text
Input: cost = [10, 15, 20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
```

### Example 2
```text
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
```

### Constraints
- $2 \le \text{cost.length} \le 1000$
- $0 \le \text{cost}[i] \le 999$

---

## Intuition & Approach
To reach step $i$, we could have arrived from step $i - 1$ or step $i - 2$. The cost to land on step $i$ is:
$$\text{min\_cost}[i] = \text{cost}[i] + \min(\text{min\_cost}[i - 1], \text{min\_cost}[i - 2])$$

Because reaching the "top of the floor" means moving beyond the last step (either by jumping from step $n - 1$ or step $n - 2$), the final answer is:
$$\min(\text{min\_cost}[n - 1], \text{min\_cost}[n - 2])$$

### Space Optimization:
Instead of maintaining an array of size $n$, notice that computing the cost for step $i$ only requires the costs of the previous two steps.
- We maintain two rolling pointers `prev` ($\text{min\_cost}[i - 2]$) and `curr` ($\text{min\_cost}[i - 1]$).
- Each step updates:
  $$\text{new\_cost} = \min(\text{prev}, \text{curr}) + \text{cost}[i]$$
  $$\text{prev} = \text{curr}, \quad \text{curr} = \text{new\_cost}$$
- After iterating through step $n - 1$, the minimum cost to clear the top is $\min(\text{new\_cost}, \text{prev})$.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Single linear scan over the array `cost`.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant auxiliary space using rolling scalar variables.

---

## Edge Cases Considered
- **Length 2** (e.g. `cost = [10, 15]`): Immediately returns $\min(\text{cost}[0], \text{cost}[1]) = 10$.
- **Zero costs**: Steps with 0 cost are traversed without penalty.
