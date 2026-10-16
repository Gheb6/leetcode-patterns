# Non-overlapping Intervals

- **Source**: LeetCode 435 / NeetCode 150
- **Links**: [LeetCode #435](https://leetcode.com/problems/non-overlapping-intervals/) | [NeetCode](https://neetcode.io/problems/non-overlapping-intervals)
- **Difficulty**: Medium
- **Pattern**: Intervals (Greedy)

---

## Problem Description
Given an array of intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

> **Note**: Intervals that only touch at a single point, such as `[1, 2]` and `[2, 3]`, are considered **non-overlapping**.

### Example 1
```text
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
```

### Example 2
```text
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to model non-overlapping intervals.
```

### Example 3
```text
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
```

### Constraints
- `1 <= intervals.length <= 10^5`
- `intervals[i].length == 2`
- `-5 * 10^4 <= start_i < end_i <= 5 * 10^4`

---

## Intuition & Approach
This is a classic variation of the **Interval Scheduling** problem. To minimize the number of removals, we want to maximize the number of compatible non-overlapping intervals we keep.

Whenever two intervals overlap, we should greedily **remove the interval with the larger end time**, because keeping the interval that finishes earlier frees up more room for future intervals to not collide.

1. **Sort Intervals**:
   - Sort intervals in ascending order by their start times: `intervals.sort(key=lambda x: x[0])`.

2. **Greedy Traversal**:
   - Initialize `prev_end = intervals[0][1]` to track the finish time of the last retained interval.
   - Initialize `counter = 0` to count removed intervals.
   - For each interval `[start, end]` in `intervals[1:]`:
     - **Overlap (`prev_end > start`)**:
       - The current interval collides with the previous retained interval.
       - Increment `counter += 1`.
       - Greedily retain the one that finishes first:
         $$\text{prev\_end} = \min(\text{end}, \text{prev\_end})$$
     - **No Overlap (`prev_end <= start`)**:
       - Both intervals can coexist without conflict.
       - Update `prev_end = end`.
3. **Return**: Return `counter`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n \log n)$ — Sorting the $n$ intervals takes $\mathcal{O}(n \log n)$ time. The subsequent greedy scan runs in linear $\mathcal{O}(n)$ time.
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space beyond Python's Timsort internal buffer ($\mathcal{O}(n)$).

---

## Edge Cases Considered
- **Adjacent intervals touching at endpoints** (e.g., `[1, 2]` and `[2, 3]`): `prev_end > start` (`2 > 2`) evaluates to `False`, correctly treated as non-overlapping.
- **Identical duplicates** (e.g., `[[1, 2], [1, 2]]`): Overlap is detected and one duplicate is removed.
- **Large interval enclosing a smaller one** (e.g., `[1, 10]` and `[2, 3]`): `min(end, prev_end)` picks `3`, effectively discarding the larger interval `[1, 10]`.
