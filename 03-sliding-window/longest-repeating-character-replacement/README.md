# Longest Repeating Character Replacement

- **Source**: LeetCode 424 / NeetCode 150
- **Links**: [LeetCode #424](https://leetcode.com/problems/longest-repeating-character-replacement/) | [NeetCode](https://neetcode.io/problems/longest-repeating-substring-with-replacement)
- **Difficulty**: Medium
- **Pattern**: Sliding Window (Frequency Map / Dynamic Window)

---

## Problem Description
You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

### Example 1
```text
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

### Example 2
```text
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
```

### Constraints
- $1 \le \text{s.length} \le 10^5$
- `s` consists of only uppercase English letters.
- $0 \le k \le \text{s.length}$

---

## Intuition & Approach
A substring of length $L = \text{right} - \text{left} + 1$ can be turned into identical characters with at most $k$ operations if and only if:
$$\text{Window Length} - \text{Frequency of Most Common Character} \le k$$

Any character that is not the most frequent character in the current window must be replaced. Thus, the minimum number of replacements needed for the current window is $L - \text{max\_freq}$.

### Sliding Window Strategy:
1. Maintain two pointers `left` and `right` representing the sliding window, and a hash map `frequencies` tracking counts of each uppercase letter within the window.
2. Track `max_freq`, the maximum frequency of any single character observed in the window.
3. Expand the window by advancing `right`:
   - Increment the frequency of `s[right]`.
   - Update `max_freq = max(max_freq, frequencies[s[right]])`.
4. If the window becomes invalid ($(\text{window\_len}) - \text{max\_freq} > k$):
   - Shrink the window from the left: decrement `frequencies[s[left]]` and increment `left`.
5. Update the result length with the valid window size.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Both `left` and `right` traverse the string at most once.
- **Space Complexity**: $\mathcal{O}(1)$ (or $\mathcal{O}(26)$) — Since the string consists only of uppercase English letters, the frequency map contains at most 26 entries.

---

## Edge Cases Considered
- **$k = 0$**: No character replacements permitted; finds the longest contiguous identical substring.
- **$k \ge \text{len}(s)$**: Any character can be converted to match; optimal answer is `len(s)`.
- **Single character string** (`s = "A"`): Returns `1`.
- **String with all identical characters** (e.g. `s = "AAAA"`): Window never shrinks, returning `len(s)`.
