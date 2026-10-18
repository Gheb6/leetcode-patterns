"""
Problem: 3Sum
LeetCode: 15 (https://leetcode.com/problems/3sum/)
NeetCode 150: 3Sum (https://neetcode.io/problems/three-integer-sum)
Difficulty: Medium
Pattern: Two Pointers (Sorting / Two Pointers / Duplicate Skipping)
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            a = nums[i]
            if a > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            b = i + 1
            c = len(nums) - 1
            while b < c:
                if nums[b] + nums[c] == -a:
                    res.append([ a, nums[b], nums[c] ])
                    b += 1
                    while nums[b] == nums[b - 1] and b < c:
                        b += 1   
                elif ( a + nums[b] + nums[c] ) > 0:
                    c -= 1
                else:
                    b += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    # Test cases
    assert sol.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]], "Failed on [-1, 0, 1, 2, -1, -4]"
    assert sol.threeSum([0, 1, 1]) == [], "Failed on [0, 1, 1]"
    assert sol.threeSum([0, 0, 0]) == [[0, 0, 0]], "Failed on [0, 0, 0]"
    assert sol.threeSum([]) == [], "Failed on empty array"
    print("All test cases for 3Sum passed!")
