# Balanced Binary Tree

- **Source**: LeetCode 110 / NeetCode 150
- **Links**: [LeetCode #110](https://leetcode.com/problems/balanced-binary-tree/) | [NeetCode](https://neetcode.io/problems/balanced-binary-tree)
- **Difficulty**: Easy
- **Pattern**: Trees (DFS / Bottom-Up Recursion)

---

## Problem Description
Given a binary tree, determine if it is **height-balanced**.

A **height-balanced** binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

---

## Strategy & Approach
- **Bottom-Up DFS**:
  - Instead of repeatedly computing subtree heights at each level ($\mathcal{O}(n^2)$), calculate the height bottom-up in a post-order traversal ($\mathcal{O}(n)$).
  - Define a helper function `get_height(node)`:
    - Base case: If `node` is `None`, return `0`.
    - Recursively compute `left_height` and `right_height`.
    - If either subtree is unbalanced (returns `-1`), propagate `-1` upwards immediately.
    - If $| \text{left\_height} - \text{right\_height} | > 1$, the subtree is unbalanced; return `-1`.
    - Otherwise, return `max(left_height, right_height) + 1`.
  - The tree is balanced if and only if `get_height(root) != -1`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Every node is visited at most once.
- **Space Complexity**: $\mathcal{O}(h)$ — Determined by the height of the recursion call stack, where $h$ is the tree height ($\mathcal{O}(\log n)$ for a balanced tree, $\mathcal{O}(n)$ in the worst case for a skewed tree).
