# Reverse Linked List

- **Source**: LeetCode 206 / NeetCode 150
- **Links**: [LeetCode #206](https://leetcode.com/problems/reverse-linked-list/) | [NeetCode](https://neetcode.io/problems/reverse-a-linked-list)
- **Difficulty**: Easy
- **Pattern**: Linked List (Iterative / Two Pointers)

---

## Problem Description
Given the `head` of a singly linked list, reverse the list, and return the reversed list.

### Example 1
```text
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

### Example 2
```text
Input: head = [1,2]
Output: [2,1]
```

### Example 3
```text
Input: head = []
Output: []
```

### Constraints
- The number of nodes in the list is in the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

---

## Intuition & Approach
To reverse a singly linked list in a single pass without extra memory:
1. Maintain two pointers: `prev` initialized to `None` and `curr` initialized to `head`.
2. At each step:
   - Temporarily save `curr.next` in `next_node` so we don't lose the rest of the list.
   - Reverse the current pointer by pointing `curr.next = prev`.
   - Advance `prev` to `curr`.
   - Advance `curr` to `next_node`.
3. When `curr` becomes `None`, `prev` will be pointing to the new head of the reversed list.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — We visit each of the $n$ nodes exactly once.
- **Space Complexity**: $\mathcal{O}(1)$ — In-place pointer manipulation with no additional data structures.

---

## Edge Cases Considered
- Empty linked list (`head is None`).
- Single node list (remains unchanged).
- Two node list.

---

## Key Takeaways / Patterns
- Three-pointer slide (`prev`, `curr`, `next_node`) is the foundational pattern for linked list mutations in-place.
