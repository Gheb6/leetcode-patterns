"""
Problem: Valid Anagram
LeetCode: 242 (https://leetcode.com/problems/valid-anagram/)
NeetCode 150: Is Anagram (https://neetcode.io/problems/is-anagram)
Difficulty: Easy
Pattern: Arrays & Hashing (Frequency Counter / Hash Map)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Determines if t is an anagram of s using character frequency counts.
        
        Time Complexity: O(N) where N is the length of the strings.
        Space Complexity: O(1) extra space because there are at most 26 lowercase English letters.
        """
        if len(s) != len(t):
            return False

        char_counts = {}
        for ch in s:
            char_counts[ch] = char_counts.get(ch, 0) + 1

        for ch in t:
            if ch not in char_counts or char_counts[ch] == 0:
                return False
            char_counts[ch] -= 1

        return True


if __name__ == "__main__":
    sol = Solution()
    # Test cases
    assert sol.isAnagram("anagram", "nagaram") is True, "Failed on 'anagram' & 'nagaram'"
    assert sol.isAnagram("rat", "car") is False, "Failed on 'rat' & 'car'"
    assert sol.isAnagram("a", "ab") is False, "Failed on length mismatch"
    assert sol.isAnagram("", "") is True, "Failed on empty strings"
    print("All test cases for Valid Anagram passed!")
