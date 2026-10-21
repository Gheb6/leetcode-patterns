# Copy List with Random Pointer

- **Source**: LeetCode 138 / NeetCode 150
- **Links**: [LeetCode #138](https://leetcode.com/problems/copy-list-with-random-pointer/) | [NeetCode](https://neetcode.io/problems/copy-linked-list-with-random-pointer)
- **Difficulty**: Medium
- **Pattern**: Linked List (Hash Map / Two-Pass Clone)

---

## Problem Description
A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.

Construct a **deep copy** of the list. The deep copy should consist of exactly `n` **brand new** nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. **None of the pointers in the new list should point to nodes in the original list**.

For example, if there are two nodes `X` and `Y` in the original list, where `X.random --> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random --> y`.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of `n` nodes. Each node is represented as a pair of `[val, random_index]` where:
- `val`: an integer representing `Node.val`
- `random_index`: the index of the node (range from `0` to `n-1`) that the `random` pointer points to, or `null` if it does not point to any node.

Your code will **only** be given the `head` of the original linked list.

### Example 1
```text
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

### Example 2
```text
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
```

### Example 3
```text
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
```

### Constraints
- $0 \le n \le 1000$
- $-10^4 \le \text{Node.val} \le 10^4$
- `Node.random` is `null` or is pointing to some node in the linked list.

---

## Intuition & Approach
A simple traversal cannot clone `random` pointers in one pass because a `random` pointer might refer to a node that has not yet been visited/created.

### Two-Pass Hash Map Approach (Optimal & Clean):
1. **Pass 1 — Create Node Copies**:
   - Traverse the original list node by node.
   - For each original node `curr`, create a clone `Node(curr.val)` and map `nodes[curr] = clone`.
   - Explicitly define `nodes[None] = None` so that `next` or `random` pointing to `None` resolves naturally without key errors.
2. **Pass 2 — Wire Next and Random Pointers**:
   - Traverse the original list again:
     - Retrieve the copied node `copy = nodes[curr]`.
     - Assign `copy.next = nodes[curr.next]`.
     - Assign `copy.random = nodes[curr.random]`.
3. Return `nodes[head]`.

*(Note: An $\mathcal{O}(1)$ space approach exists by interweaving cloned nodes directly between original nodes: `A -> A' -> B -> B'`, but the hash map solution is clean, robust, and avoids mutating the input list during intermediate steps).*

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Two linear passes over the linked list of length $n$. Hash map operations are $\mathcal{O}(1)$ on average.
- **Space Complexity**: $\mathcal{O}(n)$ — The hash map `nodes` stores $n$ entries mapping each original node reference to its newly allocated clone.

---

## Edge Cases Considered
- **Empty list** (`head = None`): `nodes[None] = None` handles this cleanly and returns `None`.
- **Node pointing to itself** (`curr.random == curr`): The map maps `curr` to `copy`, correctly setting `copy.random = copy`.
- **All random pointers are `None`**: Resolves to `None` without requiring conditional checks.
- **Cycle in random pointers**: Handled naturally since all node instances are already created in Pass 1.
