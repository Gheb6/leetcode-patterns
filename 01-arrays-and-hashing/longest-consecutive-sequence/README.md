# Longest Consecutive Sequence

- **Source**: LeetCode 128 / NeetCode 150
- **Links**: [LeetCode #128](https://leetcode.com/problems/longest-consecutive-sequence/) | [NeetCode](https://neetcode.io/problems/longest-consecutive-sequence)
- **Difficulty**: Medium
- **Pattern**: Arrays & Hashing (Hash Set / Sequence Building)

---

## Problem Description
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in $\mathcal{O}(n)$ time.

### Example 1
```text
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

### Example 2
```text
Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
Output: 9
Explanation: The longest consecutive elements sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8]. Therefore its length is 9.
```

### Constraints
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Intuition & Approach
- **Brute Force / Sorting**: Sorting the array in $\mathcal{O}(n \log n)$ time and then finding the longest sequence does not satisfy the required $\mathcal{O}(n)$ time limit.
- **Hash Set (Optimal)**:
  1. Store all elements from `nums` into a hash set `my_set` for $\mathcal{O}(1)$ average lookup time.
  2. Iterate through each number in `my_set`:
     - Check if `(num - 1)` exists in `my_set`. If it does, `num` is **not** the start of a consecutive sequence (it is part of a longer sequence that will be / was started by a smaller number), so skip it.
     - If `(num - 1)` is not in `my_set`, `num` is the **beginning** of a new sequence.
     - Count the length of the streak by repeatedly checking if `num + res` is in `my_set` (`res += 1`).
     - Update the maximum sequence length `best_res = max(best_res, res)`.
  3. Every number is checked as a sequence start in $\mathcal{O}(1)$ and visited inside the `while` loop at most once. Hence, the total time across the entire array is linear $\mathcal{O}(n)$.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Building the set takes $\mathcal{O}(n)$ time. Each number is visited at most twice (once in the outer loop, and at most once in the inner while loop when traversing from its sequence root).
- **Space Complexity**: $\mathcal{O}(n)$ — Storing the unique numbers inside the hash set `my_set`.

---

## Edge Cases Considered
- **Empty list** (`nums = []`): returns `0` immediately.
- **Single element** (`nums = [7]`): returns `1`.
- **Duplicates** (e.g. `[1, 2, 0, 1]`): the hash set automatically deduplicates elements, avoiding redundant loop cycles and correctly returning `3`.
- **Negative numbers**: handled naturally by set hashing.
