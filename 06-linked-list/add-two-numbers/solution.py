"""
Problem: Add Two Numbers
LeetCode: 2 (https://leetcode.com/problems/add-two-numbers/)
NeetCode 150: Add Two Numbers (https://neetcode.io/problems/add-two-numbers)
Difficulty: Medium
Pattern: Linked List (Simulation / Elementary Math / Dummy Node)
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_1 = l1
        curr_2 = l2
        head = ListNode(0)
        dummy = head
        carry = 0
        while curr_1 or curr_2 or carry != 0:
            val_1 = curr_1.val if curr_1 else 0
            val_2 = curr_2.val if curr_2 else 0
            summation = val_1 + val_2 + carry
            carry = summation // 10
            summation = summation % 10

            new_node = ListNode(summation)
            dummy.next = new_node
            dummy = dummy.next
            if curr_1:
                curr_1 = curr_1.next
            if curr_2:
                curr_2 = curr_2.next
        return head.next


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

    # Test case 1: 342 + 465 = 807 -> [2, 4, 3] + [5, 6, 4] = [7, 0, 8]
    l1 = from_list([2, 4, 3])
    l2 = from_list([5, 6, 4])
    assert to_list(sol.addTwoNumbers(l1, l2)) == [7, 0, 8], "Failed on [2, 4, 3] + [5, 6, 4]"

    # Test case 2: 0 + 0 = 0 -> [0] + [0] = [0]
    assert to_list(sol.addTwoNumbers(from_list([0]), from_list([0]))) == [0], "Failed on [0] + [0]"

    # Test case 3: 9999999 + 9999 = 10009998 -> [9,9,9,9,9,9,9] + [9,9,9,9] = [8,9,9,9,0,0,0,1]
    l1_3 = from_list([9, 9, 9, 9, 9, 9, 9])
    l2_3 = from_list([9, 9, 9, 9])
    assert to_list(sol.addTwoNumbers(l1_3, l2_3)) == [8, 9, 9, 9, 0, 0, 0, 1], "Failed on long lists with carries"

    print("All test cases for Add Two Numbers passed!")
