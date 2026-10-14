# Minimum Window Substring

- **Source**: LeetCode 76 / NeetCode 150
- **Links**: [LeetCode #76](https://leetcode.com/problems/minimum-window-substring/) | [NeetCode](https://neetcode.io/problems/minimum-window-with-characters)
- **Difficulty**: Hard
- **Pattern**: Sliding Window

---

## Problem Description
Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

---

## Strategy & Approach
We use an expanding and contracting **sliding window**:
1. **Target Frequency**: Count required frequencies of each character in `t` using `count_t = Counter(t)` and set `need = len(count_t)`.
2. **Expand Window (`right`)**:
   - Add character `s[right]` to `window`.
   - If the count matches the required frequency (`window[c] == count_t[c]`), increment `have`.
3. **Contract Window (`left`)**:
   - While `have == need`, record the minimal window `[left, right]`.
   - Remove `s[left]` from `window`.
   - If its count drops below the required frequency in `count_t`, decrement `have`.
   - Advance `left` by 1.
4. Return the minimum substring found.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(m + n)$ — where $m = \text{len}(s)$ and $n = \text{len}(t)$. Building `count_t` takes $\mathcal{O}(n)$, and both pointers `left` and `right` traverse `s` at most once.
- **Space Complexity**: $\mathcal{O}(m + n)$ (or $\mathcal{O}(|\Sigma|)$ bounded by alphabet size) — for storing character counts in `count_t` and `window`.
