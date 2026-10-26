"""
Problem: Median of Two Sorted Arrays
LeetCode: 4 (https://leetcode.com/problems/median-of-two-sorted-arrays/)
NeetCode 150: Median of Two Sorted Arrays (https://neetcode.io/problems/median-of-two-sorted-arrays)
Difficulty: Hard
Pattern: Binary Search (Partition / Two Arrays)
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n = len(nums1)
        m = len(nums2)
        left = 0
        right = n
        while left <= right:
            i = (left + right) // 2
            j = (n + m + 1) // 2 - i

            A_left = nums1[i - 1] if i > 0 else float('-inf')
            A_right = nums1[i] if i < n else float('inf')
            B_left = nums2[j - 1] if j > 0 else float('-inf')
            B_right = nums2[j] if j < m else float('inf')

            if A_left <= B_right and B_left <= A_right:
                if (n + m) % 2 == 1:
                    return float(max(A_left, B_left))
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
                    
            elif A_left > B_right:
                right = i - 1
            else:
                left = i + 1


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: Odd total length
    assert sol.findMedianSortedArrays([1, 3], [2]) == 2.0, "Failed on [1, 3] and [2]"

    # Test case 2: Even total length
    assert sol.findMedianSortedArrays([1, 2], [3, 4]) == 2.5, "Failed on [1, 2] and [3, 4]"

    # Test case 3: One empty array
    assert sol.findMedianSortedArrays([], [1]) == 1.0, "Failed on [] and [1]"
    assert sol.findMedianSortedArrays([2], []) == 2.0, "Failed on [2] and []"

    # Test case 4: Disjoint ranges
    assert sol.findMedianSortedArrays([100001], [100000]) == 100000.5, "Failed on [100001] and [100000]"

    # Test case 5: Duplicate elements
    assert sol.findMedianSortedArrays([1, 2], [1, 2, 3]) == 2.0, "Failed on [1, 2] and [1, 2, 3]"

    print("All test cases for Median of Two Sorted Arrays passed!")
