"""
Problem: Longest Substring Without Repeating Characters
LeetCode: 3 (https://leetcode.com/problems/longest-substring-without-repeating-characters/)
NeetCode 150: Longest Substring Without Repeating Characters (https://neetcode.io/problems/longest-substring-without-repeating-characters)
Difficulty: Medium
Pattern: Sliding Window (Hash Map / Two Pointers)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        seen = {}
        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]] = i
            else:
                left = max(left, seen[s[i]] + 1)
                seen[s[i]] = i
            longest = max(i - left + 1, longest)
        return longest
