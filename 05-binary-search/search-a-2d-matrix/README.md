# Search a 2D Matrix

- **Source**: LeetCode 74 / NeetCode 150
- **Links**: [LeetCode #74](https://leetcode.com/problems/search-a-2d-matrix/) | [NeetCode](https://neetcode.io/problems/search-2d-matrix)
- **Difficulty**: Medium
- **Pattern**: Binary Search

---

## Problem Description
You are given an $m \times n$ integer matrix `matrix` with the following two properties:
- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in `matrix` or `false` otherwise.

Must write a solution in $\mathcal{O}(\log(m \cdot n))$ time complexity.

---

## Strategy & Approach
Because the rows are sequentially ordered, the entire $m \times n$ grid behaves as a single sorted 1D array of length $m \cdot n$:
1. **Pointers**: Initialize `left = 0` and `right = (row * cols) - 1`.
2. **Coordinate Mapping**: For any 1D midpoint `mid`:
   - $\text{element\_row} = \text{mid} // \text{cols}$
   - $\text{element\_col} = \text{mid} \% \text{cols}$
3. **Binary Search**:
   - If `matrix[element_row][element_col] == target`: return `True`.
   - If greater than `target`: search left half (`right = mid - 1`).
   - If less than `target`: search right half (`left = mid + 1`).
4. Return `False` if pointers cross without finding `target`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(\log(m \cdot n))$ — Standard binary search over a virtual array of size $m \cdot n$.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant extra space using index arithmetic without copying or flattening the matrix.
