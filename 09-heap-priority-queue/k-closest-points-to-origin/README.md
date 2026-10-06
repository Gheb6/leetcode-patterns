# K Closest Points to Origin

- **Source**: LeetCode 973 / NeetCode 150
- **Links**: [LeetCode #973](https://leetcode.com/problems/k-closest-points-to-origin/) | [NeetCode](https://neetcode.io/problems/k-closest-points-to-origin)
- **Difficulty**: Medium
- **Pattern**: Heap / Priority Queue (Max-Heap of size $k$)

---

## Problem Description
Given an array of `points` where `points[i] = [x_i, y_i]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

The distance between two points on the X-Y plane is the Euclidean distance: $\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$. You may return the answer in **any order**.

---

## Intuition & Approach
- The squared Euclidean distance $x^2 + y^2$ is strictly monotonic with respect to distance, so taking square roots is unnecessary.
- To keep the $k$ closest points dynamically, maintain a **Max-Heap** bounded to size $k$:
  - Negate distances to simulate a max-heap using Python's min-heap (`heapq`).
  - Push the first $k$ points.
  - For subsequent points, if the distance is smaller than the largest distance currently in the heap (i.e. negated distance is greater), replace the top element using `heapq.heappushpop()`.
- Extract and return the $k$ points from the heap.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n \log k)$ — Pushing and popping from a heap of size $k$ for each of the $n$ points.
- **Space Complexity**: $\mathcal{O}(k)$ — The heap holds at most $k$ elements.
