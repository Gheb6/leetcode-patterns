# Binary Search

- **Source**: LeetCode 704 / NeetCode 150
- **Links**: [LeetCode #704](https://leetcode.com/problems/binary-search/) | [NeetCode](https://neetcode.io/problems/binary-search)
- **Difficulty**: Easy
- **Pattern**: Binary Search (Exact Value Search)

---

## Problem Description
Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with $\mathcal{O}(\log n)$ runtime complexity.

---

## Intuition & Approach
Because the array is sorted, every comparison with the middle element `nums[mid]` halves the search space:
- If `nums[mid] == target`: Found target, return `mid`.
- If `nums[mid] < target`: The target must be in the right half $\implies$ `left = mid + 1`.
- If `nums[mid] > target`: The target must be in the left half $\implies$ `right = mid - 1`.

> **Interview Tip**: Always prefer `mid = left + (right - left) // 2` over `(left + right) // 2`. In Python integers have arbitrary precision, but in C++, Java, and Go `(left + right)` can cause integer overflow when both bounds are large.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(\log n)$ — At each iteration, the search interval is cut in half.
- **Space Complexity**: $\mathcal{O}(1)$ — Only pointer variables are maintained.

---

## Edge Cases Considered
- Target at boundaries (first or last element).
- Target smaller than minimum or larger than maximum element.
- Single element array.
