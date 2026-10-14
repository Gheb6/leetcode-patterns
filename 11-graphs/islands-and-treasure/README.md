# Islands and Treasure (Walls and Gates)

- **Source**: LeetCode 286 / NeetCode 150
- **Links**: [LeetCode #286](https://leetcode.com/problems/walls-and-gates/) | [NeetCode](https://neetcode.io/problems/islands-and-treasure)
- **Difficulty**: Medium
- **Pattern**: Graphs (Multi-Source BFS)

---

## Problem Description
You are given an $m \times n$ 2D grid initialized with these three possible values:
- `-1`: A water cell / wall that cannot be traversed.
- `0`: A treasure chest / gate.
- `INF` (`2147483647`): Empty land.

Fill each empty land cell with the distance to its nearest treasure chest. If it is impossible to reach a treasure chest, it should remain `INF`.

---

## Strategy & Approach
Instead of running a separate BFS from each empty cell, perform **Multi-Source BFS** starting simultaneously from all treasure chests (`0`):
1. **Queue Initialization**: Scan the grid and add all coordinates with `grid[r][c] == 0` into a `deque`.
2. **Breadth-First Expansion**:
   - Dequeue the front cell `(r, c)`.
   - Check all 4 adjacent neighbors `(nr, nc)`.
   - If a neighbor is an unvisited empty land (`2147483647`), update its distance:
     $$\text{grid}[nr][nc] = \text{grid}[r][c] + 1$$
   - Enqueue `(nr, nc)`.
3. Because BFS traverses level by level, the first time an empty land is reached represents its shortest distance to any treasure chest.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(m \cdot n)$ — each cell is enqueued and visited at most once.
- **Space Complexity**: $\mathcal{O}(m \cdot n)$ — in the worst case, the queue holds $\mathcal{O}(m \cdot n)$ coordinates.
