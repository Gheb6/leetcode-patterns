"""
Problem: Subtree of Another Tree
LeetCode: 572 (https://leetcode.com/problems/subtree-of-another-tree/)
NeetCode 150: Subtree of Another Tree (https://neetcode.io/problems/subtree-of-a-binary-tree)
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(tree_1, tree_2):
            if not tree_1 and not tree_2:
                return True
            elif tree_1 and not tree_2:
                return False
            elif not tree_1 and tree_2:
                return False
            elif tree_1.val != tree_2.val:
                return False
            return isSameTree(tree_1.left, tree_2.left) and isSameTree(tree_1.right, tree_2.right)

        if not subRoot:
            return True
        elif not root:
            return False
        elif isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: root = [3, 4, 5, 1, 2], subRoot = [4, 1, 2] -> True
    r1 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    s1 = TreeNode(4, TreeNode(1), TreeNode(2))
    assert sol.isSubtree(r1, s1) is True, "Failed on example 1"

    # Test case 2: root = [3, 4, 5, 1, 2, None, None, None, None, 0], subRoot = [4, 1, 2] -> False
    r2 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0), None)), TreeNode(5))
    s2 = TreeNode(4, TreeNode(1), TreeNode(2))
    assert sol.isSubtree(r2, s2) is False, "Failed on example 2"

    # Test case 3: Single identical node -> True
    assert sol.isSubtree(TreeNode(1), TreeNode(1)) is True, "Failed on single identical node"

    # Test case 4: Empty subRoot -> True
    assert sol.isSubtree(TreeNode(1), None) is True, "Failed on empty subRoot"

    # Test case 5: Empty root with non-empty subRoot -> False
    assert sol.isSubtree(None, TreeNode(1)) is False, "Failed on empty root with non-empty subRoot"

    print("All test cases for Subtree of Another Tree passed!")
