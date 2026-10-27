"""
Problem: Binary Tree Level Order Traversal
LeetCode: 102 (https://leetcode.com/problems/binary-tree-level-order-traversal/)
NeetCode 150: Binary Tree Level Order Traversal (https://neetcode.io/problems/level-order-traversal-of-binary-tree)
Difficulty: Medium
Pattern: Trees (BFS / Queue / Level-Order Traversal)
"""

from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        levels = deque([root])
        while levels:
            my_list = []
            for _ in range(len(levels)):
                curr = levels.popleft()
                my_list.append(curr.val)
                if curr.left:
                    levels.append(curr.left)
                if curr.right:
                    levels.append(curr.right)
            res.append(my_list)
        return res


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: Tree [3, 9, 20, None, None, 15, 7] -> [[3], [9, 20], [15, 7]]
    t1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert sol.levelOrder(t1) == [[3], [9, 20], [15, 7]], "Failed on example 1"

    # Test case 2: Single node [1] -> [[1]]
    t2 = TreeNode(1)
    assert sol.levelOrder(t2) == [[1]], "Failed on single node [1]"

    # Test case 3: Empty tree -> []
    assert sol.levelOrder(None) == [], "Failed on empty tree"

    # Test case 4: Skewed tree [1, 2, None, 3] -> [[1], [2], [3]]
    t4 = TreeNode(1, TreeNode(2, TreeNode(3), None), None)
    assert sol.levelOrder(t4) == [[1], [2], [3]], "Failed on skewed tree"

    print("All test cases for Binary Tree Level Order Traversal passed!")
