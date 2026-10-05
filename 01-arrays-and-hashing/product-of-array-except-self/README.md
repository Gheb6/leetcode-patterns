# Product of Array Except Self

- **Source**: LeetCode 238 / NeetCode 150
- **Links**: [LeetCode #238](https://leetcode.com/problems/product-of-array-except-self/) | [NeetCode](https://neetcode.io/problems/products-of-array-discluding-self)
- **Difficulty**: Medium
- **Pattern**: Arrays & Hashing (Prefix & Suffix Products)

---

## Problem Description
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

You must write an algorithm that runs in $\mathcal{O}(n)$ time and without using the division operation.

---

## Intuition & Approach
- Build the result in two passes:
  1. **Left-to-right pass**: Store in `left[i]` the prefix product of all numbers before index `i`.
  2. **Right-to-left pass**: Maintain a running suffix product `right_prod` and multiply it into `left[i]`.
- This avoids using division and operates in $\mathcal{O}(1)$ auxiliary space beyond the output array.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Two linear passes over the array of length $n$.
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space (excluding the output array).
