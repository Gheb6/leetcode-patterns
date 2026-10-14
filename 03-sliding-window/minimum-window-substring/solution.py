"""
Problem: Minimum Window Substring
LeetCode: 76 (https://leetcode.com/problems/minimum-window-substring/)
NeetCode 150: Minimum Window Substring (https://neetcode.io/problems/minimum-window-with-characters)
Difficulty: Hard
Pattern: Sliding Window
"""

from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        window = defaultdict(int)
        need = len(count_t)
        have = 0
        left = 0
        right = 0
        res = [-1, -1]
        res_len = float("infinity")
        for right in range(len(s)):
            c = s[right]
            window[c] += 1
            if window[c] == count_t[c]:
                have += 1
            while have == need:
                if (right - left + 1) < res_len:
                    res_len = right - left + 1
                    res = [left, right]
                c = s[left]
                window[s[left]] -= 1
                if c in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1
        left, right = res
        return s[left : right + 1] if res_len != float("infinity") else ""
