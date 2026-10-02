"""
Problem: Group Anagrams
LeetCode: 49 (https://leetcode.com/problems/group-anagrams/)
NeetCode 150: Anagram Groups (https://neetcode.io/problems/anagram-groups)
Difficulty: Medium
Pattern: Arrays & Hashing (Hash Map with Canonical Key)
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups anagrams together using sorted string as canonical hash map key.
        
        Time Complexity: O(N * K log K) where N is number of strings and K is max string length.
        Space Complexity: O(N * K) to store grouped strings in the dictionary.
        """
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        return list(groups.values())


if __name__ == "__main__":
    sol = Solution()
    # Test cases
    result = sol.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"])
    # Normalize order for assertion
    sorted_result = sorted([sorted(g) for g in result])
    expected = sorted([["act", "cat"], ["hat"], ["pots", "stop", "tops"]])
    assert sorted_result == expected, f"Expected {expected}, got {sorted_result}"

    assert sol.groupAnagrams(["x"]) == [["x"]], "Failed on single character"
    assert sol.groupAnagrams([""]) == [[""]], "Failed on empty string"
    print("All test cases for Group Anagrams passed!")
