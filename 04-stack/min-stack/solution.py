"""
Problem: Min Stack
LeetCode: 155 (https://leetcode.com/problems/min-stack/)
NeetCode 150: Minimum Stack (https://neetcode.io/problems/minimum-stack)
Difficulty: Medium
Pattern: Stack
"""


class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if not self.main_stack:
            self.main_stack.append(val)
            self.min_stack.append(val)
        else:
            self.main_stack.append(val)
            minimum = min(val, self.min_stack[-1])
            self.min_stack.append( minimum )

    def pop(self) -> None:
        self.main_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        res = self.min_stack[-1]
        return res
