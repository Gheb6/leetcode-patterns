"""
Problem: Course Schedule
LeetCode: 207 (https://leetcode.com/problems/course-schedule/)
NeetCode 150: Course Schedule (https://neetcode.io/problems/course-schedule)
Difficulty: Medium
Pattern: Graphs (Topological Sort / Kahn's Algorithm / Cycle Detection)
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        graph = defaultdict(list)
        my_deque = deque()
        completed = 0
        for elem in prerequisites:
            a = elem[0]
            b = elem[1]
            graph[b].append(a)
            in_degree[a] += 1
        for course, degree in enumerate(in_degree):
            if degree == 0:
                my_deque.append(course)
        while my_deque:
            curr = my_deque.popleft()
            completed += 1
            for neighbour in graph[curr]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    my_deque.append(neighbour)
        return completed == numCourses


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: Linear prerequisite dependency (0 -> 1)
    assert sol.canFinish(2, [[1, 0]]) is True, "Failed on 2 courses: [[1, 0]]"

    # Test case 2: Cycle dependency (0 -> 1 and 1 -> 0)
    assert sol.canFinish(2, [[1, 0], [0, 1]]) is False, "Failed on cycle: [[1, 0], [0, 1]]"

    # Test case 3: No prerequisites
    assert sol.canFinish(1, []) is True, "Failed on single course without prerequisites"

    # Test case 4: Diamond DAG
    assert sol.canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) is True, "Failed on diamond DAG"

    # Test case 5: Disconnected graph with isolated cycle
    assert sol.canFinish(4, [[1, 0], [2, 3], [3, 2]]) is False, "Failed on disconnected graph with cycle"

    print("All test cases for Course Schedule passed!")
