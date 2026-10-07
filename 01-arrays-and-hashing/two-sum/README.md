# Two Sum

- **Source**: LeetCode 1 / NeetCode 150
- **Links**: [LeetCode #1](https://leetcode.com/problems/two-sum/) | [NeetCode](https://neetcode.io/problems/two-integer-sum)
- **Difficulty**: Easy
- **Pattern**: Arrays & Hashing (Hash Map / One-pass)

---

## Problem Description
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice. You can return the answer in any order.

---

## Intuition & Approach
- Use a **Hash Map** (`my_dict`) to store elements and their corresponding indices.
- In a single pass, for each element:
  - Check if the current value exists in the dictionary (representing a previous complement). If so, return `[my_dict[nums[i]], i]`.
  - Otherwise, calculate its complement `target - nums[i]` and map it to current index `i`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Single pass through the array with $\mathcal{O}(1)$ average hash map lookups.
- **Space Complexity**: $\mathcal{O}(n)$ — The hash map stores at most $n$ entries.
