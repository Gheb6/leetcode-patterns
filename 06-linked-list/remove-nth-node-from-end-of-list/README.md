# Remove Nth Node From End of List

- **Source**: LeetCode 19 / NeetCode 150
- **Links**: [LeetCode #19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | [NeetCode](https://neetcode.io/problems/remove-node-from-end-of-linked-list)
- **Difficulty**: Medium
- **Pattern**: Linked List (Two Pointers / Fast & Slow / Dummy Node)

---

## Problem Description
Given the `head` of a linked list, remove the $n^{\text{th}}$ node from the end of the list and return its head.

### Example 1
```text
Input: head = [1, 2, 3, 4, 5], n = 2
Output: [1, 2, 3, 5]
```

### Example 2
```text
Input: head = [1], n = 1
Output: []
```

### Example 3
```text
Input: head = [1, 2], n = 1
Output: [1]
```

### Constraints
- The number of nodes in the list is `sz`.
- $1 \le \text{sz} \le 30$
- $0 \le \text{Node.val} \le 100$
- $1 \le n \le \text{sz}$

---

## Intuition & Approach
- **Two-Pass Approach**: First pass counts the total length $L$ of the linked list. Second pass traverses to the $(L - n)^{\text{th}}$ node and removes the next node. Takes $\mathcal{O}(L)$ time with two traversals.
- **One-Pass Approach (Optimal with Two Pointers & Dummy Node)**:
  1. Create a `dummy` node pointing to `head` (`dummy = ListNode(0, head)`). This handles edge cases cleanly (such as deleting the head itself when $n = \text{sz}$).
  2. Set `left = dummy` and `right = head`.
  3. Advance `right` by $n$ steps ahead. Now the gap between `left` and `right` is exactly $n$ nodes.
  4. Advance both `left` and `right` one step at a time until `right` reaches `None`.
  5. At this point, `left` points to the node **directly preceding** the $n^{\text{th}}$ node from the end.
  6. Delete the target node by updating `left.next = left.next.next`.
  7. Return `dummy.next`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(L)$ — Single traversal of the linked list of length $L$.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant auxiliary space without allocating additional list nodes.

---

## Edge Cases Considered
- **Removing the head node** ($n = \text{sz}$): Handled seamlessly via the `dummy` node (`dummy.next` points to the new head).
- **Removing the tail node** ($n = 1$): `left.next = None` correctly unlinks the final node.
- **Single-node list** (`head = [1], n = 1`): Deletes the node and returns `None` (`[]`).
- **Two-node list**: Removing either head ($n = 2$) or tail ($n = 1$) behaves properly.
