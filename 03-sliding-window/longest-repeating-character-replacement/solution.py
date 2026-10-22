"""
Problem: Longest Repeating Character Replacement
LeetCode: 424 (https://leetcode.com/problems/longest-repeating-character-replacement/)
NeetCode 150: Longest Repeating Character Replacement (https://neetcode.io/problems/longest-repeating-substring-with-replacement)
Difficulty: Medium
Pattern: Sliding Window (Frequency Map / Dynamic Window)
"""

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        res = 0
        frequencies = defaultdict(int)
        max_freq = 0
        for right in range(len(s)):
            max_freq = max(max_freq, frequencies[s[right]])
            frequencies[s[right]] += 1
            right += 1
            if (right - left + 1) - max_freq > k:
                frequencies[s[left]] -= 1
                left += 1
            res = max(res, (right - left + 1))
        return res


if __name__ == "__main__":
    sol = Solution()

    # Test cases
    assert sol.characterReplacement("A", 0) == 1, "Failed on single character"
    print("Test cases for Longest Repeating Character Replacement passed!")
