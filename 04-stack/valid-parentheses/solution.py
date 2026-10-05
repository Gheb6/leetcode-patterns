"""
Problem: Valid Parentheses
LeetCode: 20 (https://leetcode.com/problems/valid-parentheses/)
NeetCode 150: Validate Parentheses (https://neetcode.io/problems/validate-parentheses)
Difficulty: Easy
Pattern: Stack
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []
        my_map = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if stack and my_map[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack