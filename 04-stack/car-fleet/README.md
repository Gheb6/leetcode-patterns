# Car Fleet

- **Source**: LeetCode 853 / NeetCode 150
- **Links**: [LeetCode #853](https://leetcode.com/problems/car-fleet/) | [NeetCode](https://neetcode.io/problems/car-fleet)
- **Difficulty**: Medium
- **Pattern**: Stack (Sorting / Monotonic Stack)

---

## Problem Description
There are `n` cars at given miles away from the starting mile `0`, traveling towards a destination at mile `target`.

You are given two integer arrays `position` and `speed`, both of length `n`, where `position[i]` is the position of the $i^{\text{th}}$ car and `speed[i]` is the speed of the $i^{\text{th}}$ car (in miles per hour).

A car cannot pass another car ahead of it, but it can catch up to it and drive bumper-to-bumper at the same speed. A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also considered a car fleet.

If a car catches up to a car fleet right at the destination point, it is still considered as having joined the fleet.

Return the **number of car fleets** that will arrive at the destination.

### Example 1
```text
Input: target = 12, position = [10, 8, 0, 5, 3], speed = [2, 4, 1, 1, 3]
Output: 3
Explanation:
- The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12 (time = (12-10)/2 = 1.0, (12-8)/4 = 1.0).
- The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself (time = 12.0).
- The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6 (time to target = 7.0 for car at 5, and (12-3)/3 = 3.0 <= 7.0 for car at 3).
Thus, there are 3 fleets.
```

### Example 2
```text
Input: target = 10, position = [3], speed = [3]
Output: 1
Explanation: There is only one car, hence only 1 fleet.
```

### Example 3
```text
Input: target = 100, position = [0, 2, 4], speed = [4, 2, 1]
Output: 1
```

### Constraints
- $n == \text{position.length} == \text{speed.length}$
- $1 \le n \le 10^5$
- $0 < \text{target} \le 10^6$
- $0 \le \text{position}[i] < \text{target}$
- All the values of `position` are **unique**.
- $0 < \text{speed}[i] \le 10^6$

---

## Intuition & Approach
- **Key Observation**:
  - Cars closer to the `target` determine the maximum speed for cars behind them, because cars cannot pass each other.
  - The time it takes for a car at position $p$ with speed $s$ to reach target is:
    $$\text{time} = \frac{\text{target} - p}{s}$$
  - If a car starts **behind** car $A$ ($p_B < p_A$) and its arrival time without obstruction would be $\le \text{time}_A$, it will catch up to car $A$ at or before the destination. Since it cannot pass, it merges into car $A$'s fleet and adopts car $A$'s bottleneck arrival time.
- **Algorithm (Sorting + Stack)**:
  1. Pair each car's position with its speed: `pair = [[p, s] for p, s in zip(position, speed)]`.
  2. Sort the pairs in **descending order of position** (`pair.sort(reverse=True)`), so we process cars from closest to `target` to farthest.
  3. Maintain a stack `my_stack` of fleet arrival times:
     - For each car, calculate its time to target: `time = (target - p) / s`.
     - Push `time` onto `my_stack`.
     - If the stack has at least 2 entries and the top car arrives faster than or at the same time as the fleet ahead of it (`my_stack[-1] <= my_stack[-2]`), this car merges into the preceding fleet. Pop it from the stack (`my_stack.pop()`).
  4. The number of remaining elements in `my_stack` is the number of distinct car fleets.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n \log n)$ — Dominated by sorting $n$ cars by position. The subsequent pass takes linear time $\mathcal{O}(n)$, as each car time is pushed and popped at most once.
- **Space Complexity**: $\mathcal{O}(n)$ — For storing the `pair` list and the monotonic stack of size at most $n$.

---

## Edge Cases Considered
- **Single car ($n = 1$)**: Returns `1` fleet immediately.
- **All cars merge into a single fleet**: Stack shrinks down to `1` element.
- **No cars merge**: All arrival times are strictly increasing from front to back, keeping all $n$ entries in the stack.
- **Cars arrive at the exact same time**: Handled by `<=` condition, correctly merging into the front fleet.
