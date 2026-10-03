"""
Problem: Reverse Linked List
LeetCode: 206 (https://leetcode.com/problems/reverse-linked-list/)
NeetCode 150: Reverse a Linked List (https://neetcode.io/problems/reverse-a-linked-list)
Difficulty: Easy
Pattern: Linked List (Iterative / Two Pointers)
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: 1 -> 2 -> 3 -> 4 -> 5 -> None -> 5 -> 4 -> 3 -> 2 -> 1 -> None
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    rev1 = sol.reverseList(head1)
    curr = rev1
    for expected_val in [5, 4, 3, 2, 1]:
        assert curr is not None and curr.val == expected_val
        curr = curr.next
    assert curr is None

    # Test case 2: 1 -> 2 -> None -> 2 -> 1 -> None
    head2 = ListNode(1, ListNode(2))
    rev2 = sol.reverseList(head2)
    assert rev2 is not None and rev2.val == 2
    assert rev2.next is not None and rev2.next.val == 1
    assert rev2.next.next is None

    # Test case 3: Empty list
    assert sol.reverseList(None) is None

    print("All test cases for Reverse Linked List passed!")
