# Validate Binary Search Tree

- **Source**: LeetCode 98 / NeetCode 150
- **Links**: [LeetCode #98](https://leetcode.com/problems/validate-binary-search-tree/) | [NeetCode](https://neetcode.io/problems/valid-binary-search-tree)
- **Difficulty**: Medium
- **Pattern**: Trees (BST Properties / DFS Range Validation)

---

## Problem Description
Given the `root` of a binary tree, *determine if it is a valid binary search tree (BST)*.

A **valid BST** is defined as follows:
- The left subtree of a node contains only nodes with keys **strictly less than** the node's key.
- The right subtree of a node contains only nodes with keys **strictly greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

### Example 1
```text
    2
   / \
  1   3

Input: root = [2,1,3]
Output: true
```

### Example 2
```text
    5
   / \
  1   4
     / \
    3   6

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

### Constraints
- The number of nodes in the tree is in the range $[1, 10^4]$.
- $-2^{31} \le \text{Node.val} \le 2^{31} - 1$

---

## Strategy & Approach
A common pitfall is merely verifying that `node.left.val < node.val` and `node.right.val > node.val` locally. A valid BST requires that **all** nodes in the left subtree are smaller than `node.val` and **all** nodes in the right subtree are larger than `node.val`.

### 1. DFS Range Validation (Recursive)
We carry valid lower and upper bounds `(low, high)` down the recursive traversal:
- Base case: If `node is None`, return `True`.
- Validity check: If `node.val <= low` or `node.val >= high`, the tree violates the strict BST ordering constraint: return `False`.
- Recurse on subtrees with updated bounds:
  - Left child must satisfy: `(low, node.val)`
  - Right child must satisfy: `(node.val, high)`
- Return `valid(node.left, low, node.val) and valid(node.right, node.val, high)`.

### 2. Iterative In-Order Traversal (Alternative)
An in-order traversal of a BST must visit elements in strictly increasing order (`curr.val > prev`). Using an explicit stack, we track `prev` and return `False` if any node violates `curr.val <= prev`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Every node is visited at most once.
- **Space Complexity**: $\mathcal{O}(h)$ — Memory on the recursive call stack bounded by the tree height $h$ ($\mathcal{O}(\log n)$ for a balanced tree, $\mathcal{O}(n)$ for a skewed tree).

---

## Edge Cases Considered
- **Duplicate values** (e.g., `[2, 2, 2]`): The condition `node.val <= low or node.val >= high` strictly rejects duplicates as required.
- **Extreme integer limits** ($-2^{31}$ to $2^{31}-1$): Using floating-point infinities (`-float('inf')` and `float('inf')`) avoids boundary collisions.
- **Single-node tree**: Base case succeeds and returns `True`.

