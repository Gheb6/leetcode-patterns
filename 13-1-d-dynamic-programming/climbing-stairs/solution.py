"""
Problem: Climbing Stairs
LeetCode: 70 (https://leetcode.com/problems/climbing-stairs/)
NeetCode 150: Climbing Stairs (https://neetcode.io/problems/climbing-stairs)
Difficulty: Easy
Pattern: 1-D Dynamic Programming (Fibonacci / Space Optimized)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev = 1
        curr = 2
        for i in range(3, n + 1):
            new_step = prev + curr
            prev = curr
            curr = new_step
        return curr


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: n = 1 -> 1 way (1)
    assert sol.climbStairs(1) == 1, "Failed on n = 1"

    # Test case 2: n = 2 -> 2 ways (1+1, 2)
    assert sol.climbStairs(2) == 2, "Failed on n = 2"

    # Test case 3: n = 3 -> 3 ways (1+1+1, 1+2, 2+1)
    assert sol.climbStairs(3) == 3, "Failed on n = 3"

    # Test case 4: n = 4 -> 5 ways
    assert sol.climbStairs(4) == 5, "Failed on n = 4"

    # Test case 5: n = 5 -> 8 ways
    assert sol.climbStairs(5) == 8, "Failed on n = 5"

    # Test case 6: Large n = 45
    assert sol.climbStairs(45) == 1836311903, "Failed on n = 45"

    print("All test cases for Climbing Stairs passed!")
