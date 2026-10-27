# Binary Tree Level Order Traversal

- **Source**: LeetCode 102 / NeetCode 150
- **Links**: [LeetCode #102](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [NeetCode](https://neetcode.io/problems/level-order-traversal-of-binary-tree)
- **Difficulty**: Medium
- **Pattern**: Trees (BFS / Queue / Level-Order Traversal)

---

## Problem Description
Given the `root` of a binary tree, return the **level order traversal** of its nodes' values (i.e., from left to right, level by level).

### Example 1
```text
    3
   / \
  9  20
    /  \
   15   7

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

### Example 2
```text
Input: root = [1]
Output: [[1]]
```

### Example 3
```text
Input: root = []
Output: []
```

### Constraints
- The number of nodes in the tree is in the range $[0, 2000]$.
- $-1000 \le \text{Node.val} \le 1000$

---

## Strategy & Approach
We use **Breadth-First Search (BFS)** with a double-ended queue (`collections.deque`):
1. **Edge Case**: If `root` is `None`, return an empty list `[]`.
2. **Queue Initialization**: Initialize `levels = deque([root])`.
3. **Level-by-Level Processing**:
   - While `levels` is not empty, measure the current queue size `len(levels)`. This captures exactly the number of nodes situated on the current level.
   - Iterate through that fixed number of nodes:
     - Pop the front node: `curr = levels.popleft()`.
     - Record its value: `my_list.append(curr.val)`.
     - Push its non-null left and right children to the queue.
   - Append `my_list` representing the completed level into `res`.
4. Return `res`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Every node is pushed and popped from the queue exactly once.
- **Space Complexity**: $\mathcal{O}(n)$ — In the worst case (a full binary tree), the queue holds all the leaf nodes at the deepest level, which is up to $\lceil n/2 \rceil = \mathcal{O}(n)$ nodes.

---

## Edge Cases Considered
- **Empty tree** (`root = None`): Directly returns `[]`.
- **Single node** (`root = [1]`): Returns `[[1]]`.
- **Completely skewed tree** (linked-list like): Each level contains exactly one element; correctly produces $n$ single-element sublists.
