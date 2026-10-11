"""
Problem: Distinct Subsequences
LeetCode: 115 (https://leetcode.com/problems/distinct-subsequences/)
NeetCode 150: Distinct Subsequences (https://neetcode.io/problems/distinct-subsequences)
Difficulty: Hard
Pattern: 2-D Dynamic Programming
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        row = len(s) + 1 
        column = len(t) + 1
        matrix = [[0 for _ in range(column)] for _ in range(row)]
        for i in range(row):
            matrix[i][0] = 1
        for i in range(1, row):
            for j in range(1, column):
                if s[i - 1] != t[j - 1]:
                    matrix[i][j] = matrix[i-1][j]
                else:
                    matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j]
        return matrix[row - 1][column - 1]
