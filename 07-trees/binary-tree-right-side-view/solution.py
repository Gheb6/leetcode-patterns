"""
Problem: Binary Tree Right Side View
LeetCode: 199 (https://leetcode.com/problems/binary-tree-right-side-view/)
NeetCode 150: Binary Tree Right Side View (https://neetcode.io/problems/binary-tree-right-side-view)
Difficulty: Medium
Pattern: Trees (BFS / Level Order / Queue)
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        levels = deque()
        levels.append(root)
        while levels:
            level_size = len(levels)
            for i in range(level_size):
                node = levels.popleft()
                if node.left:
                    levels.append(node.left)
                if node.right:
                    levels.append(node.right)
                if i == level_size - 1:
                    res.append(node.val)
        return res


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: [1, 2, 3, None, 5, None, 4] -> [1, 3, 4]
    #       1            <--- 1
    #     /   \
    #    2     3         <--- 3
    #     \     \
    #      5     4       <--- 4
    t1 = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    assert sol.rightSideView(t1) == [1, 3, 4], "Failed on example 1"

    # Test case 2: [1, None, 3] -> [1, 3]
    t2 = TreeNode(1, None, TreeNode(3))
    assert sol.rightSideView(t2) == [1, 3], "Failed on example 2"

    # Test case 3: Empty tree -> []
    assert sol.rightSideView(None) == [], "Failed on empty tree"

    # Test case 4: Left branch deeper than right branch
    #        1           <--- 1
    #      /   \
    #     2     3        <--- 3
    #    /
    #   4                <--- 4
    #  /
    # 5                  <--- 5
    t4 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5), None), None), TreeNode(3))
    assert sol.rightSideView(t4) == [1, 3, 4, 5], "Failed when left branch is deeper"

    print("All test cases for Binary Tree Right Side View passed!")

