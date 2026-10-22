# Rotting Oranges (Rotting Fruit)

- **Source**: LeetCode 994 / NeetCode 150
- **Links**: [LeetCode #994](https://leetcode.com/problems/rotting-oranges/) | [NeetCode](https://neetcode.io/problems/rotting-fruit)
- **Difficulty**: Medium
- **Pattern**: Graphs (Multi-Source BFS / Grid Simulation)

---

## Problem Description
You are given an `m x n` `grid` where each cell can have one of three values:
- `0`: representing an empty cell,
- `1`: representing a fresh orange, or
- `2`: representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1`.

### Example 1
```text
Input: grid = [
  [2, 1, 1],
  [1, 1, 0],
  [0, 1, 1]
]
Output: 4
```

### Example 2
```text
Input: grid = [
  [2, 1, 1],
  [0, 1, 1],
  [1, 0, 1]
]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
```

### Example 3
```text
Input: grid = [[0, 2]]
Output: 0
Explanation: Since there are already 0 fresh oranges at minute 0, the answer is just 0.
```

### Constraints
- $m == \text{grid.length}$
- $n == \text{grid}[i]\text{.length}$
- $1 \le m, n \le 10$
- `grid[i][j]` is `0`, `1`, or `2`.

---

## Intuition & Approach
This problem models the simultaneous spread of an infection across a 2D grid, making it an ideal candidate for **Multi-Source Breadth-First Search (BFS)**:

1. **Initial Scan**:
   - Traverse the entire grid to count initial fresh oranges (`fresh`) and collect coordinates of all rotten oranges into a `deque` (`my_deque`).
2. **Level-by-Level BFS (Time Steps)**:
   - While `my_deque` is not empty and `fresh > 0`:
     - Snapshot the current size of the queue `len(my_deque)` to process exactly one minute (one level) of contagion.
     - For each rotten orange, inspect its 4 neighbors:
       - If a neighbor contains a fresh orange (`grid[nr][nc] == 1`):
         - Rot the orange in-place: `grid[nr][nc] = 2`.
         - Decrement `fresh -= 1`.
         - Append its coordinates to `my_deque`.
     - Increment `time += 1`.
3. **Termination**:
   - If `fresh == 0`, all oranges have been successfully rotted; return `time`.
   - If `fresh > 0` after the queue becomes empty, some fresh oranges are unreachable; return `-1`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(m \cdot n)$ — Every cell is scanned during initialization. In the BFS, each cell is enqueued and popped at most once.
- **Space Complexity**: $\mathcal{O}(m \cdot n)$ — The queue holds at most $m \cdot n$ coordinates in the worst case.

---

## Edge Cases Considered
- **Zero fresh oranges at the start** (e.g. `grid = [[0, 2]]`): While loop never executes since `fresh > 0` is false, immediately returning `0`.
- **Fresh oranges surrounded by empty cells or grid boundaries**: BFS terminates with `fresh > 0`, correctly returning `-1`.
- **All cells are empty** (`grid = [[0]]`): Returns `0`.
- **Grid with only fresh oranges** (`grid = [[1]]`): Deque starts empty, while loop does not run, returns `-1`.
