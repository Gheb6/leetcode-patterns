# Subtree of Another Tree

- **Source**: LeetCode 572 / NeetCode 150
- **Links**: [LeetCode #572](https://leetcode.com/problems/subtree-of-another-tree/) | [NeetCode](https://neetcode.io/problems/subtree-of-a-binary-tree)
- **Difficulty**: Easy
- **Pattern**: Trees (DFS / Tree Traversal)

---

## Problem Description
Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.

A **subtree** of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

### Example 1
```text
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
```

### Example 2
```text
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
```

### Constraints
- The number of nodes in the `root` tree is in the range `[1, 2000]`.
- The number of nodes in the `subRoot` tree is in the range `[1, 1000]`.
- $-10^4 \le \text{root.val} \le 10^4$
- $-10^4 \le \text{subRoot.val} \le 10^4$

---

## Strategy & Approach
We formulate the solution using a recursive tree traversal combined with a helper function:
1. **Helper `isSameTree(tree_1, tree_2)`**:
   - Compares two trees structurally and by value.
   - If both nodes are `None`, returns `True`.
   - If one is `None` while the other is not, or if values differ, returns `False`.
   - Recursively verifies both left and right children.
2. **Main Function `isSubtree(root, subRoot)`**:
   - If `subRoot` is `None`, an empty tree is always a valid subtree: return `True`.
   - If `root` is `None` (and `subRoot` is not), `subRoot` cannot be found: return `False`.
   - If `isSameTree(root, subRoot)` evaluates to `True`, a match is found: return `True`.
   - Otherwise, recursively check the left and right subtrees of `root`:
     `self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(m \cdot n)$ — In the worst case, for each of the $m$ nodes in `root`, we compare up to $n$ nodes of `subRoot` using `isSameTree`.
- **Space Complexity**: $\mathcal{O}(h)$ — Maximum memory on the recursion stack is bounded by the height of `root` ($h_{\text{root}}$) plus the height of `subRoot` ($h_{\text{subRoot}}$).

---

## Edge Cases Considered
- **`subRoot` is empty**: Handled by `if not subRoot: return True`.
- **`root` is empty with non-empty `subRoot`**: Handled by `elif not root: return False`.
- **Extra child in `root`**: Example 2 verifies that descendants must match exactly (cannot have extra leaves in `root`'s subtree).
