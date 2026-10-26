"""
Problem: Maximum Depth of Binary Tree
LeetCode: 104 (https://leetcode.com/problems/maximum-depth-of-binary-tree/)
NeetCode 150: Maximum Depth of Binary Tree (https://neetcode.io/problems/depth-of-binary-tree)
Difficulty: Easy
Pattern: Trees (DFS / Post-Order / Recursion)
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: Tree [3, 9, 20, None, None, 15, 7] -> Depth = 3
    t1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert sol.maxDepth(t1) == 3, "Failed on [3, 9, 20, None, None, 15, 7]"

    # Test case 2: Tree [1, None, 2] -> Depth = 2
    t2 = TreeNode(1, None, TreeNode(2))
    assert sol.maxDepth(t2) == 2, "Failed on [1, None, 2]"

    # Test case 3: Empty tree -> Depth = 0
    assert sol.maxDepth(None) == 0, "Failed on empty tree"

    # Test case 4: Single node tree -> Depth = 1
    assert sol.maxDepth(TreeNode(1)) == 1, "Failed on single node"

    print("All test cases for Maximum Depth of Binary Tree passed!")
