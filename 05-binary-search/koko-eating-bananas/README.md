# Koko Eating Bananas

- **Source**: LeetCode 875 / NeetCode 150
- **Links**: [LeetCode #875](https://leetcode.com/problems/koko-eating-bananas/) | [NeetCode](https://neetcode.io/problems/eating-bananas)
- **Difficulty**: Medium
- **Pattern**: Binary Search on Solution Space (Monotonic Feasibility Function)

---

## Problem Description
Koko loves to eat bananas. There are `n` piles of bananas, the $i$-th pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Return the **minimum integer** `k` such that she can eat all the bananas within `h` hours.

---

## Intuition & Approach
Instead of binary searching over an existing array, we **binary search over the possible range of answers**:
1. **Answer Range**:
   - Minimum possible speed: $k = 1$ (cannot eat 0 bananas/hr).
   - Maximum necessary speed: $k = \max(\text{piles})$ (at this speed she eats any pile in at most 1 hour).
2. **Monotonicity**:
   - If speed $k$ allows finishing within $h$ hours, any higher speed $k' > k$ will also allow finishing.
   - If speed $k$ fails to finish in time, any lower speed will definitely fail.
3. **Binary Search**:
   - Compute `mid = (left + right) // 2`.
   - Calculate total hours required at speed `mid`: $\sum \lceil \frac{\text{pile}}{\text{mid}} \rceil$.
   - If total hours $\le h$: speed `mid` is feasible. Record `mid` and try searching lower speeds (`right = mid - 1`).
   - Else: speed `mid` is too slow, must increase speed (`left = mid + 1`).

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n \log m)$ where $n = \text{len(piles)}$ and $m = \max(\text{piles})$.
  - Range size is $m$, so binary search takes $\mathcal{O}(\log m)$ iterations.
  - In each iteration, we iterate over all $n$ piles taking $\mathcal{O}(n)$ time.
- **Space Complexity**: $\mathcal{O}(1)$ — Only a few scalar variables.

---

## Edge Cases Considered
- `h == len(piles)`: speed must equal $\max(\text{piles})$ because Koko cannot eat from multiple piles in the same hour.
- Very large pile sizes: Python handles arbitrarily large numbers, but watch out for time limit if iterating linearly instead of binary search.
