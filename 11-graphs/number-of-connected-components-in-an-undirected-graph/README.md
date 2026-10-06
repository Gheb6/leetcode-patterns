# Number of Connected Components in an Undirected Graph

- **Source**: LeetCode 323 / NeetCode 150
- **Links**: [LeetCode #323](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | [NeetCode](https://neetcode.io/problems/count-connected-components)
- **Difficulty**: Medium
- **Pattern**: Graphs (DFS / Connected Components)

---

## Problem Description
You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer `n` and an array `edges` where `edges[i] = [a_i, b_i]` indicates an undirected edge between `a_i` and `b_i`.

Return the total number of connected components in the graph.

---

## Intuition & Approach
- Build an undirected graph adjacency list using a hash map / `defaultdict`.
- Maintain a `visited` set to track explored nodes.
- Iterate through each node from `0` to `n - 1`:
  - If node `i` is not visited, it marks the start of a new connected component (increment counter).
  - Perform an iterative **DFS** (using an explicit stack) to traverse and mark all nodes reachable from `i` as visited.
- Return the total number of connected components discovered.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(V + E)$ — Where $V = n$ and $E = \text{len}(edges)$. Each node and edge is processed at most a constant number of times.
- **Space Complexity**: $\mathcal{O}(V + E)$ — To store the adjacency list, the `visited` set, and the DFS stack.
