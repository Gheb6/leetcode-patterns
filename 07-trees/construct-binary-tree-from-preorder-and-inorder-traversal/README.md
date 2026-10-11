# Construct Binary Tree from Preorder and Inorder Traversal

- **Source**: LeetCode 105 / NeetCode 150
- **Links**: [LeetCode #105](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | [NeetCode](https://neetcode.io/problems/binary-tree-from-preorder-and-inorder-traversal)
- **Difficulty**: Medium
- **Pattern**: Trees (Divide & Conquer / Hash Map)

---

## Problem Description
Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

---

## Strategy & Approach
1. **Properties of Traversals**:
   - `preorder` follows `[Root, Left, Right]`: the current root is always the next available element in `preorder`.
   - `inorder` follows `[Left, Root, Right]`: elements to the left of `root` belong to the left subtree, and elements to the right belong to the right subtree.
2. **Fast Lookup with Hash Map**:
   - Build a hash map `inorder_map` mapping each value to its index in `inorder` for $\mathcal{O}(1)$ position lookup.
3. **Recursive Division**:
   - Increment `pre_idx` to pick the current root node.
   - Use `mid = inorder_map[root_val]` to split the inorder boundary `[in_left, in_right]`.
   - Recursively construct the left subtree from `[in_left, mid - 1]`.
   - Recursively construct the right subtree from `[mid + 1, in_right]`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Building `inorder_map` takes $\mathcal{O}(n)$, and each of the $n$ nodes is created in $\mathcal{O}(1)$ time using the index map.
- **Space Complexity**: $\mathcal{O}(n)$ — $\mathcal{O}(n)$ space for the hash map, plus $\mathcal{O}(h)$ recursion call stack space where $h \le n$.
