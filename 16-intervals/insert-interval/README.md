# Insert Interval

- **Source**: LeetCode 57 / NeetCode 150
- **Links**: [LeetCode #57](https://leetcode.com/problems/insert-interval/) | [NeetCode](https://neetcode.io/problems/insert-new-interval)
- **Difficulty**: Medium
- **Pattern**: Intervals

---

## Problem Description
You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start_i, end_i]` represent the start and the end of the $i$-th interval and `intervals` is sorted in ascending order by `start_i`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start_i` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` after the insertion.

> **Note**: You don't need to modify `intervals` in-place. You can make a new array and return it.

### Example 1
```text
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

### Example 2
```text
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

### Constraints
- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^5`
- `intervals` is sorted by `start_i` in ascending order.
- `newInterval.length == 2`
- `0 <= start <= end <= 10^5`

---

## Intuition & Approach
Since the input `intervals` is already sorted by start time, we can solve this problem in a single linear pass ($\mathcal{O}(n)$) divided into three distinct phases:

1. **Add non-overlapping intervals before `newInterval`**:
   - While `i < n` and `intervals[i][1] < newInterval[0]`:
     - The current interval ends strictly before `newInterval` begins, so there is no overlap.
     - Append `intervals[i]` to `res` and increment `i`.

2. **Merge all overlapping intervals with `newInterval`**:
   - While `i < n` and `intervals[i][0] <= newInterval[1]`:
     - The current interval starts before or at the end of `newInterval`, which implies an overlap.
     - Expand `newInterval` to cover both:
       $$\text{newInterval}[0] = \min(\text{newInterval}[0], \text{intervals}[i][0])$$
       $$\text{newInterval}[1] = \max(\text{newInterval}[1], \text{intervals}[i][1])$$
     - Increment `i`.
   - After merging all overlapping intervals, append the updated `newInterval` to `res`.

3. **Add remaining non-overlapping intervals after `newInterval`**:
   - While `i < n`:
     - All subsequent intervals start strictly after `newInterval` has ended.
     - Append each directly to `res` and increment `i`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — We iterate through `intervals` with index pointer `i`, visiting each interval at most once.
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space (excluding the output list `res` of size $\mathcal{O}(n)$).

---

## Edge Cases Considered
- **Empty input (`intervals = []`)**: Phase 1 and 3 loops do not execute; `newInterval` is appended and returned (`[newInterval]`).
- **No overlap (inserted at front or back)**: `newInterval` is appended at the correct relative position without merging.
- **Total overlap**: `newInterval` overlaps with and absorbs every interval in `intervals`.
