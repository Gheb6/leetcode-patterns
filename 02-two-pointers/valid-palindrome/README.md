# Valid Palindrome

- **Source**: LeetCode 125 / NeetCode 150
- **Links**: [LeetCode #125](https://leetcode.com/problems/valid-palindrome/) | [NeetCode](https://neetcode.io/problems/is-palindrome)
- **Difficulty**: Easy
- **Pattern**: Two Pointers

---

## Problem Description
A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

---

## Strategy & Approach
- Initialize two pointers at opposite ends (`left = 0`, `right = len(s) - 1`).
- Skip non-alphanumeric characters using `.isalnum()`.
- Compare characters case-insensitively on-the-fly (`s[left].lower() == s[right].lower()`):
  - If equal, advance `left` and decrement `right`.
  - If different, return `False`.
- If the pointers cross without mismatches, return `True`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Linear scan over the string of length $n$.
- **Space Complexity**: $\mathcal{O}(1)$ — In-place pointer scan comparing characters on-the-fly without allocating a transformed copy of the string.

