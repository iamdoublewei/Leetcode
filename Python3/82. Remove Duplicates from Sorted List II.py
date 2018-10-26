'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        dummy = ListNode(0)
        dummy.next = head
        prev, val, duplicated = dummy, None, False
        while head:
            if val == head.val:
                duplicated = True
            elif val != None and val != head.val and not duplicated:
                prev.next.val = val
                prev = prev.next
                duplicated = False
            elif val != None and val != head.val and duplicated:
                duplicated = False
            val = head.val
            head = head.next       
        if not duplicated:
            prev.next.val = val
            prev = prev.next
        prev.next = None
        return dummy.next