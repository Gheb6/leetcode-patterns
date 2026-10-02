# Contains Duplicate

- **Source**: LeetCode 217 / NeetCode 150
- **Links**: [LeetCode #217](https://leetcode.com/problems/contains-duplicate/) | [NeetCode](https://neetcode.io/problems/duplicate-integer)
- **Difficulty**: Easy
- **Pattern**: Arrays & Hashing (Hash Set)

---

## Problem Description
Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

### Example 1
```text
Input: nums = [1, 2, 3, 1]
Output: true
```

### Example 2
```text
Input: nums = [1, 2, 3, 4]
Output: false
```

---

## Intuition & Approach
- **Brute Force**: Compare every pair $(i, j)$ with nested loops $\mathcal{O}(n^2)$ time and $\mathcal{O}(1)$ space.
- **Sorting**: Sort the array in $\mathcal{O}(n \log n)$ time and check adjacent elements in $\mathcal{O}(1)$ space.
- **Hash Set (Optimal)**: Iterate through the array once while keeping track of seen elements inside a hash set. Hash set lookup and insertion take average $\mathcal{O}(1)$ time. If an element already exists in `seen`, we return `true` immediately (early return).

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — We iterate through the list at most once, performing $\mathcal{O}(1)$ average set lookups and insertions.
- **Space Complexity**: $\mathcal{O}(n)$ — In the worst case (when all elements are unique), the set stores all $n$ elements.

---

## Edge Cases Considered
- Array with 0 or 1 element: naturally returns `false`.
- All elements identical: detects duplicate on the second element.
- Large negative numbers and zeros: sets handle signed integers seamlessly.
