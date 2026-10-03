"""
Problem: Merge Two Sorted Lists
LeetCode: 21 (https://leetcode.com/problems/merge-two-sorted-lists/)
NeetCode 150: Merge Two Sorted Linked Lists (https://neetcode.io/problems/merge-two-sorted-linked-lists)
Difficulty: Easy
Pattern: Linked List (Two Pointers / Simulation)
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        new_list = ListNode()
        head_newlist = new_list
        head_1 = list1
        head_2 = list2
        while head_1 != None and head_2 != None:
            if head_1.val <= head_2.val:
                head_newlist.next = head_1
                head_newlist = head_newlist.next
                head_1 = head_1.next
            else:
                head_newlist.next = head_2
                head_newlist = head_newlist.next
                head_2 = head_2.next
        if head_1 == None:
            head_newlist.next = head_2
            return new_list.next
        elif head_2 == None:
            head_newlist.next = head_1
            return new_list.next
        return new_list.next


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: [1, 2, 4] and [1, 3, 4] -> [1, 1, 2, 3, 4, 4]
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    merged = sol.mergeTwoLists(l1, l2)
    curr = merged
    for expected_val in [1, 1, 2, 3, 4, 4]:
        assert curr is not None and curr.val == expected_val
        curr = curr.next
    assert curr is None

    # Test case 2: Both empty
    assert sol.mergeTwoLists(None, None) is None

    # Test case 3: One empty list
    l4 = ListNode(0)
    res = sol.mergeTwoLists(None, l4)
    assert res is not None and res.val == 0 and res.next is None

    print("All test cases for Merge Two Sorted Lists passed!")
