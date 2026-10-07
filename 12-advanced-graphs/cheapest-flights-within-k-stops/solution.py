"""
Problem: Cheapest Flights Within K Stops
LeetCode: 787 (https://leetcode.com/problems/cheapest-flights-within-k-stops/)
NeetCode 150: Cheapest Flights Within K Stops (https://neetcode.io/problems/cheapest-flights-within-k-stops)
Difficulty: Medium
Pattern: Advanced Graphs (BFS / Bellman-Ford / Dijkstra with Stop Constraint)
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Time Complexity: O(k * E) where E = len(flights) and k is the max number of stops.
        Space Complexity: O(V + E) for the adjacency list, visited cost map, and queue.
        """
        neighbours = defaultdict(list)
        visited = {}
        for item in flights:
            neighbours[item[0]].append([item[1], item[2]])
        my_queue = deque([(src, 0, 0)])
        optimal_cost = float('inf')
        while my_queue:
            curr = my_queue.popleft()
            if curr[0] == dst:
                optimal_cost = min(optimal_cost, curr[1])
                continue
            elif curr[2] > k:
                continue
            if curr[0] in visited and visited[curr[0]] < curr[1]:
                continue
            visited[curr[0]] = curr[1]
            neigh = neighbours[curr[0]]
            for item in neigh:
                my_tuple = (item[0], item[1] + curr[1], curr[2] + 1)
                my_queue.append(my_tuple)
        if optimal_cost == float('inf'):
            return -1
        else:
            return optimal_cost
