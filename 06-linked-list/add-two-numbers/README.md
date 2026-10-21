# Add Two Numbers

- **Source**: LeetCode 2 / NeetCode 150
- **Links**: [LeetCode #2](https://leetcode.com/problems/add-two-numbers/) | [NeetCode](https://neetcode.io/problems/add-two-numbers)
- **Difficulty**: Medium
- **Pattern**: Linked List (Simulation / Elementary Math / Dummy Node)

---

## Problem Description
You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

### Example 1
```text
Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
Output: [7, 0, 8]
Explanation: 342 + 465 = 807.
```

### Example 2
```text
Input: l1 = [0], l2 = [0]
Output: [0]
```

### Example 3
```text
Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
Output: [8, 9, 9, 9, 0, 0, 0, 1]
```

### Constraints
- The number of nodes in each linked list is in the range `[1, 100]`.
- $0 \le \text{Node.val} \le 9$
- It is guaranteed that the list represents a number that does not have leading zeros.

---

## Intuition & Approach
Because the digits are stored in **reverse order** (the least significant digit is at the head of the list), we can simulate standard column-by-column addition directly from head to tail:

1. **Dummy Head & Pointers**:
   - Create a dummy head `head = ListNode(0)` and a traversal pointer `dummy = head`.
   - Maintain a `carry` variable initialized to `0`.
2. **Iterative Digit Addition**:
   - Loop as long as there is an unvisited node in `l1`, an unvisited node in `l2`, or a remaining non-zero `carry`:
     - Extract `val_1 = curr_1.val` if `curr_1` exists, otherwise `0`.
     - Extract `val_2 = curr_2.val` if `curr_2` exists, otherwise `0`.
     - Sum the values plus the previous carry: `summation = val_1 + val_2 + carry`.
     - Calculate the new carry: `carry = summation // 10`.
     - Create a new node with `summation % 10` and append it to `dummy.next`.
     - Advance `dummy` and advance `curr_1` / `curr_2` if they are not `None`.
3. **Return Result**:
   - `head.next` points to the head of the newly created sum linked list.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(\max(m, n))$ — Where $m$ and $n$ are the lengths of `l1` and `l2` respectively. The loop runs at most $\max(m, n) + 1$ times.
- **Space Complexity**: $\mathcal{O}(\max(m, n))$ — Space allocated for the output linked list which has at most $\max(m, n) + 1$ nodes.

---

## Edge Cases Considered
- **Lists of different lengths** (e.g. `[9, 9, 9]` and `[1]`): Gracefully treated missing nodes as `0`.
- **Final carry creates a new node** (e.g. `5 + 5 = 10`): Loop condition `carry != 0` ensures the trailing carry is appended as a node.
- **Single-node zeroes** (`[0] + [0]`): Produces a single node `[0]`.
- **Chained carries across multiple 9s** (e.g. `9999 + 1 = 10000`).
