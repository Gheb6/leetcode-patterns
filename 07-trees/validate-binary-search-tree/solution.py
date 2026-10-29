"""
Problem: Validate Binary Search Tree (Valid Binary Search Tree)
LeetCode: 98 (https://leetcode.com/problems/validate-binary-search-tree/)
NeetCode 150: Valid Binary Search Tree (https://neetcode.io/problems/valid-binary-search-tree)
Difficulty: Medium
Pattern: Trees (BST Properties / DFS Range Validation)
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Iterative version

        # prev = - float('inf')
        # my_stack = []
        # curr = root
        # while curr or my_stack:
        #     while curr:
        #         my_stack.append(curr)
        #         curr = curr.left
        #     curr = my_stack.pop()
        #     if curr.val <= prev:
        #         return False
        #     else:
        #         prev = curr.val
        #     curr = curr.right
        # return True

        def valid(node, low = -float('inf'), high = float('inf')) -> bool:
            if not node:
                return True
            elif node.val >= high or node.val <= low:
                return False
            return valid(node.left, low, node.val) and valid(node.right, node.val, high)
        return valid(root)


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: Valid BST [2, 1, 3] -> True
    #     2
    #    / \
    #   1   3
    t1 = TreeNode(2, TreeNode(1), TreeNode(3))
    assert sol.isValidBST(t1) is True, "Failed on valid BST [2, 1, 3]"

    # Test case 2: Invalid BST [5, 1, 4, None, None, 3, 6] -> False
    #     5
    #    / \
    #   1   4
    #      / \
    #     3   6
    t2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert sol.isValidBST(t2) is False, "Failed on invalid BST [5, 1, 4, None, None, 3, 6]"

    # Test case 3: Invalid BST with duplicate values [2, 2, 2] -> False
    t3 = TreeNode(2, TreeNode(2), TreeNode(2))
    assert sol.isValidBST(t3) is False, "Failed on duplicate values"

    # Test case 4: Single node -> True
    assert sol.isValidBST(TreeNode(1)) is True, "Failed on single node"

    # Test case 5: Empty tree -> True
    assert sol.isValidBST(None) is True, "Failed on empty tree"

    print("All test cases for Validate Binary Search Tree passed!")

