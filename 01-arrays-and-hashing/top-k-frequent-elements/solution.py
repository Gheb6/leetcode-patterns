"""
Problem: Top K Frequent Elements
LeetCode: 347 (https://leetcode.com/problems/top-k-frequent-elements/)
NeetCode 150: Top K Elements in List (https://neetcode.io/problems/top-k-elements-in-list)
Difficulty: Medium
Pattern: Arrays & Hashing (Hash Map & Frequency Sort)
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time Complexity: O(n + m log m) where n is len(nums) and m is the number of unique elements.
        Space Complexity: O(m) to store frequencies in the dictionary and list.
        """
        my_dict = {}
        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1
        sorted_items = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
        ordered_keys = [item[0] for item in sorted_items]   
        # my_list = []
        # for i in range(k):
        #     my_list.append(ordered_keys[i])
        # return my_list 

        # Slicing
        return ordered_keys[:k]
