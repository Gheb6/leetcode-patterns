"""
Problem: Remove Nth Node From End of List
LeetCode: 19 (https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
NeetCode 150: Remove Node From End of Linked List (https://neetcode.io/problems/remove-node-from-end-of-linked-list)
Difficulty: Medium
Pattern: Linked List (Two Pointers / Fast & Slow / Dummy Node)
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        for _ in range(n):
            right = right.next
            
        while right is not None:
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy.next


if __name__ == "__main__":
    def from_list(vals):
        dummy = ListNode(0)
        curr = dummy
        for v in vals:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next

    def to_list(head):
        res = []
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

    sol = Solution()

    # Test cases
    assert to_list(sol.removeNthFromEnd(from_list([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5], "Failed on [1, 2, 3, 4, 5] n=2"
    assert to_list(sol.removeNthFromEnd(from_list([1]), 1)) == [], "Failed on [1] n=1"
    assert to_list(sol.removeNthFromEnd(from_list([1, 2]), 1)) == [1], "Failed on [1, 2] n=1"
    assert to_list(sol.removeNthFromEnd(from_list([1, 2]), 2)) == [2], "Failed on [1, 2] n=2 (head removal)"
    print("All test cases for Remove Nth Node From End of List passed!")
