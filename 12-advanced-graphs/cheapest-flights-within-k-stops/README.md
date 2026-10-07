# Cheapest Flights Within K Stops

- **Source**: LeetCode 787 / NeetCode 150
- **Links**: [LeetCode #787](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | [NeetCode](https://neetcode.io/problems/cheapest-flights-within-k-stops)
- **Difficulty**: Medium
- **Pattern**: Advanced Graphs (BFS with Level & Cost Pruning)

---

## Problem Description
There are `n` cities connected by some number of flights. You are given an array `flights` where `flights[i] = [from_i, to_i, price_i]` indicates that there is a flight from city `from_i` to city `to_i` with cost `price_i`.

You are also given three integers `src`, `dst`, and `k`, return the **cheapest price** from `src` to `dst` with at most `k` stops. If there is no such route, return `-1`.

---

## Intuition & Approach
- Build an adjacency list `neighbours[u] = [(v, price), ...]`.
- Use a **BFS queue** storing tuples `(city, total_cost, stops)` starting from `(src, 0, 0)`.
- Apply pruning:
  1. If `stops > k` when departing, skip that state.
  2. If the destination `dst` is reached, record the candidate minimum cost.
  3. Maintain a `visited` map storing the minimum cost to reach each city; prune if the current path cost is greater than or equal to an already discovered cheaper cost to that city.
- Return the optimal cost if finite, else `-1`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(k \cdot E)$ — Where $E = \text{len}(flights)$ and $k$ is the stop limit. Each edge is relaxed across at most $k + 1$ levels.
- **Space Complexity**: $\mathcal{O}(V + E)$ — To store the graph adjacency list, `visited` map, and BFS queue.
