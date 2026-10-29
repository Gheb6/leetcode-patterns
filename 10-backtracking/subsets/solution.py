"""
Problem: Subsets
LeetCode: 78 (https://leetcode.com/problems/subsets/)
NeetCode 150: Subsets (https://neetcode.io/problems/subsets)
Difficulty: Medium
Pattern: Backtracking (Include / Exclude Decision Tree)
"""

from typing import List


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []  

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()

            dfs(i + 1)

        dfs(0)
        return res


if __name__ == "__main__":
    sol = Solution()

    # Helper function to compare list of lists regardless of order
    def normalize(subsets):
        return sorted([sorted(s) for s in subsets])

    # Test case 1: nums = [1, 2, 3] -> 8 subsets
    expected_1 = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    result_1 = sol.subsets([1, 2, 3])
    assert len(result_1) == 8, "Failed length check on [1, 2, 3]"
    assert normalize(result_1) == normalize(expected_1), "Failed on [1, 2, 3]"

    # Test case 2: nums = [0] -> [[], [0]]
    expected_2 = [[], [0]]
    result_2 = sol.subsets([0])
    assert normalize(result_2) == normalize(expected_2), "Failed on [0]"

    # Test case 3: empty list -> [[]]
    assert sol.subsets([]) == [[]], "Failed on empty list"

    print("All test cases for Subsets passed!")
