# Maximum Product Subarray

- **Source**: LeetCode 152 / NeetCode 150
- **Links**: [LeetCode #152](https://leetcode.com/problems/maximum-product-subarray/) | [NeetCode](https://neetcode.io/problems/maximum-product-subarray)
- **Difficulty**: Medium
- **Pattern**: 1-D Dynamic Programming

---

## Problem Description
Given an integer array `nums`, find a subarray that has the largest product, and return *the product*.

The test cases are generated so that the answer will fit in a 32-bit integer.

---

## Intuition & Approach
- Unlike maximum sum subarray (Kadane's algorithm), multiplying by a negative number flips signs:
  - A large positive product becomes a large negative product.
  - A small negative product becomes a large positive product.
- Track both `curr_max` and `curr_min` simultaneously at each step:
  - When encountering a negative number `nums[i] < 0`, swap `curr_max` and `curr_min`.
  - Update `curr_max = max(nums[i], curr_max * nums[i])`.
  - Update `curr_min = min(nums[i], curr_min * nums[i])`.
  - Maintain `global_max = max(global_max, curr_max)`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Single pass through the array `nums` of length $n$.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant auxiliary space for trackers.
