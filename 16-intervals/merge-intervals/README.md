# Merge Intervals

- **Source**: LeetCode 56 / NeetCode 150
- **Links**: [LeetCode #56](https://leetcode.com/problems/merge-intervals/) | [NeetCode](https://neetcode.io/problems/merge-intervals)
- **Difficulty**: Medium
- **Pattern**: Intervals

---

## Problem Description
Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

### Example 1
```text
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
```

### Example 2
```text
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

### Constraints
- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`

---

## Intuition & Approach
If the intervals are ordered arbitrarily, finding overlapping intervals requires checking pairs across the entire array. However, by sorting the intervals by their start points first, all potentially overlapping intervals are brought adjacent to each other:

1. **Sort by Start Value**:
   - Sort the array in ascending order of interval start times:
     `intervals.sort(key=lambda x: x[0])`

2. **Greedy Iterative Merge**:
   - Initialize the result list with the first interval: `res = [intervals[0]]`.
   - Iterate through each subsequent interval `[start, end]` in `intervals[1:]`:
     - Compare `start` against the end boundary of the most recently merged interval `last_end = res[-1][1]`.
     - **Overlap (`start <= last_end`)**: Merge the current interval into the last one by updating its end point:
       $$\text{res}[-1][1] = \max(\text{last\_end}, \text{end})$$
     - **No Overlap (`start > last_end`)**: Append `[start, end]` as a new disjoint interval to `res`.
3. **Return**: Return `res`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n \log n)$ — Sorting the $n$ intervals dominates the runtime. The subsequent single-pass linear scan takes $\mathcal{O}(n)$ time.
- **Space Complexity**: $\mathcal{O}(n)$ — Space required for Python's Timsort algorithm and storing the output array `res`.

---

## Edge Cases Considered
- **Single interval**: `intervals = [[1, 4]]` returns `[[1, 4]]` without entering the loop.
- **Adjacent intervals touching at a single point**: e.g., `[1, 4]` and `[4, 5]` satisfy `start <= last_end` (`4 <= 4`) and correctly merge into `[1, 5]`.
- **Nested intervals**: When one interval completely encompasses the next (e.g., `[1, 6]` and `[2, 4]`), `max(last_end, end)` keeps the upper bound at 6.
- **No overlapping intervals**: All intervals are appended in order to `res`.
