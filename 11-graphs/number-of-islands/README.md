# Number of Islands

- **Source**: LeetCode 200 / NeetCode 150
- **Links**: [LeetCode #200](https://leetcode.com/problems/number-of-islands/) | [NeetCode](https://neetcode.io/problems/count-number-of-islands)
- **Difficulty**: Medium
- **Pattern**: Graphs (Breadth-First Search / Connected Components)

---

## Problem Description
Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

### Example 1
```text
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

### Example 2
```text
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

### Constraints
- $m == \text{grid.length}$
- $n == \text{grid}[i]\text{.length}$
- $1 \le m, n \le 300$
- `grid[i][j]` is `'0'` or `'1'`.

---

## Intuition & Approach
The grid can be modeled as an unweighted, undirected graph where each land cell (`'1'`) is a node connected to up to 4 neighbors (up, down, left, right). Finding the number of islands corresponds to finding the number of **connected components**.

### Breadth-First Search (BFS) / In-place Marking:
1. Iterate over every cell $(i, j)$ in the $m \times n$ grid:
   - When encountering a land cell (`grid[i][j] == '1'`):
     - We have discovered a new island: increment `islands += 1`.
     - "Sink" the island (or mark it as visited) by immediately flipping `grid[i][j] = '0'`.
     - Push `(i, j)` to a `deque`.
     - Run a **BFS traversal**:
       - While the queue is not empty, pop `(r, c) = my_deque.popleft()`.
       - For each of the 4 cardinal directions `(dr, dc)`:
         - Calculate neighbor `(nr, nc) = (r + dr, c + dc)`.
         - If `(nr, nc)` is in bounds and `grid[nr][nc] == '1'`:
           - Mark `grid[nr][nc] = '0'` immediately (to avoid duplicate enqueueing).
           - Enqueue `(nr, nc)`.
2. Return `islands`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(m \cdot n)$ — Each cell in the grid is visited at most twice: once in the outer loops, and at most once by the BFS queue.
- **Space Complexity**: $\mathcal{O}(\min(m, n))$ in typical BFS queue behavior, up to $\mathcal{O}(m \cdot n)$ in worst-case grid filling. Marking visited cells in-place avoids an external `visited` matrix.

---

## Edge Cases Considered
- **All water** (e.g. `grid = [["0"]]`): Loops complete without triggering BFS, correctly returning `0`.
- **All land**: BFS expands across the entire grid in a single pass, returning `1`.
- **Diagonal lands**: Lands touching only diagonally are not connected, correctly treated as separate islands.
- **Grid with dimensions $1 \times n$ or $m \times 1$**: Handled properly by boundary checks.
