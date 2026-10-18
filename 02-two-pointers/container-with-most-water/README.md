# Container With Most Water

- **Source**: LeetCode 11 / NeetCode 150
- **Links**: [LeetCode #11](https://leetcode.com/problems/container-with-most-water/) | [NeetCode](https://neetcode.io/problems/max-water-container)
- **Difficulty**: Medium
- **Pattern**: Two Pointers (Greedy / Opposite Ends)

---

## Problem Description
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the $i^{\text{th}}$ line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

### Example 1
```text
Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49
Explanation: The vertical lines are represented by array [1, 8, 6, 2, 5, 4, 8, 3, 7]. In this case, the max area of water the container can contain is 49 (between index 1 with height 8 and index 8 with height 7: width = 7, min_height = 7, area = 49).
```

### Example 2
```text
Input: height = [1, 1]
Output: 1
```

### Constraints
- $n == \text{height.length}$
- $2 \le n \le 10^5$
- $0 \le \text{height}[i] \le 10^4$

---

## Intuition & Approach
- **Brute Force**: Evaluate all pairs $(i, j)$ and compute their area: $\text{area} = (j - i) \times \min(\text{height}[i], \text{height}[j])$. This takes $\mathcal{O}(n^2)$ time and exceeds time limits for $n = 10^5$.
- **Two Pointers (Optimal / Greedy)**:
  1. Place two pointers at opposite ends: `left = 0` and `right = len(height) - 1`. This starts with the maximum possible container width.
  2. Compute the current area:
     $$\text{area} = (\text{right} - \text{left}) \times \min(\text{height}[\text{left}], \text{height}[\text{right}])$$
     and update `best_area`.
  3. **Greedy Pointer Movement**:
     - The water capacity is bottlenecked by the shorter of the two lines.
     - Moving the taller line inward would only decrease the width without any chance of increasing the bounded height (since the minimum remains limited by the shorter line or gets even smaller).
     - Therefore, we must move the pointer corresponding to the **shorter line** inward (`left += 1` if `height[left] < height[right]`, otherwise `right -= 1`), in hopes of finding a taller boundary that compensates for the reduced width.
  4. Continue until the two pointers meet.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Single pass where the pointers move towards each other; at each step, either `left` increments or `right` decrements, taking at most $n$ iterations.
- **Space Complexity**: $\mathcal{O}(1)$ — Only a constant number of integer variables are used.

---

## Edge Cases Considered
- **Minimum length ($n = 2$)**: Array with two heights computes the single valid container directly.
- **All lines with equal height** (e.g. `[4, 4, 4, 4]`): Pointers correctly narrow down and evaluate the maximal width initially.
- **Heights with zero values**: Area is $0$ when bounded by a line of height $0$, handled correctly by `min()`.
- **Plateaus or decreasing staircases**: The greedy choice guarantees no optimal configuration is skipped.
