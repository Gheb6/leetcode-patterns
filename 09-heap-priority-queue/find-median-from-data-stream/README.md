# Find Median from Data Stream

- **Source**: LeetCode 295 / NeetCode 150
- **Links**: [LeetCode #295](https://leetcode.com/problems/find-median-from-data-stream/) | [NeetCode](https://neetcode.io/problems/find-median-in-a-data-stream)
- **Difficulty**: Hard
- **Pattern**: Heap / Priority Queue (Two Heaps)

---

## Problem Description
The **median** is the middle value in an ordered integer list. If the size of the list is even, the median is the mean of the two middle values.

Implement the `MedianFinder` class:
- `MedianFinder()`: initializes the object.
- `void addNum(int num)`: adds the integer `num` from the data stream.
- `double findMedian()`: returns the median of all elements so far.

---

## Strategy & Approach
Maintain two heaps to divide numbers into two halves:
1. `max_heap`: stores the smaller half of numbers (inverted values for Python's min-heap).
2. `min_heap`: stores the larger half of numbers.

**Balancing Invariant**:
- Filter every incoming number through `max_heap` into `min_heap`.
- If `len(min_heap) > len(max_heap)`, move the smallest element of `min_heap` back to `max_heap`.
- Thus, `max_heap` either contains the exact same number of elements or 1 extra element.

**Median Calculation**:
- If total count is even, average the tops of both heaps.
- If odd, the top of `max_heap` is the median.

---

## Complexity Analysis
- **Time Complexity**:
  - `addNum`: $\mathcal{O}(\log n)$ — heap insertion and deletion operations.
  - `findMedian`: $\mathcal{O}(1)$ — constant-time peek at the root of the heap(s).
- **Space Complexity**: $\mathcal{O}(n)$ — stores all $n$ numbers across the two heaps.
