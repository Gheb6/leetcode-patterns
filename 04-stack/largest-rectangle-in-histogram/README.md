# Largest Rectangle in Histogram

- **Source**: LeetCode 84 / NeetCode 150
- **Links**: [LeetCode #84](https://leetcode.com/problems/largest-rectangle-in-histogram/) | [NeetCode](https://neetcode.io/problems/largest-rectangle-in-histogram)
- **Difficulty**: Hard
- **Pattern**: Stack (Monotonic Increasing Stack)

---

## Problem Description
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return the area of the largest rectangle in the histogram.

### Example 1
```text
Input: heights = [2, 1, 5, 6, 2, 3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units (height 5, width 2: between indices 2 and 3).
```

### Example 2
```text
Input: heights = [2, 4]
Output: 4
```

### Constraints
- $1 \le \text{heights.length} \le 10^5$
- $0 \le \text{heights}[i] \le 10^4$

---

## Intuition & Approach
- **Brute Force**: For each bar $i$, find the farthest bars to the left and right that are at least as tall as $\text{heights}[i]$. That takes $\mathcal{O}(n^2)$ time, which results in Time Limit Exceeded (TLE) for $n = 10^5$.
- **Monotonic Increasing Stack (Optimal)**:
  1. Maintain a stack of pairs `(start_index, height)` kept in **strictly increasing** order of heights.
  2. For each bar `(i, h)` in `heights`:
     - Initialize `start = i`.
     - While the stack is non-empty and the height of the top element is strictly greater than current height $h$ (`my_stack[-1][1] > h`):
       - The taller bar cannot extend to the right beyond index $i$.
       - Pop `(pop_i, pop_h)` from the stack.
       - Calculate the area of the rectangle formed by this popped height:
         $$\text{area} = \text{pop\_h} \times (i - \text{pop\_i})$$
       - Update `max_area = max(max_area, area)`.
       - Because the current bar of height $h$ is shorter than `pop_h`, the rectangle of height $h$ can extend **backward** all the way to `pop_i`. Hence, set `start = pop_i`.
     - Push `(start, h)` onto the stack.
  3. After iterating through all bars, process any remaining bars in the stack:
     - These bars could extend all the way to the end of the histogram (`len(heights)`).
     - For each `(start_i, h)` in `my_stack`:
       $$\text{area} = h \times (\text{len(heights)} - \text{start\_i})$$
       Update `max_area`.
  4. Return `max_area`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Each bar is pushed onto the stack once and popped at most once, leading to a linear scan overall.
- **Space Complexity**: $\mathcal{O}(n)$ — In the worst case (strictly increasing heights), the stack stores all $n$ bars.

---

## Edge Cases Considered
- **All bars of height zero** (`[0]` or `[0, 0]`): Correctly returns `0`.
- **Strictly increasing heights** (e.g. `[1, 2, 3, 4]`): Bars are all pushed, then resolved in the final loop.
- **Strictly decreasing heights** (e.g. `[4, 3, 2, 1]`): Each subsequent bar pops the previous bar and extends its start index backward.
- **All bars equal height** (e.g. `[5, 5, 5]`): Evaluates max area $5 \times 3 = 15$.
- **Single bar** (e.g. `[7]`): Handled naturally, returning `7`.
