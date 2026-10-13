# Time Based Key-Value Store

- **Source**: LeetCode 981 / NeetCode 150
- **Links**: [LeetCode #981](https://leetcode.com/problems/time-based-key-value-store/) | [NeetCode](https://neetcode.io/problems/time-based-key-value-store)
- **Difficulty**: Medium
- **Pattern**: Binary Search

---

## Problem Description
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the `TimeMap` class:
- `TimeMap()`: initializes the object.
- `void set(String key, String value, int timestamp)`: stores the `key` with the `value` at the given `timestamp`.
- `String get(String key, int timestamp)`: returns the value with the largest `timestamp_prev <= timestamp`. If no such timestamp exists, returns `""`.

---

## Strategy & Approach
1. **Data Structure**: Use a hash map mapping each `key` to a list of pairs: `[timestamp, value]`.
2. **Naturally Sorted Timestamps**: The problem guarantees that `timestamp` values for `set` are strictly increasing. Therefore, the list for any given key is already sorted by timestamp.
3. **Binary Search (`get`)**:
   - Perform binary search on the list associated with `key`.
   - If `values[mid][0] <= timestamp`: record `values[mid][1]` as candidate `best_res` and search the right half (`left = mid + 1`) to find a later valid timestamp.
   - Otherwise: search the left half (`right = mid - 1`).

---

## Complexity Analysis
- **Time Complexity**:
  - `set`: $\mathcal{O}(1)$ — appending to a list is amortized constant time.
  - `get`: $\mathcal{O}(\log n)$ — binary search over $n$ timestamps associated with the given key.
- **Space Complexity**: $\mathcal{O}(N)$ — where $N$ is the total number of key-value pairs stored across all `set` calls.
