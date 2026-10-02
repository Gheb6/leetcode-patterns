"""
Problem: Two Sum II - Input Array Is Sorted
LeetCode: 167 (https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
NeetCode 150: Two Integer Sum II (https://neetcode.io/problems/two-integer-sum-ii)
Difficulty: Medium
Pattern: Two Pointers (Opposite Ends)
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Finds two numbers such that they add up to target in a 1-indexed sorted array.
        
        Time Complexity: O(N) single pass two-pointer scan.
        Space Complexity: O(1) extra space.
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]  # 1-indexed
            elif curr_sum > target:
                right -= 1
            else:
                left += 1

        return []


if __name__ == "__main__":
    sol = Solution()
    # Test cases
    assert sol.twoSum([2, 7, 11, 15], 9) == [1, 2], "Failed on [2, 7, 11, 15] target 9"
    assert sol.twoSum([2, 3, 4], 6) == [1, 3], "Failed on [2, 3, 4] target 6"
    assert sol.twoSum([-1, 0], -1) == [1, 2], "Failed on [-1, 0] target -1"
    print("All test cases for Two Sum II passed!")
