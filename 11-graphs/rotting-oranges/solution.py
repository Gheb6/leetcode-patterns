"""
Problem: Rotting Oranges (Rotting Fruit)
LeetCode: 994 (https://leetcode.com/problems/rotting-oranges/)
NeetCode 150: Rotting Fruit (https://neetcode.io/problems/rotting-fruit)
Difficulty: Medium
Pattern: Graphs (Multi-Source BFS / Grid Simulation)
"""

from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        my_deque = deque()
        fresh = 0
        time = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    my_deque.append((i, j))
        while my_deque and fresh > 0:
            for _ in range(len(my_deque)):
                r, c = my_deque.popleft()
                for dr, dc in directions:
                    if -1 < c + dc < column and -1 < r + dr < row and grid[r + dr][c + dc] == 1:
                        grid[r + dr][c + dc] = 2
                        my_deque.append((r + dr, c + dc))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: Standard rotting cascade
    grid1 = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]
    assert sol.orangesRotting(grid1) == 4, "Failed on grid1"

    # Test case 2: Impossible to rot all fresh oranges
    grid2 = [
        [2, 1, 1],
        [0, 1, 1],
        [1, 0, 1]
    ]
    assert sol.orangesRotting(grid2) == -1, "Failed on grid2"

    # Test case 3: No fresh oranges at start
    grid3 = [[0, 2]]
    assert sol.orangesRotting(grid3) == 0, "Failed on grid3"

    # Test case 4: Only a fresh orange with no rotten ones
    grid4 = [[1]]
    assert sol.orangesRotting(grid4) == -1, "Failed on grid4"

    print("All test cases for Rotting Oranges passed!")
