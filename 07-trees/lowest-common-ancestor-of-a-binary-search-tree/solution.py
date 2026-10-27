"""
Problem: Lowest Common Ancestor of a Binary Search Tree
LeetCode: 235 (https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
NeetCode 150: Lowest Common Ancestor in Binary Search Tree (https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree)
Difficulty: Medium
Pattern: Trees (BST Properties / Binary Search Tree Traversal)
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr
        return None


if __name__ == "__main__":
    sol = Solution()

    # Construct BST:
    #         6
    #       /   \
    #      2     8
    #     / \   / \
    #    0   4 7   9
    #       / \
    #      3   5
    n0 = TreeNode(0)
    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n4 = TreeNode(4, n3, n5)
    n2 = TreeNode(2, n0, n4)
    n7 = TreeNode(7)
    n9 = TreeNode(9)
    n8 = TreeNode(8, n7, n9)
    root = TreeNode(6, n2, n8)

    # Test case 1: LCA of 2 and 8 is 6
    assert sol.lowestCommonAncestor(root, n2, n8).val == 6, "Failed on LCA(2, 8)"

    # Test case 2: LCA of 2 and 4 is 2 (a node can be a descendant of itself)
    assert sol.lowestCommonAncestor(root, n2, n4).val == 2, "Failed on LCA(2, 4)"

    # Test case 3: LCA of 3 and 5 is 4
    assert sol.lowestCommonAncestor(root, n3, n5).val == 4, "Failed on LCA(3, 5)"

    # Test case 4: Small BST [2, 1], p = 2, q = 1 -> 2
    r_small = TreeNode(2, TreeNode(1), None)
    assert sol.lowestCommonAncestor(r_small, r_small, r_small.left).val == 2, "Failed on small BST"

    print("All test cases for Lowest Common Ancestor of a BST passed!")
