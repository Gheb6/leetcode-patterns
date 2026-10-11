# Invert Binary Tree

- **Source**: LeetCode 226 / NeetCode 150
- **Links**: [LeetCode #226](https://leetcode.com/problems/invert-binary-tree/) | [NeetCode](https://neetcode.io/problems/invert-a-binary-tree)
- **Difficulty**: Easy
- **Pattern**: Trees (DFS / Recursion)

---

## Problem Description
Given the `root` of a binary tree, invert the tree, and return its root.

---

## Strategy & Approach
- **Base Case**: If `root` is `None`, return `None`.
- **Swap Children**: Swap `root.left` and `root.right` in-place.
- **Recursive Step**: Recursively call `invertTree` on the new left and right subtrees.
- Return the modified `root`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — We visit every node in the binary tree exactly once.
- **Space Complexity**: $\mathcal{O}(h)$ — Maximum depth of the recursion call stack, where $h$ is the height of the tree ($\mathcal{O}(\log n)$ for a balanced tree, $\mathcal{O}(n)$ for a skewed tree).
