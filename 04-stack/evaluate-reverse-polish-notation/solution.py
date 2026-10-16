"""
Problem: Evaluate Reverse Polish Notation
LeetCode: 150 (https://leetcode.com/problems/evaluate-reverse-polish-notation/)
NeetCode 150: Evaluate Reverse Polish Notation (https://neetcode.io/problems/evaluate-reverse-polish-notation)
Difficulty: Medium
Pattern: Stack
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {"+", "-", "*", "/"}
        my_stack = []
        if len(tokens) == 1:
            return int(tokens[0])
        for token in tokens:
            if token not in operations:
                token = int(token)
                my_stack.append(token)
            else:
                elem_2 = my_stack.pop()
                elem_1 = my_stack.pop()
                res = 0
                if token == '+':
                    res = (elem_1 + elem_2)
                elif token == '-':
                    res = (elem_1 - elem_2)
                elif token == '/':
                    res = int(elem_1 / elem_2)
                elif token == '*':
                    res = elem_1 * elem_2
                my_stack.append(res)
        return my_stack[0]
