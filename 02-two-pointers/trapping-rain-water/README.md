# Trapping Rain Water

- **Source**: LeetCode 42 / NeetCode 150
- **Links**: [LeetCode #42](https://leetcode.com/problems/trapping-rain-water/) | [NeetCode](https://neetcode.io/problems/trapping-rain-water)
- **Difficulty**: Hard
- **Pattern**: Two Pointers (Opposite Ends / Boundary Maxima)

---

## Problem Description
Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

### Example 1
```text
Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
Explanation: The elevation map above is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water are being trapped.
```

### Example 2
```text
Input: height = [4, 2, 0, 3, 2, 5]
Output: 9
```

### Constraints
- $n == \text{height.length}$
- $1 \le n \le 2 \cdot 10^4$
- $0 \le \text{height}[i] \le 10^5$

---

## Intuition & Approach

The water trapped at any bar $i$ is determined by the minimum of the highest bar to its left and the highest bar to its right, minus its own height:
$$\text{trapped}[i] = \max(0, \min(\text{max\_left}[i], \text{max\_right}[i]) - \text{height}[i])$$

### Progression of Solutions:
1. **Brute Force**: For each element, scan left and right to find maximums. $\mathcal{O}(n^2)$ time, $\mathcal{O}(1)$ space (Time Limit Exceeded).
2. **Prefix and Suffix Max Arrays (Dynamic Programming)**: Precompute `left_max` and `right_max` arrays in two passes. $\mathcal{O}(n)$ time, but requires $\mathcal{O}(n)$ extra space.
3. **Two Pointers (Optimal)**:
   - Instead of storing all prefix and suffix maxima, maintain running variables `left_max` and `right_max` with two pointers `left = 0` and `right = len(height) - 1`.
   - At each step, compare `left_max` and `right_max`:
     - If `left_max < right_max`: the bottleneck for the bar at `left + 1` is definitively `left_max` (since we know there is a bar on the right at least as tall as `right_max > left_max`). Advance `left += 1`, update `left_max`, and add `left_max - height[left]` to total water.
     - Otherwise (`left_max >= right_max`): the bottleneck for the bar at `right - 1` is definitively `right_max`. Decrement `right -= 1`, update `right_max`, and add `right_max - height[right]` to total water.
   - Continue until the two pointers meet.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Single pass over the array of length $n$. Each pointer moves inward by one step per iteration.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant auxiliary space using only four pointers/variables (`left`, `right`, `left_max`, `right_max`).

---

## Edge Cases Considered
- **Fewer than 3 bars** (e.g. `[1]` or `[1, 2]`): Water cannot be trapped without boundaries on both sides; correctly returns `0`.
- **Flat surface / All heights identical** (e.g. `[3, 3, 3]`): No cavities exist; returns `0`.
- **Strictly ascending or descending elevations**: Water drains off edges; returns `0`.
- **Multiple local peaks / V-valleys**: Traps water at different elevations simultaneously.
