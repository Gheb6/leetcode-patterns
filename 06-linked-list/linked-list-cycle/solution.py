"""
Problem: Linked List Cycle
LeetCode: 141 (https://leetcode.com/problems/linked-list-cycle/)
NeetCode 150: Linked List Cycle Detection (https://neetcode.io/problems/linked-list-cycle-detection)
Difficulty: Easy
Pattern: Linked List (Fast & Slow Pointers / Floyd's Cycle Finding)
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        if head == None:
            return False
        while fast is not None and fast.next is not None:
            slow = slow.next          
            fast = fast.next.next     
            if slow == fast:
                return True 
        return False     


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: List with cycle 3 -> 2 -> 0 -> -4 -> 2
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    assert sol.hasCycle(node1) is True, "Failed on list with cycle"

    # Test case 2: List without cycle 1 -> 2 -> None
    n1 = ListNode(1, ListNode(2))
    assert sol.hasCycle(n1) is False, "Failed on list without cycle"

    # Test case 3: Single node without cycle
    n_single = ListNode(1)
    assert sol.hasCycle(n_single) is False, "Failed on single node"

    # Test case 4: Empty list
    assert sol.hasCycle(None) is False, "Failed on empty list"

    print("All test cases for Linked List Cycle passed!")
