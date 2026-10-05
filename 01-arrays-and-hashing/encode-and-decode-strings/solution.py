"""
Problem: Encode and Decode Strings
LeetCode: 271 (https://leetcode.com/problems/encode-and-decode-strings/)
NeetCode 150: String Encode and Decode (https://neetcode.io/problems/string-encode-and-decode)
Difficulty: Medium
Pattern: Arrays & Hashing / String
"""

from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Time Complexity: O(N) where N is total number of characters across all strings.
        Space Complexity: O(N) for the encoded string.
        """
        encoded_string = ""
        for c in strs:
            encoded_string = encoded_string + str( len(c) ) + "#" + c
        return encoded_string

    def decode(self, s: str) -> List[str]:
        """
        Time Complexity: O(N) where N is the length of encoded string s.
        Space Complexity: O(N) to store decoded list of strings.
        """
        decoded_strs = []
        i = 0
        while i < len(s):
            j = s.find('#',i)
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            decoded_strs.append(word)
            i = j + 1 + length
        return decoded_strs
