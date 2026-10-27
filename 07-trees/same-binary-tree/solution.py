"""
Problem: Same Binary Tree (Same Tree)
LeetCode: 100 (https://leetcode.com/problems/same-tree/)
NeetCode 150: Same Binary Tree (https://neetcode.io/problems/same-binary-tree)
Difficulty: Easy
Pattern: Trees (DFS / Tree Traversal)
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: Identical trees [1, 2, 3] and [1, 2, 3] -> True
    p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    q1 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert sol.isSameTree(p1, q1) is True, "Failed on identical trees [1, 2, 3]"

    # Test case 2: Structurally different [1, 2] vs [1, None, 2] -> False
    p2 = TreeNode(1, TreeNode(2), None)
    q2 = TreeNode(1, None, TreeNode(2))
    assert sol.isSameTree(p2, q2) is False, "Failed on structurally different trees"

    # Test case 3: Same structure, different values [1, 2, 1] vs [1, 1, 2] -> False
    p3 = TreeNode(1, TreeNode(2), TreeNode(1))
    q3 = TreeNode(1, TreeNode(1), TreeNode(2))
    assert sol.isSameTree(p3, q3) is False, "Failed on trees with different node values"

    # Test case 4: Both empty -> True
    assert sol.isSameTree(None, None) is True, "Failed on both None"

    # Test case 5: One empty, one non-empty -> False
    assert sol.isSameTree(TreeNode(1), None) is False, "Failed on one empty tree"

    print("All test cases for Same Binary Tree passed!")
