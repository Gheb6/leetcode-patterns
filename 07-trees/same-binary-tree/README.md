# Same Binary Tree

- **Source**: LeetCode 100 / NeetCode 150
- **Links**: [LeetCode #100](https://leetcode.com/problems/same-tree/) | [NeetCode](https://neetcode.io/problems/same-binary-tree)
- **Difficulty**: Easy
- **Pattern**: Trees (DFS / Tree Traversal)

---

## Problem Description
Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

### Example 1
```text
Input: p = [1,2,3], q = [1,2,3]
Output: true
```

### Example 2
```text
Input: p = [1,2], q = [1,null,2]
Output: false
```

### Example 3
```text
Input: p = [1,2,1], q = [1,1,2]
Output: false
```

### Constraints
- The number of nodes in both trees is in the range `[0, 100]`.
- $-10^4 \le \text{Node.val} \le 10^4$

---

## Strategy & Approach
We use recursive Depth-First Search (DFS) to traverse both trees simultaneously:
1. **Base Case 1 (Both empty)**:
   - If `not p and not q`, both subtrees are empty and thus identical: return `True`.
2. **Base Case 2 (Mismatch)**:
   - If one node is `None` while the other is not (`not p or not q`), or if their values differ (`p.val != q.val`): return `False`.
3. **Recursive Step**:
   - Recursively verify that both left subtrees are identical AND both right subtrees are identical:
     `self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)`

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — In the worst case (when the trees are identical), every node in both trees is visited once, where $n = \min(|p|, |q|)$.
- **Space Complexity**: $\mathcal{O}(h)$ — Memory used by the recursive call stack, where $h$ is the height of the trees ($\mathcal{O}(\log n)$ for balanced trees, $\mathcal{O}(n)$ in the worst case for skewed trees).

---

## Edge Cases Considered
- **Both trees are empty** (`p = None, q = None`): Correctly returns `True`.
- **One tree is empty, one is not**: Correctly returns `False`.
- **Identical structures but different values**: Detected by `p.val != q.val`.
- **Different structural configurations with same values**: Detected by the asymmetry in `None` checks.
