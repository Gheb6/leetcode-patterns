# Permutation in String

- **Source**: LeetCode 567 / NeetCode 150
- **Links**: [LeetCode #567](https://leetcode.com/problems/permutation-in-string/) | [NeetCode](https://neetcode.io/problems/permutation-string)
- **Difficulty**: Medium
- **Pattern**: Sliding Window (Fixed Length / Frequency Map Matching)

---

## Problem Description
Given two strings `s1` and `s2`, return `true` if `s2` contains a **permutation** of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the **substring** of `s2`.

### Example 1
```text
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

### Example 2
```text
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```

### Constraints
- $1 \le \text{s1.length}, \text{s2.length} \le 10^4$
- `s1` and `s2` consist of lowercase English letters.

---

## Strategy & Approach
A permutation of a string is an anagram of that string. Therefore, the problem reduces to finding whether any contiguous substring in `s2` of length `len(s1)` has the exact same character frequency distribution as `s1`.

### Fixed-Size Sliding Window:
1. **Initial Guard**: If `len(s1) > len(s2)`, `s2` cannot contain a permutation of `s1`; return `False`.
2. **Frequency Counting**:
   - Count character frequencies of `s1` in hash map `string_1`.
   - Count character frequencies of the first window of size `window_dim = len(s1)` in `s2` into `string_2`.
3. **Slide the Window**:
   - For each index $i$ from `window_dim` up to $\text{len}(s2)$:
     - If `string_1 == string_2`, a valid permutation window is found; return `True`.
     - Otherwise, slide the window by 1:
       - Decrement frequency of the outgoing character: `s2[i - window_dim]`.
       - If its count drops to 0, delete the key from `string_2` so dictionary equality checks remain accurate without spurious zero keys.
       - Increment frequency of incoming character: `s2[i]`.
4. **Final Window Check**:
   - Return `string_1 == string_2` for the last window.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(|s_1| + (|s_2| - |s_1|) \cdot \Sigma) = \mathcal{O}(|s_2|)$ — Populating initial frequencies takes $\mathcal{O}(|s_1|)$. Sliding the window performs at most $|s_2| - |s_1|$ steps, each comparing hash maps of at most $\Sigma = 26$ lowercase English characters ($\mathcal{O}(26) = \mathcal{O}(1)$ per comparison).
- **Space Complexity**: $\mathcal{O}(\Sigma) = \mathcal{O}(1)$ — Auxiliary storage uses two hash maps storing at most 26 unique lowercase English letter entries.

---

## Edge Cases Considered
- **`len(s1) > len(s2)`**: Handled immediately at the start returning `False`.
- **Matching window at the very beginning of `s2`**: Detected at the start of the loop ($i = \text{window\_dim}$).
- **Matching window at the very end of `s2`**: Handled by the final `return string_1 == string_2`.
- **Single character strings**: Works without out-of-bounds errors.

