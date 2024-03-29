"""
https://leetcode.com/problems/reverse-linked-list/
206. Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode,headref = 0) -> ListNode:
        curr = head
        headref = head
        if head == None:
            return headref
        first = curr
        rest = curr.next
        if rest == None:
            headref = curr
            return headref
        headref = self.reverseList(rest,headref)
        rest.next = first
        first.next = None
        return headref
        
        
        
