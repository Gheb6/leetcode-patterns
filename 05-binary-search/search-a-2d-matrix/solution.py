"""
Problem: Search a 2D Matrix
LeetCode: 74 (https://leetcode.com/problems/search-a-2d-matrix/)
NeetCode 150: Search a 2D Matrix (https://neetcode.io/problems/search-2d-matrix)
Difficulty: Medium
Pattern: Binary Search
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        cols = len(matrix[0])
        row = len(matrix) 
        left = 0
        right = cols * row - 1
        while left <= right:
            mid = ( left + right ) // 2
            element_row = mid // cols
            element_col = mid % cols
            if matrix[element_row][element_col] == target:
                return True
            elif matrix[element_row][element_col] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
