# Search in Rotated Sorted Array

- **Source**: LeetCode 33 / NeetCode 150
- **Links**: [LeetCode #33](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [NeetCode](https://neetcode.io/problems/find-target-in-rotated-sorted-array)
- **Difficulty**: Medium
- **Pattern**: Binary Search (Rotated Sorted Array)

---

## Problem Description
There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` ($1 \le k < \text{nums.length}$) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0, 1, 2, 4, 5, 6, 7]` might be rotated at pivot index 3 and become `[4, 5, 6, 7, 0, 1, 2]`.

Given the array `nums` after the possible rotation and an integer `target`, return the *index of* `target` *if it is in* `nums`, *or* `-1` *if it is not in* `nums`.

You must write an algorithm with $\mathcal{O}(\log n)$ runtime complexity.

### Example 1
```text
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4
```

### Example 2
```text
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
Output: -1
```

### Example 3
```text
Input: nums = [1], target = 0
Output: -1
```

### Constraints
- $1 \le \text{nums.length} \le 5000$
- $-10^4 \le \text{nums}[i] \le 10^4$
- All values of `nums` are **unique**.
- `nums` is an ascending array that is possibly rotated.
- $-10^4 \le \text{target} \le 10^4$

---

## Intuition & Approach
In a standard binary search, the array is strictly sorted end-to-end. In a rotated sorted array, splitting the array at index `mid` divides it into two halves where **at least one half is guaranteed to be normally sorted**:

1. **Check if `nums[mid] == target`**:
   - If yes, return `mid`.

2. **Determine which half is sorted**:
   - **Case 1: Left half is sorted** (`nums[mid] >= nums[left]`):
     - If the target lies within the sorted left boundaries (`nums[left] <= target < nums[mid]`), narrow the search space to the left half: `right = mid - 1`.
     - Otherwise, the target must reside in the right half: `left = mid + 1`.
   - **Case 2: Right half is sorted** (`nums[mid] < nums[left]`):
     - If the target lies within the sorted right boundaries (`nums[mid] < target <= nums[right]`), narrow the search space to the right half: `left = mid + 1`.
     - Otherwise, the target must reside in the left half: `right = mid - 1`.

3. **Termination**:
   - If `left > right` without finding the target, return `-1`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(\log n)$ — At every step, half of the remaining search space is discarded based on boundary comparisons.
- **Space Complexity**: $\mathcal{O}(1)$ — In-place binary search using constant auxiliary pointers (`left`, `right`, `mid`).

---

## Edge Cases Considered
- **Array of length 1** (`nums = [1]`): Correctly checks if `nums[0] == target`, returns 0 or -1.
- **Unrotated sorted array** (`nums = [1, 2, 3, 4]`): `nums[mid] >= nums[left]` holds true throughout, behaving identically to standard binary search.
- **Target at the rotation pivot / boundaries**: Both strictly inclusive boundary conditions (`nums[left] <= target` and `target <= nums[right]`) ensure edge values are not missed.
