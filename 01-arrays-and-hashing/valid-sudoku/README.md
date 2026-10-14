# Valid Sudoku

- **Source**: LeetCode 36 / NeetCode 150
- **Links**: [LeetCode #36](https://leetcode.com/problems/valid-sudoku/) | [NeetCode](https://neetcode.io/problems/valid-sudoku)
- **Difficulty**: Medium
- **Pattern**: Arrays & Hashing (Hash Set / Matrix Traversal)

---

## Problem Description
Determine if a $9 \times 9$ Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine $3 \times 3$ sub-boxes of the grid must contain the digits `1-9` without repetition.

> **Note**:
> - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
> - Only the filled cells need to be validated according to the mentioned rules.
> - Empty cells are indicated by the character `'.'`.

### Example 1
```text
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
```

### Example 2
```text
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the first element on the top-left corner being 8 instead of 5. Since there are two 8's in the first 3x3 sub-box and also in the first column, it is invalid.
```

### Constraints
- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit `'1'-'9'` or `'.'`.

---

## Intuition & Approach
To validate the Sudoku board in a single pass, we need to efficiently track which numbers have already appeared in each row, column, and $3 \times 3$ block.

1. **State Tracking with Hash Sets**:
   - `rows = collections.defaultdict(set)`: tracks the set of digits seen in row $i$.
   - `cols = collections.defaultdict(set)`: tracks the set of digits seen in column $j$.
   - `boxes = collections.defaultdict(set)`: tracks digits seen in the sub-box indexed by `(r, c)`.

2. **$3 \times 3$ Box Coordinate Mapping**:
   - Dividing the row and column indices by 3 using integer floor division maps every cell $(i, j)$ into its corresponding sub-box coordinate:
     $$r = i // 3, \quad c = j // 3 \quad (r, c \in \{0, 1, 2\})$$
   - This partitions the $9 \times 9$ grid into 9 distinct $(r, c)$ keys.

3. **Single-Pass Traversal**:
   - Iterate over each cell $(i, j)$ on the $9 \times 9$ grid.
   - If the cell is empty (`"."`), skip it.
   - Check if `val` is already present in `rows[i]`, `cols[j]`, or `boxes[(r, c)]`:
     - If yes, the board violates Sudoku rules $\rightarrow$ return `False`.
     - Otherwise, insert `val` into `rows[i]`, `cols[j]`, and `boxes[(r, c)]`.
   - If all cells are traversed without any duplicate found, return `True`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(1)$ or $\mathcal{O}(N^2)$ with $N = 9$. We iterate over a fixed grid of $9 \times 9 = 81$ cells. Each hash set lookup and insertion is $\mathcal{O}(1)$ on average, resulting in strictly bounded constant running time.
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space. The hash sets store at most $9$ values for each of the 9 rows, 9 columns, and 9 sub-boxes ($3 \times 81$ entries in the worst case), which is fixed and bounded.

---

## Edge Cases Considered
- **Partially filled board**: The rules only apply to the filled cells; unfilled cells (`"."`) are ignored.
- **Duplicate in the same $3 \times 3$ sub-box**: Correctly captured via the `(i // 3, j // 3)` coordinate key even if row or column indices differ.
- **Empty board**: Completely empty board with only `"."` immediately returns `True`.
