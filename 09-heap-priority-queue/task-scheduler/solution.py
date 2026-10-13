"""
Problem: Task Scheduler
LeetCode: 621 (https://leetcode.com/problems/task-scheduler/)
NeetCode 150: Task Scheduler (https://neetcode.io/problems/task-scheduler)
Difficulty: Medium
Pattern: Heap / Priority Queue (Max-Heap + Queue)
"""

from collections import Counter, deque
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        my_deque = deque()  
        count = Counter(tasks)     
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        time = 0
        while max_heap or my_deque :
            time += 1
            if max_heap:
                task = heapq.heappop(max_heap)
                task += 1
                unlock = time + n
                if -task > 0:
                    my_deque.append((task, unlock))
            if my_deque:
                res = my_deque[0]
                if res[1] == time:
                    todo = my_deque.popleft()
                    heapq.heappush(max_heap, todo[0])
        return time
