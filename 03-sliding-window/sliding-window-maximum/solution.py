"""
Problem: Sliding Window Maximum
LeetCode: 239 (https://leetcode.com/problems/sliding-window-maximum/)
NeetCode 150: Sliding Window Maximum (https://neetcode.io/problems/sliding-window-maximum)
Difficulty: Hard
Pattern: Sliding Window (Monotonic Deque)
"""

from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Time Complexity: O(n) since each element index is added and removed at most once from the deque.
        Space Complexity: O(k) for the monotonic deque storing indices within the current window.
        """
        my_deque = deque()
        res = []
        for i, num in enumerate(nums):
            if my_deque and my_deque[0] <= i - k:
                my_deque.popleft()
            while my_deque and nums[my_deque[-1]] < num:
                my_deque.pop()
            my_deque.append(i)
            if i >= k - 1:
                res.append(nums[my_deque[0]])
        return res
