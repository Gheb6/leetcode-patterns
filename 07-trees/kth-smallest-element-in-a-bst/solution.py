"""
Problem: Kth Smallest Element in a BST
LeetCode: 230 (https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
NeetCode 150: Kth Smallest Integer in BST (https://neetcode.io/problems/kth-smallest-integer-in-bst)
Difficulty: Medium
Pattern: Trees (BST Properties / In-Order Traversal / Iterative Stack)
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        my_stack = []
        curr = root
        while curr or my_stack:
            while curr:
                my_stack.append(curr)
                curr = curr.left
            curr = my_stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: root = [3, 1, 4, None, 2], k = 1 -> 1
    #       3
    #      / \
    #     1   4
    #      \
    #       2
    t1 = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    assert sol.kthSmallest(t1, 1) == 1, "Failed on example 1 with k = 1"

    # Test case 2: root = [5, 3, 6, 2, 4, None, None, 1], k = 3 -> 3
    #         5
    #        / \
    #       3   6
    #      / \
    #     2   4
    #    /
    #   1
    t2 = TreeNode(
        5,
        TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)),
        TreeNode(6),
    )
    assert sol.kthSmallest(t2, 3) == 3, "Failed on example 2 with k = 3"

    # Test case 3: Single node root = [1], k = 1 -> 1
    t3 = TreeNode(1)
    assert sol.kthSmallest(t3, 1) == 1, "Failed on single node tree"

    print("All test cases for Kth Smallest Element in a BST passed!")

