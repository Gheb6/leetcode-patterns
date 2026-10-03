# Linked List Cycle

- **Source**: LeetCode 141 / NeetCode 150
- **Links**: [LeetCode #141](https://leetcode.com/problems/linked-list-cycle/) | [NeetCode](https://neetcode.io/problems/linked-list-cycle-detection)
- **Difficulty**: Easy
- **Pattern**: Linked List (Fast & Slow Pointers / Floyd's Tortoise and Hare)

---

## Problem Description
Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

### Example 1
```text
Input: head = [3,2,0,-4], pos = 1 (tail connects to node index 1)
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

### Example 2
```text
Input: head = [1,2], pos = 0
Output: true
```

### Example 3
```text
Input: head = [1], pos = -1
Output: false
```

### Constraints
- The number of the nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the linked-list.

---

## Intuition & Approach
Use **Floyd's Tortoise and Hare algorithm** (Fast and Slow Pointers):
1. Initialize two pointers, `slow` and `fast`, both starting at `head`.
2. Move `slow` by 1 step (`slow = slow.next`) and `fast` by 2 steps (`fast = fast.next.next`).
3. If there is no cycle, `fast` or `fast.next` will reach `None`.
4. If there is a cycle, the fast pointer will eventually lap the slow pointer and they will point to the exact same node (`slow == fast`).

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — If there is no cycle, `fast` reaches the end in $n/2$ iterations. If there is a cycle, `fast` catches up to `slow` in at most the cycle's length iterations.
- **Space Complexity**: $\mathcal{O}(1)$ — Only two pointer references are used.

---

## Edge Cases Considered
- Empty linked list (`head is None`).
- Single node without cycle.
- Single node with self-loop.
- Two-node cycle.

---

## Key Takeaways / Patterns
- Floyd's cycle detection detects cycles with $\mathcal{O}(1)$ space instead of storing visited nodes in a hash set ($\mathcal{O}(n)$ space).
