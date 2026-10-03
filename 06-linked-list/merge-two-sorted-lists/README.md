# Merge Two Sorted Lists

- **Source**: LeetCode 21 / NeetCode 150
- **Links**: [LeetCode #21](https://leetcode.com/problems/merge-two-sorted-lists/) | [NeetCode](https://neetcode.io/problems/merge-two-sorted-linked-lists)
- **Difficulty**: Easy
- **Pattern**: Linked List (Two Pointers / Dummy Node)

---

## Problem Description
You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

### Example 1
```text
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

### Example 2
```text
Input: list1 = [], list2 = []
Output: []
```

### Example 3
```text
Input: list1 = [], list2 = [0]
Output: [0]
```

### Constraints
- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in non-decreasing order.

---

## Intuition & Approach
1. Use a **dummy head node** to avoid handling edge cases when selecting the very first node of the merged list.
2. Maintain a `tail` pointer pointing to the last merged node.
3. Compare the current values of `head_1` and `head_2`:
   - Append the smaller node to `tail.next`.
   - Advance the pointer of the chosen list.
   - Advance `tail`.
4. Once one list is exhausted, directly link the remainder of the other list to `tail.next`.
5. Return `dummy.next`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n + m)$ — Where $n$ and $m$ are the lengths of `list1` and `list2`. We traverse each node at most once.
- **Space Complexity**: $\mathcal{O}(1)$ — In-place pointer rearrangement without allocating new list nodes.

---

## Edge Cases Considered
- Both lists are empty.
- One list is empty while the other has elements.
- Lists of different lengths.
- Lists with identical values / duplicates.

---

## Key Takeaways / Patterns
- A **dummy head** simplifies linked list construction by removing boundary checks for the head node.
- In-place splicing avoids allocating extra node memory.
