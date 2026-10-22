# Find Minimum in Rotated Sorted Array

- **Source**: LeetCode 153 / NeetCode 150
- **Links**: [LeetCode #153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [NeetCode](https://neetcode.io/problems/find-minimum-in-rotated-sorted-array)
- **Difficulty**: Medium
- **Pattern**: Binary Search (Rotated Sorted Array / Inflection Point)

---

## Problem Description
Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0, 1, 2, 4, 5, 6, 7]` might become:
- `[4, 5, 6, 7, 0, 1, 2]` if it was rotated 4 times.
- `[0, 1, 2, 4, 5, 6, 7]` if it was rotated 7 times.

Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return the *minimum element* of this array.

You must write an algorithm that runs in $\mathcal{O}(\log n)$ time.

### Example 1
```text
Input: nums = [3, 4, 5, 1, 2]
Output: 1
Explanation: The original array was [1, 2, 3, 4, 5] rotated 3 times.
```

### Example 2
```text
Input: nums = [4, 5, 6, 7, 0, 1, 2]
Output: 0
Explanation: The original array was [0, 1, 2, 4, 5, 6, 7] rotated 4 times.
```

### Example 3
```text
Input: nums = [11, 13, 15, 17]
Output: 11
Explanation: The original array was [11, 13, 15, 17] and it was rotated 4 times.
```

### Constraints
- $n == \text{nums.length}$
- $1 \le n \le 5000$
- $-5000 \le \text{nums}[i] \le 5000$
- All the integers of `nums` are **unique**.
- `nums` is sorted and rotated between `1` and `n` times.

---

## Intuition & Approach
In a standard sorted array, `nums[left] < nums[right]`. When an array is rotated, it is partitioned into two sorted subarrays where all elements in the left subarray are strictly greater than elements in the right subarray (e.g., `[4, 5, 6, 7]` and `[0, 1, 2]`). The minimum element is the **inflection point** (the start of the second subarray).

### Binary Search Strategy:
Instead of comparing `nums[mid]` against a target value, compare `nums[mid]` with the rightmost boundary `nums[right]`:
1. **If `nums[mid] > nums[right]`**:
   - The middle element belongs to the left (larger) sorted portion.
   - The minimum element must strictly lie to the **right** of `mid`.
   - Update `left = mid + 1`.
2. **If `nums[mid] <= nums[right]`**:
   - The middle element belongs to the right (smaller) sorted portion, or the entire subarray `[left, right]` is sorted.
   - The minimum element could be `mid` itself or to its **left**.
   - Update `right = mid`.

The loop terminates when `left == right`, converging precisely onto the index of the minimum element.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(\log n)$ — At each iteration, the search interval $[left, right]$ is halved.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant auxiliary space using only three index pointers (`left`, `right`, `mid`).

---

## Edge Cases Considered
- **Array not rotated / rotated $n$ times** (e.g. `[11, 13, 15, 17]`): `nums[mid] < nums[right]` holds throughout, correctly converging to index 0.
- **Single element** (`nums = [1]`): While loop never executes since `left < right` is false, returns `nums[0] = 1`.
- **Two elements** (e.g. `[2, 1]`): Correctly compares $2 > 1$, advances `left = 1`, and returns `1`.
