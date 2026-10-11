# Kth Largest Element in a Stream

- **Source**: LeetCode 703 / NeetCode 150
- **Links**: [LeetCode #703](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | [NeetCode](https://neetcode.io/problems/kth-largest-element-in-a-stream)
- **Difficulty**: Easy
- **Pattern**: Heap / Priority Queue (Min-Heap of Size K)

---

## Problem Description
Design a class to find the $k^{\text{th}}$ largest element in a stream. Note that it is the $k^{\text{th}}$ largest element in sorted order, not the $k^{\text{th}}$ distinct element.

Implement `KthLargest`:
- `KthLargest(int k, int[] nums)`: initializes the object with the integer `k` and the stream of integers `nums`.
- `int add(int val)`: appends the integer `val` to the stream and returns the element representing the $k^{\text{th}}$ largest element in the stream.

---

## Strategy & Approach
We maintain a **min-heap of size at most $k$**:
1. **Initialization (`__init__`)**:
   - Heapify `nums` in $\mathcal{O}(n)$ time.
   - Pop the smallest elements until the heap size reduces to $k$.
2. **Adding Elements (`add`)**:
   - Push `val` into the heap.
   - If the size exceeds $k$, pop the smallest element (`heapq.heappop`).
   - The top of the min-heap (`min_heap[0]`) is guaranteed to be the $k^{\text{th}}$ largest element.

---

## Complexity Analysis
- **Time Complexity**:
  - `__init__`: $\mathcal{O}(n + (n - k) \log n)$ where $n = \text{len}(nums)$.
  - `add`: $\mathcal{O}(\log k)$ — since the heap size never exceeds $k + 1$.
- **Space Complexity**: $\mathcal{O}(k)$ — at most $k$ elements are kept in the min-heap.
