# Find the Duplicate Number

- **Source**: LeetCode 287 / NeetCode 150
- **Links**: [LeetCode #287](https://leetcode.com/problems/find-the-duplicate-number/) | [NeetCode](https://neetcode.io/problems/find-duplicate-integer)
- **Difficulty**: Medium
- **Pattern**: Linked List (Floyd's Tortoise and Hare / Cycle Detection)

---

## Problem Description
Given an array of integers `nums` containing $n + 1$ integers where each integer is in the range $[1, n]$ inclusive.

There is only **one repeated number** in `nums`, return this *repeated number*.

You must solve the problem **without** modifying the array `nums` and using only constant extra space.

### Example 1
```text
Input: nums = [1, 3, 4, 2, 2]
Output: 2
```

### Example 2
```text
Input: nums = [3, 1, 3, 4, 2]
Output: 3
```

### Example 3
```text
Input: nums = [3, 3, 3, 3, 3]
Output: 3
```

### Constraints
- $1 \le n \le 10^5$
- $\text{nums.length} == n + 1$
- $1 \le \text{nums}[i] \le n$
- All the integers in `nums` appear only **once** except for **precisely one integer** which appears **two or more times**.

---

## Intuition & Approach
The constraints prohibit modifying the array (disqualifying in-place negation or sorting) and require $\mathcal{O}(1)$ auxiliary space (disqualifying hash sets).

By viewing the array as a directed graph where each index $i$ points to node $\text{nums}[i]$ ($i \to \text{nums}[i]$):
- Because values are in the range $[1, n]$ and there are $n + 1$ elements, index 0 is never pointed to by any node (a pure entry point).
- The duplicate value has multiple incoming edges (indegree $\ge 2$), which creates a **cycle** in the graph.
- The entrance to the cycle is precisely the duplicate number!

### Floyd's Tortoise and Hare Algorithm:
1. **Phase 1: Find Intersection**:
   - `slow = nums[nums[0]]` (or `nums[0]`) and `fast = nums[nums[nums[0]]]`.
   - Advance `slow = nums[slow]` (1 step) and `fast = nums[nums[fast]]` (2 steps) until `slow == fast`.
2. **Phase 2: Find Entrance of Cycle**:
   - Reset `slow = 0`.
   - Advance both `slow = nums[slow]` and `fast = nums[fast]` at the same speed (1 step at a time).
   - When they meet again (`slow == fast`), their meeting point is the start of the cycle, which is the duplicate value.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Phase 1 and Phase 2 each traverse at most linear steps proportional to the cycle length and path length.
- **Space Complexity**: $\mathcal{O}(1)$ — In-place pointer traversal with constant auxiliary memory without modifying `nums`.

---

## Edge Cases Considered
- **All elements identical** (e.g. `[3, 3, 3, 3, 3]`): Immediate cycle of length 1, converges correctly to 3.
- **Two elements** (`[1, 1]`): Minimum size $n = 1$, correctly detects 1.
- **Duplicate appears more than twice**: The entrance of the cycle remains unchanged.
