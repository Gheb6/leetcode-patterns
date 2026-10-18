# Daily Temperatures

- **Source**: LeetCode 739 / NeetCode 150
- **Links**: [LeetCode #739](https://leetcode.com/problems/daily-temperatures/) | [NeetCode](https://neetcode.io/problems/daily-temperatures)
- **Difficulty**: Medium
- **Pattern**: Stack (Monotonic Decreasing Stack)

---

## Problem Description
Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the $i^{\text{th}}$ day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

### Example 1
```text
Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
```

### Example 2
```text
Input: temperatures = [30, 40, 50, 60]
Output: [1, 1, 1, 0]
```

### Example 3
```text
Input: temperatures = [30, 60, 90]
Output: [1, 1, 0]
```

### Constraints
- $1 \le \text{temperatures.length} \le 10^5$
- $30 \le \text{temperatures}[i] \le 100$

---

## Intuition & Approach
- **Brute Force**: For each day $i$, scan all forward days $j > i$ until finding a higher temperature. This takes $\mathcal{O}(n^2)$ time and will result in Time Limit Exceeded (TLE) for $n = 10^5$.
- **Monotonic Decreasing Stack (Optimal)**:
  1. Initialize `res` as a list of zeros with the same length as `temperatures`.
  2. Maintain a stack of pairs `(index, temperature)` that is kept in **strictly decreasing** (or non-increasing) order of temperature.
  3. Iterate through `temperatures` with `(index, temperature)`:
     - While the stack is non-empty and the current day's temperature is strictly greater than the temperature at the top of the stack (`temperature > my_stack[-1][1]`):
       - We have found the *next warmer day* for that earlier index!
       - Pop `(prev_idx, prev_temp)` from the stack.
       - Calculate the days waited: `res[prev_idx] = index - prev_idx`.
     - Push the current day `(index, temperature)` onto the stack.
  4. Any days remaining in the stack at the end have no warmer future day, so their entries naturally stay `0`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Each day's index/temperature is pushed onto the stack exactly once and popped at most once across the entire iteration, resulting in linear time overall.
- **Space Complexity**: $\mathcal{O}(n)$ — In the worst case (strictly decreasing temperatures), the stack holds up to $n$ elements.

---

## Edge Cases Considered
- **Strictly decreasing temperatures** (e.g. `[90, 80, 70]`): Elements are pushed to the stack and never popped; result is all `0`s.
- **Strictly increasing temperatures** (e.g. `[30, 40, 50, 60]`): Each new element immediately pops the previous one; result is `[1, 1, 1, 0]`.
- **Single element array** (e.g. `[50]`): Loop runs once, element remains in stack, returns `[0]`.
- **Duplicate temperatures**: Strict inequality `>` ensures duplicate temperatures are pushed rather than incorrectly resolving each other.
