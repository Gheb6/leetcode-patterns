"""
Problem: Combination Sum II
LeetCode: 40 (https://leetcode.com/problems/combination-sum-ii/)
NeetCode 150: Combination Sum II (https://neetcode.io/problems/combination-target-sum-ii)
Difficulty: Medium
Pattern: Backtracking (Pruning & Duplicate Handling)
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()
        def dfs(start, current_sum):
            if current_sum == target:
                res.append(subset.copy())
                return
            for i in range(start, len(candidates)):
                if current_sum + candidates[i] > target:
                    break
                elif i > start and candidates[i] == candidates[i - 1]:
                    continue
                subset.append(candidates[i])
                dfs(i + 1, current_sum + candidates[i])
                subset.pop()
        dfs(0,0)
        return res


if __name__ == "__main__":
    sol = Solution()

    def normalize(combinations):
        return sorted([sorted(c) for c in combinations])

    # Test case 1: candidates = [10, 1, 2, 7, 6, 1, 5], target = 8
    expected_1 = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    res_1 = sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    assert normalize(res_1) == normalize(expected_1), f"Failed on test 1: got {res_1}"

    # Test case 2: candidates = [2, 5, 2, 1, 2], target = 5
    expected_2 = [[1, 2, 2], [5]]
    res_2 = sol.combinationSum2([2, 5, 2, 1, 2], 5)
    assert normalize(res_2) == normalize(expected_2), f"Failed on test 2: got {res_2}"

    # Test case 3: target impossible
    assert sol.combinationSum2([3, 5], 2) == [], "Failed on impossible target"

    print("All test cases for Combination Sum II passed!")

