"""
Problem: Islands and Treasure (Walls and Gates)
LeetCode: 286 (https://leetcode.com/problems/walls-and-gates/)
NeetCode 150: Islands and Treasure (https://neetcode.io/problems/islands-and-treasure)
Difficulty: Medium
Pattern: Graphs (Multi-Source BFS)
"""

from collections import deque
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        treasures = deque()
        cols = len(grid[0])
        rows = len(grid)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    treasures.append( (i, j) )
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while treasures:
            elem = treasures.popleft()
            for dr, dc in directions:
                nr, nc = elem[0] + dr, elem[1] + dc
                if nr < rows and nc < cols and nr >= 0 and nc >=0:
                    if grid[nr][nc] == -1:
                        continue
                    elif grid[nr][nc] == 2147483647:
                        grid[nr][nc] = grid[elem[0]][elem[1]] + 1
                        treasures.append( (nr, nc) )
