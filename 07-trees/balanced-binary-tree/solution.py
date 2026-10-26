"""
Problem: Balanced Binary Tree
LeetCode: 110 (https://leetcode.com/problems/balanced-binary-tree/)
NeetCode 150: Balanced Binary Tree (https://neetcode.io/problems/balanced-binary-tree)
Difficulty: Easy
Pattern: Trees (DFS / Bottom-Up Recursion)
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def get_height(node):
            if node is None:
                return 0
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            
            if left_height == -1:
                return -1
            if right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
        
            return max(left_height, right_height) + 1
        if get_height(root) != -1:
            return True
        return False


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: [3, 9, 20, None, None, 15, 7] -> True
    t1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert sol.isBalanced(t1) is True, "Failed on [3, 9, 20, None, None, 15, 7]"

    # Test case 2: [1, 2, 2, 3, 3, None, None, 4, 4] -> False
    #       1
    #      / \
    #     2   2
    #    / \
    #   3   3
    #  / \
    # 4   4
    left_subtree = TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3))
    t2 = TreeNode(1, left_subtree, TreeNode(2))
    assert sol.isBalanced(t2) is False, "Failed on unbalanced tree"

    # Test case 3: Empty tree [] -> True
    assert sol.isBalanced(None) is True, "Failed on empty tree"

    # Test case 4: Single node [1] -> True
    assert sol.isBalanced(TreeNode(1)) is True, "Failed on single node tree"

    print("All test cases for Balanced Binary Tree passed!")
