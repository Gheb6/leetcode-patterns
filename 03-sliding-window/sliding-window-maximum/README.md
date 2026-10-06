# Sliding Window Maximum

- **Source**: LeetCode 239 / NeetCode 150
- **Links**: [LeetCode #239](https://leetcode.com/problems/sliding-window-maximum/) | [NeetCode](https://neetcode.io/problems/sliding-window-maximum)
- **Difficulty**: Hard
- **Pattern**: Sliding Window (Monotonic Deque)

---

## Problem Description
You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

---

## Intuition & Approach
- Maintain a **monotonically decreasing deque** storing indices of elements.
- For each element `num` at index `i`:
  1. **Evict out-of-bound indices**: If `my_deque and my_deque[0] <= i - k`, pop from the left.
  2. **Maintain monotonicity**: While `nums[my_deque[-1]] < num`, pop from the right (smaller elements can never be the maximum in this or subsequent windows).
  3. **Push current index**: Append `i` to the right.
  4. **Record maximum**: Once `i >= k - 1`, append `nums[my_deque[0]]` to the result.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Each index is pushed and popped from the deque at most once.
- **Space Complexity**: $\mathcal{O}(k)$ auxiliary space — The deque holds at most $k$ indices.
