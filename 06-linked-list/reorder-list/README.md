# Reorder List

- **Source**: LeetCode 143 / NeetCode 150
- **Links**: [LeetCode #143](https://leetcode.com/problems/reorder-list/) | [NeetCode](https://neetcode.io/problems/reorder-linked-list)
- **Difficulty**: Medium
- **Pattern**: Linked List (Fast & Slow Pointers / In-Place Reversal)

---

## Problem Description
You are given the head of a singly linked-list:
$L_0 \rightarrow L_1 \rightarrow \dots \rightarrow L_{n-1} \rightarrow L_n$

Reorder the list to be on the following form:
$L_0 \rightarrow L_n \rightarrow L_1 \rightarrow L_{n-1} \rightarrow L_2 \rightarrow L_{n-2} \rightarrow \dots$

You may not modify the values in the list's nodes. Only nodes themselves may be changed in-place.

---

## Strategy & Approach
This problem decomposes cleanly into three sub-problems:
1. **Find the Middle**: Use fast and slow pointers (`slow` moves 1 step, `fast` moves 2 steps) to locate the midpoint of the linked list.
2. **Reverse the Second Half**: Split the list at `slow.next = None` and reverse the second half in-place using standard three-pointer reversal (`prev`, `curr`, `next_node`).
3. **Merge the Halves**: Interleave nodes alternately from the first half and the reversed second half.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — $\mathcal{O}(n)$ to find the middle, $\mathcal{O}(n)$ to reverse the second half, and $\mathcal{O}(n)$ to merge.
- **Space Complexity**: $\mathcal{O}(1)$ — Mutates node pointers directly in-place without additional data structures.

---

## Edge Cases Considered
- Single node list (`head.next is None`): already reordered.
- Two-node list: order remains identical.
- Odd vs. even length lists handled by pointer split at the midpoint.
