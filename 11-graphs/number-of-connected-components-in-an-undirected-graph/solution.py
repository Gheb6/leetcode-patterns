"""
Problem: Number of Connected Components in an Undirected Graph
LeetCode: 323 (https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)
NeetCode 150: Count Connected Components (https://neetcode.io/problems/count-connected-components)
Difficulty: Medium
Pattern: Graphs (DFS / Connected Components)
"""

from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Time Complexity: O(V + E) where V = n is vertices and E = len(edges).
        Space Complexity: O(V + E) to store the adjacency list, visited set, and stack.
        """
        visited = set()
        adjacency_list = defaultdict(list)
        connected_component = 0
        for i in range(len(edges)):
            a, b = edges[i]
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)
        for i in range(n):
            if i in visited:
                continue
            else:
                connected_component += 1
                my_stack = [i]
                while my_stack:
                    curr = my_stack.pop()
                    if curr in visited:
                        continue
                    visited.add(curr)
                    for value in adjacency_list[curr]:
                        if value not in visited:
                            my_stack.append(value)
        return connected_component
