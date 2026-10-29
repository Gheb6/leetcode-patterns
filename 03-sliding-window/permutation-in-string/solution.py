"""
Problem: Permutation in String
LeetCode: 567 (https://leetcode.com/problems/permutation-in-string/)
NeetCode 150: Permutation in String (https://neetcode.io/problems/permutation-string)
Difficulty: Medium
Pattern: Sliding Window (Fixed Length / Frequency Map Matching)
"""

from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        string_1 = defaultdict(int)
        string_2 = defaultdict(int)
        for c in s1:
            string_1[c] += 1
        window_dim = len(s1)

        for i in range(window_dim):
            string_2[s2[i]] += 1

        for i in range(window_dim, len(s2)):
            if string_1 == string_2:
                return True
            else:
                string_2[s2[i - window_dim]] -= 1
                if string_2[s2[i - window_dim]] == 0:
                    del string_2[s2[i - window_dim]]
                string_2[s2[i]] += 1
        return string_1 == string_2


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: s1 = "ab", s2 = "eidbaooo" -> True (contains "ba")
    assert sol.checkInclusion("ab", "eidbaooo") is True, "Failed on example 1"

    # Test case 2: s1 = "ab", s2 = "eidboaoo" -> False
    assert sol.checkInclusion("ab", "eidboaoo") is False, "Failed on example 2"

    # Test case 3: Permutation at the end of s2
    assert sol.checkInclusion("adc", "dcda") is True, "Failed on 'adc' in 'dcda'"

    # Test case 4: Single character matching
    assert sol.checkInclusion("a", "a") is True, "Failed on single character match"

    # Test case 5: s1 longer than s2
    assert sol.checkInclusion("longer", "short") is False, "Failed when s1 is longer"

    # Test case 6: Duplicate characters
    assert sol.checkInclusion("hello", "ooolleoooleh") is False, "Failed on test case with repeated characters"

    print("All test cases for Permutation in String passed!")

