# Two Sum II - Input Array Is Sorted

- **Source**: LeetCode 167 / NeetCode 150
- **Links**: [LeetCode #167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [NeetCode](https://neetcode.io/problems/two-integer-sum-ii)
- **Difficulty**: Medium
- **Pattern**: Two Pointers

---

## Problem Description
Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific `target` number. Return the indices of the two numbers added by one (`[index1, index2]`).

### Constraints
- $2 \le \text{numbers.length} \le 3 \cdot 10^4$
- Exactly one valid solution exists.
- Constant extra space $\mathcal{O}(1)$ is required.

---

## Intuition & Approach
Because the array is already **sorted**, we can leverage the two-pointer technique starting at opposite ends:
- Initialize `left = 0` and `right = len(numbers) - 1`.
- If `numbers[left] + numbers[right] == target`: we found the solution!
- If the sum is **too large** (`> target`): since the array is sorted, any other pair with `right` will also be too large. We must decrement `right`.
- If the sum is **too small** (`< target`): any other pair with `left` will also be too small. We must increment `left`.

This avoids the $\mathcal{O}(n)$ hash map space needed in classic Two Sum, achieving true $\mathcal{O}(1)$ space complexity.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — In each step, the search space shrinks by one pointer move. At most $n$ iterations.
- **Space Complexity**: $\mathcal{O}(1)$ — Only two pointer variables are used.

---

## Edge Cases Considered
- Negative numbers: Works properly because sorting preserves order regardless of sign.
- Two identical elements adding up to target (e.g. `[2, 5, 5, 11]`, target = 10).
