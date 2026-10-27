# Lowest Common Ancestor of a Binary Search Tree

- **Source**: LeetCode 235 / NeetCode 150
- **Links**: [LeetCode #235](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | [NeetCode](https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree)
- **Difficulty**: Medium
- **Pattern**: Trees (BST Properties / Binary Search Tree Traversal)

---

## Problem Description
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the **definition of LCA on Wikipedia**: “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”

### Example 1
```text
        6
      /   \
     2     8
    / \   / \
   0   4 7   9
      / \
     3   5

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
```

### Example 2
```text
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
```

### Example 3
```text
Input: root = [2,1], p = 2, q = 1
Output: 2
```

### Constraints
- The number of nodes in the tree is in the range $[2, 10^5]$.
- $-10^9 \le \text{Node.val} \le 10^9$
- All `Node.val` are **unique**.
- `p != q`
- `p` and `q` will exist in the BST.

---

## Strategy & Approach
We leverage the core property of a **Binary Search Tree (BST)**:
- For any node `curr`, all values in its left subtree are strictly smaller than `curr.val`, and all values in its right subtree are strictly greater than `curr.val`.

Starting at `curr = root`:
1. **Both nodes in left subtree**: If `p.val < curr.val and q.val < curr.val`, the LCA must be located in the left subtree: `curr = curr.left`.
2. **Both nodes in right subtree**: If `p.val > curr.val and q.val > curr.val`, the LCA must be located in the right subtree: `curr = curr.right`.
3. **Split Point found**: If one value is less than or equal to `curr.val` and the other is greater than or equal to `curr.val` (or one of them equals `curr.val`), `curr` is the **first split point** where paths to `p` and `q` diverge. Thus, `curr` is the Lowest Common Ancestor: return `curr`.

By using an iterative `while` loop, this traversal operates in $\mathcal{O}(1)$ auxiliary space without recursion stack overhead.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(h)$ — In each step we move down one level of the BST. The maximum number of steps is the height of the tree $h$ ($\mathcal{O}(\log n)$ for a balanced BST, $\mathcal{O}(n)$ in the worst case for a completely skewed tree).
- **Space Complexity**: $\mathcal{O}(1)$ — The iterative approach uses constant extra memory.

---

## Edge Cases Considered
- **One node is ancestor of the other** (e.g. `p = 2`, `q = 4`): The condition triggers the `else` branch when `curr.val == p.val`, correctly returning node 2.
- **Tree of minimum size (2 nodes)**: Handled without null pointer exceptions.
