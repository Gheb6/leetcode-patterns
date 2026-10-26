# Diameter of Binary Tree

- **Source**: LeetCode 543 / NeetCode 150
- **Links**: [LeetCode #543](https://leetcode.com/problems/diameter-of-binary-tree/) | [NeetCode](https://neetcode.io/problems/binary-tree-diameter)
- **Difficulty**: Easy
- **Pattern**: Trees (DFS / Post-Order Recursion)

---

## Problem Description
Given the `root` of a binary tree, return the length of the **diameter** of the tree.

The **diameter** of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The length of a path between two nodes is represented by the number of edges between them.

---

## Strategy & Approach
- **Bottom-Up DFS (Post-Order)**:
  - The diameter passing through any node $u$ is the sum of the maximum depth of its left subtree and the maximum depth of its right subtree: $\text{left\_depth} + \text{right\_depth}$.
  - We define a recursive helper `depth(node)`:
    - Base case: If `node` is `None`, return `0`.
    - Recursively compute `left_depth = depth(node.left)` and `right_depth = depth(node.right)`.
    - Update the global maximum diameter with `left_depth + right_depth`.
    - Return the height of the current subtree: `max(left_depth, right_depth) + 1`.
  - The final answer is the maximum diameter found across all nodes.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Every node in the binary tree is visited once.
- **Space Complexity**: $\mathcal{O}(h)$ — Recursive call stack bounded by the tree height $h$ ($\mathcal{O}(\log n)$ for a balanced tree, $\mathcal{O}(n)$ in the worst case for a skewed tree).
