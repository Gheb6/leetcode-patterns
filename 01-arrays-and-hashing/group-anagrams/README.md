# Group Anagrams

- **Source**: LeetCode 49 / NeetCode 150
- **Links**: [LeetCode #49](https://leetcode.com/problems/group-anagrams/) | [NeetCode](https://neetcode.io/problems/anagram-groups)
- **Difficulty**: Medium
- **Pattern**: Arrays & Hashing (Hash Map / Canonical Key)

---

## Problem Description
Given an array of strings `strs`, group all anagrams together into sublists. You can return the output in any order.

### Example 1
```text
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
```

---

## Intuition & Approach
Two strings are anagrams if and only if their sorted representations (or character frequency tuples) are identical. We can use this property to create a **canonical key** for a hash map:

1. **Sorting Key Approach** (implemented in `solution.py`):
   - For each string `s`, sort its characters: `key = "".join(sorted(s))`.
   - Append `s` to `map[key]`.
   - **Time Complexity**: $\mathcal{O}(n \cdot k \log k)$, where $n$ is the number of strings and $k$ is the maximum length of a string.
2. **Frequency Tuple Key Approach (Optimization)**:
   - Instead of sorting in $\mathcal{O}(k \log k)$, count character frequencies in a 26-element tuple: `key = tuple(count)`.
   - **Time Complexity**: $\mathcal{O}(n \cdot k)$ linear time!

---

## Complexity Analysis (Sorting Key)
- **Time Complexity**: $\mathcal{O}(n \cdot k \log k)$ — Sorting each of the $n$ words of length at most $k$.
- **Space Complexity**: $\mathcal{O}(n \cdot k)$ — Storing all words inside the hash map.

---

## Edge Cases Considered
- `strs = [""]` (single empty string): returns `[[""]]`.
- `strs = ["a"]` (single character): returns `[["a"]]`.
- No anagrams among words: each word ends up in its own single-element group.
