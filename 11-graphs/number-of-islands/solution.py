"""
Problem: Number of Islands
LeetCode: 200 (https://leetcode.com/problems/number-of-islands/)
NeetCode 150: Number of Islands (https://neetcode.io/problems/count-number-of-islands)
Difficulty: Medium
Pattern: Graphs (Breadth-First Search / Connected Components)
"""

from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        column = len(grid[0])
        my_deque = deque()
        islands = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(row):
            for j in range(column):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    my_deque.append((i,j))
                    islands += 1
                    while my_deque:
                        r, c = my_deque.popleft()
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < row and 0 <= nc < column and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"
                                my_deque.append((nr, nc))
        return islands


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: Single island
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert sol.numIslands(grid1) == 1, "Failed on grid1"

    # Test case 2: Three islands
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert sol.numIslands(grid2) == 3, "Failed on grid2"

    # Test case 3: Single water cell
    assert sol.numIslands([["0"]]) == 0, "Failed on single water cell"

    # Test case 4: Single land cell
    assert sol.numIslands([["1"]]) == 1, "Failed on single land cell"

    print("All test cases for Number of Islands passed!")
