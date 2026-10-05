"""
Problem: Reorder List
LeetCode: 143 (https://leetcode.com/problems/reorder-list/)
NeetCode 150: Reorder Linked List (https://neetcode.io/problems/reorder-linked-list)
Difficulty: Medium
Pattern: Linked List (Fast & Slow Pointers / Two Pointers)
"""

from typing import Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None:
            return None
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next
            fast = fast.next
        # median point is slow

        # Inverting the list second half
        curr = slow.next
        slow.next = None
        prev = None
        while curr != None:
            next_node = curr.next 
            curr.next = prev
            prev = curr
            curr = next_node
        dummy = head
        while dummy != None and prev != None:
            dummy_tmp = dummy.next
            prev_tmp = prev.next
            dummy.next = prev
            prev.next = dummy_tmp
            dummy = dummy_tmp
            prev = prev_tmp
        return None

