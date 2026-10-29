# Kth Smallest Element in a BST

- **Source**: LeetCode 230 / NeetCode 150
- **Links**: [LeetCode #230](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | [NeetCode](https://neetcode.io/problems/kth-smallest-integer-in-bst)
- **Difficulty**: Medium
- **Pattern**: Trees (BST Properties / In-Order Traversal / Iterative Stack)

---

## Problem Description
Given the `root` of a binary search tree, and an integer `k`, return the $k$-th smallest value (**1-indexed**) of all the values of the nodes in the tree.

### Example 1
```text
    3
   / \
  1   4
   \
    2

Input: root = [3,1,4,null,2], k = 1
Output: 1
```

### Example 2
```text
        5
       / \
      3   6
     / \
    2   4
   /
  1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

### Constraints
- The number of nodes in the tree is $n$.
- $1 \le k \le n \le 10^4$
- $0 \le \text{Node.val} \le 10^4$

---

## Strategy & Approach
A key property of a **Binary Search Tree (BST)** is that an **in-order traversal** ($\text{Left} \to \text{Node} \to \text{Right}$) visits all node values in strictly ascending sorted order.

Instead of performing a full traversal and storing all elements in an array ($\mathcal{O}(n)$ time and space), we perform an **iterative in-order traversal using an explicit stack**:
1. Initialize an empty stack `my_stack = []` and pointer `curr = root`.
2. Push all nodes along the left spine to the stack (`curr = curr.left`).
3. Pop the topmost node from the stack (`curr = my_stack.pop()`). This represents the next smallest element in sorted order.
4. Decrement $k$: `k -= 1`.
5. If $k == 0$, we have reached the $k$-th smallest element; return `curr.val` immediately (**early exit**).
6. Shift to the right child: `curr = curr.right` and repeat.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(h + k)$ — We traverse down to the leftmost leaf in $\mathcal{O}(h)$ time, and then visit only the first $k$ nodes in in-order sequence before terminating early. In the worst case (skewed tree or $k = n$), this is $\mathcal{O}(n)$.
- **Space Complexity**: $\mathcal{O}(h)$ — The stack stores at most the height of the tree $h$ nodes at any point ($\mathcal{O}(\log n)$ for a balanced BST, $\mathcal{O}(n)$ for a skewed tree).

---

## Edge Cases Considered
- **$k = 1$**: Early exit after popping the first leftmost leaf.
- **$k = n$**: Traversal proceeds until the largest element (rightmost node).
- **Single-node tree**: Stack pushes and immediately pops node, returning its value.

