"""
Problem: Invert Binary Tree
LeetCode: 226 (https://leetcode.com/problems/invert-binary-tree/)
NeetCode 150: Invert Binary Tree (https://neetcode.io/problems/invert-a-binary-tree)
Difficulty: Easy
Pattern: Trees (DFS / Recursion)
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        else:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
