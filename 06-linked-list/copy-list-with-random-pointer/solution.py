"""
Problem: Copy List with Random Pointer
LeetCode: 138 (https://leetcode.com/problems/copy-list-with-random-pointer/)
NeetCode 150: Copy Linked List with Random Pointer (https://neetcode.io/problems/copy-linked-list-with-random-pointer)
Difficulty: Medium
Pattern: Linked List (Hash Map / Two-Pass Clone)
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}
        curr = head
        while curr is not None:
            nodes[curr] = Node(curr.val)
            curr = curr.next
        nodes[None] = None

        curr = head
        while curr is not None:
            copy = nodes[curr]
            copy.next = nodes[curr.next]
            copy.random = nodes[curr.random]
            curr = curr.next
        return nodes[head]


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: empty list
    assert sol.copyRandomList(None) is None, "Failed on empty list"

    # Test case 2: single node with self random pointer
    n1 = Node(1)
    n1.random = n1
    c1 = sol.copyRandomList(n1)
    assert c1 is not n1, "Copy should be a new instance"
    assert c1.val == 1
    assert c1.random is c1, "Random pointer should point to copied node"
    assert c1.next is None

    # Test case 3: two nodes with cross links
    a = Node(1)
    b = Node(2)
    a.next = b
    a.random = b
    b.random = a
    c_a = sol.copyRandomList(a)
    assert c_a is not a
    assert c_a.next is not b
    assert c_a.val == 1 and c_a.next.val == 2
    assert c_a.random is c_a.next
    assert c_a.next.random is c_a

    print("All test cases for Copy List with Random Pointer passed!")
