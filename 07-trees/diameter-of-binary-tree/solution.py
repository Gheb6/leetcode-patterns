"""
Problem: Diameter of Binary Tree
LeetCode: 543 (https://leetcode.com/problems/diameter-of-binary-tree/)
NeetCode 150: Diameter of Binary Tree (https://neetcode.io/problems/binary-tree-diameter)
Difficulty: Easy
Pattern: Trees (DFS / Post-Order Recursion)
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def depth(node):
            if node is None:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right) 
            total_depth = left_depth + right_depth
            nonlocal max_diameter 
            max_diameter = max(max_diameter, total_depth)
            return max(left_depth, right_depth) + 1
        depth(root)
        return max_diameter


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: [1, 2, 3, 4, 5] -> Diameter = 3 (path: [4, 2, 1, 3] or [5, 2, 1, 3])
    t1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert sol.diameterOfBinaryTree(t1) == 3, "Failed on [1, 2, 3, 4, 5]"

    # Test case 2: [1, 2] -> Diameter = 1
    t2 = TreeNode(1, TreeNode(2))
    assert sol.diameterOfBinaryTree(t2) == 1, "Failed on [1, 2]"

    # Test case 3: Single node [1] -> Diameter = 0
    assert sol.diameterOfBinaryTree(TreeNode(1)) == 0, "Failed on single node"

    # Test case 4: Empty tree -> Diameter = 0
    assert sol.diameterOfBinaryTree(None) == 0, "Failed on empty tree"

    print("All test cases for Diameter of Binary Tree passed!")
