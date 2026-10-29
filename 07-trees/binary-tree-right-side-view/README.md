# Binary Tree Right Side View

- **Source**: LeetCode 199 / NeetCode 150
- **Links**: [LeetCode #199](https://leetcode.com/problems/binary-tree-right-side-view/) | [NeetCode](https://neetcode.io/problems/binary-tree-right-side-view)
- **Difficulty**: Medium
- **Pattern**: Trees (BFS / Level Order / Queue)

---

## Problem Description
Given the `root` of a binary tree, imagine yourself standing on the **right side** of it, return the values of the nodes you can see ordered from top to bottom.

### Example 1
```text
      1            <--- 1
    /   \
   2     3         <--- 3
    \     \
     5     4       <--- 4

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```

### Example 2
```text
      1            <--- 1
       \
        3          <--- 3

Input: root = [1,null,3]
Output: [1,3]
```

### Example 3
```text
Input: root = []
Output: []
```

### Constraints
- The number of nodes in the tree is in the range $[0, 100]$.
- $-100 \le \text{Node.val} \le 100$

---

## Strategy & Approach
We use **Breadth-First Search (BFS)** with a queue to traverse the tree level by level:
1. **Edge Case**: If `root` is `None`, return `[]`.
2. **Queue Setup**: Initialize a `deque` containing `root`.
3. **Level Processing**:
   - At each level, determine the number of nodes at this depth: `level_size = len(levels)`.
   - Iterate through `range(level_size)`:
     - Pop the front node: `node = levels.popleft()`.
     - Enqueue left and right children if present.
     - If `i == level_size - 1`, this node is the **rightmost node** of the current level; append its value to `res`.
4. Return `res`.

> **Note**: A common misconception is that the right side view simply follows `node.right`. If the left subtree is deeper than the right subtree, lower nodes from the left subtree will be visible from the right side once the right subtree terminates. BFS level-by-level processing naturally handles this.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Each node in the tree is enqueued and dequeued exactly once.
- **Space Complexity**: $\mathcal{O}(n)$ — In the worst case (full binary tree), the queue holds up to $\lceil n/2 \rceil$ nodes at the deepest level.

---

## Edge Cases Considered
- **Empty tree** (`root = None`): Directly returns `[]`.
- **Single node** (`root = [1]`): Returns `[1]`.
- **Left subtree deeper than right subtree**: Lower left-descendant nodes are correctly included when the right side has no nodes at those depths.

