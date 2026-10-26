# Maximum Depth of Binary Tree

- **Source**: LeetCode 104 / NeetCode 150
- **Links**: [LeetCode #104](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [NeetCode](https://neetcode.io/problems/depth-of-binary-tree)
- **Difficulty**: Easy
- **Pattern**: Trees (DFS / Post-Order Recursion)

---

## Problem Description
Given the `root` of a binary tree, return its maximum depth.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

---

## Strategy & Approach
- **Base Case**: If `root` is `None` (empty subtree), the depth is `0`.
- **Recursive Step (DFS / Post-Order)**:
  - Recursively compute the maximum depth of the left subtree: `maxDepth(root.left)`.
  - Recursively compute the maximum depth of the right subtree: `maxDepth(root.right)`.
  - The maximum depth at the current node is `max(left_depth, right_depth) + 1`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Every node in the binary tree is visited exactly once.
- **Space Complexity**: $\mathcal{O}(h)$ — Determined by the height of the recursive call stack, where $h$ is the height of the tree ($\mathcal{O}(\log n)$ for a balanced tree, $\mathcal{O}(n)$ in the worst case for a completely skewed tree).
