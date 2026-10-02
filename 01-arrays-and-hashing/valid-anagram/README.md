# Valid Anagram

- **Source**: LeetCode 242 / NeetCode 150
- **Links**: [LeetCode #242](https://leetcode.com/problems/valid-anagram/) | [NeetCode](https://neetcode.io/problems/is-anagram)
- **Difficulty**: Easy
- **Pattern**: Arrays & Hashing (Frequency Counting)

---

## Problem Description
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise. An **anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Example 1
```text
Input: s = "anagram", t = "nagaram"
Output: true
```

### Example 2
```text
Input: s = "rat", t = "car"
Output: false
```

---

## Intuition & Approach
1. **Length Check**: If `len(s) != len(t)`, they cannot be anagrams.
2. **Frequency Map**:
   - Count frequencies of characters in `s` using a dictionary or fixed-size array of 26 integers.
   - Decrement the count when scanning through `t`. If a character is missing or count drops below zero, return `false`.
3. **Alternative (Sorting)**: Sort both strings and compare `sorted(s) == sorted(t)`. Takes $\mathcal{O}(n \log n)$ time and $\mathcal{O}(n)$ space depending on the sorting algorithm.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Single pass over string $s$ and string $t$.
- **Space Complexity**: $\mathcal{O}(1)$ — The alphabet size is bounded (e.g. 26 lowercase English letters), so dictionary/array size is $\mathcal{O}(1)$ bounded.

---

## Edge Cases & Follow-up
- Strings of different lengths: immediately return `false`.
- Empty strings: valid anagram (`true`).
- Unicode characters: A hash table (dictionary) handles arbitrary Unicode characters, whereas a 26-size integer array only handles lowercase English letters.
