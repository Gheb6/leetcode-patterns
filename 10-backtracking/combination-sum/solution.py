"""
Problem: Combination Sum
LeetCode: 39 (https://leetcode.com/problems/combination-sum/)
NeetCode 150: Combination Sum (https://neetcode.io/problems/combination-target-sum)
Difficulty: Medium
Pattern: Backtracking (Unbounded Knapsack / Decision Tree)
"""

from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i, current_sum):
            if current_sum == target:
                res.append(subset.copy())
                return
            elif current_sum > target:
                return
            elif i >= len(nums):
                return 
            
            # include
            subset.append(nums[i])
            current_sum += nums[i]
            dfs(i, current_sum)

            subset.pop()
            current_sum -= nums[i]
            dfs(i + 1, current_sum)
        dfs(0, 0)
        return res


if __name__ == "__main__":
    sol = Solution()

    # Helper function to normalize output for comparison
    def normalize(combinations):
        return sorted([sorted(c) for c in combinations])

    # Test case 1: nums = [2, 3, 6, 7], target = 7 -> [[2, 2, 3], [7]]
    expected_1 = [[2, 2, 3], [7]]
    result_1 = sol.combinationSum([2, 3, 6, 7], 7)
    assert normalize(result_1) == normalize(expected_1), "Failed on [2, 3, 6, 7], target = 7"

    # Test case 2: nums = [2, 3, 5], target = 8 -> [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    expected_2 = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    result_2 = sol.combinationSum([2, 3, 5], 8)
    assert normalize(result_2) == normalize(expected_2), "Failed on [2, 3, 5], target = 8"

    # Test case 3: nums = [2], target = 1 -> []
    assert sol.combinationSum([2], 1) == [], "Failed on [2], target = 1"

    print("All test cases for Combination Sum passed!")
