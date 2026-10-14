"""
Problem: Valid Sudoku
LeetCode: 36 (https://leetcode.com/problems/valid-sudoku/)
NeetCode 150: Valid Sudoku (https://neetcode.io/problems/valid-sudoku)
Difficulty: Medium
Pattern: Arrays & Hashing (Hash Set / Matrix Traversal)
"""

import collections
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val == ".":
                    continue
                r = i // 3
                c = j // 3
                if val in rows[i] or val in cols[j] or val in boxes[r, c]:
                    return False
                else:
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[r, c].add(val)
        return True
