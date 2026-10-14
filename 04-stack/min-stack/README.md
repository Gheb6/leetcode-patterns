# Min Stack

- **Source**: LeetCode 155 / NeetCode 150
- **Links**: [LeetCode #155](https://leetcode.com/problems/min-stack/) | [NeetCode](https://neetcode.io/problems/minimum-stack)
- **Difficulty**: Medium
- **Pattern**: Stack

---

## Problem Description
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:
- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with $\mathcal{O}(1)$ time complexity for each function.

---

## Strategy & Approach
We use two parallel stacks to track elements alongside their running minimums:
1. **`main_stack`**: Stores all pushed values in standard LIFO order.
2. **`min_stack`**: Stores the minimum value encountered up to the current stack height.
   - When pushing `val`, append `min(val, min_stack[-1])` to `min_stack`.
   - When popping, pop from both stacks simultaneously to keep them synchronized.
3. **Retrieval**:
   - `top()` returns `main_stack[-1]`.
   - `getMin()` returns `min_stack[-1]` in $\mathcal{O}(1)$ without recalculating.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(1)$ for all operations (`push`, `pop`, `top`, `getMin`).
- **Space Complexity**: $\mathcal{O}(n)$ — each pushed value takes an entry in both `main_stack` and `min_stack`.
