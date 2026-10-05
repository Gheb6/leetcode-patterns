# Longest Substring Without Repeating Characters

- **Source**: LeetCode 3 / NeetCode 150
- **Links**: [LeetCode #3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [NeetCode](https://neetcode.io/problems/longest-substring-without-repeating-characters)
- **Difficulty**: Medium
- **Pattern**: Sliding Window (Dynamic Window / Hash Map)

---

## Problem Description
Given a string `s`, find the length of the **longest substring** without repeating characters.

---

## Strategy & Approach
Use a **sliding window** with a hash map to store the most recent index of each character:
1. Maintain two pointers for the window: `left` pointer and current index `i` (right pointer).
2. Use a hash map `seen` mapping `character -> last_seen_index`.
3. For each character `s[i]`:
   - If `s[i]` is already in `seen`, jump `left` past the previous occurrence: `left = max(left, seen[s[i]] + 1)`.
   - Update `seen[s[i]] = i`.
   - Update the maximum length: `longest = max(longest, i - left + 1)`.
4. Return `longest`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — We iterate through the string of length $n$ once.
- **Space Complexity**: $\mathcal{O}(\min(n, m))$ — Where $m$ is the size of the character set (at most $\mathcal{O}(1)$ for fixed ASCII/extended ASCII sets).

---

## Edge Cases Considered
- Empty string `s = ""` (returns `0`).
- String with all identical characters, e.g., `"bbbbb"` (returns `1`).
- String with all unique characters, e.g., `"abcdef"` (returns string length).
