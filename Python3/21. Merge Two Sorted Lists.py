'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Original
# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         dummy = ListNode(0)
#         head = dummy
#         while l1 and l2:
#             head.next = ListNode(0)
#             head = head.next
#             if l1.val <= l2.val:
#                 head.val = l1.val
#                 l1 = l1.next
#             elif l1.val > l2.val:
#                 head.val = l2.val
#                 l2 = l2.next
#         if l1:
#             head.next = l1
#         if l2:
#             head.next = l2
#         return dummy.next

#Improved beat 100%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        head = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            elif l1.val > l2.val:
                head.next = l2
                l2 = l2.next
            head = head.next

        if l1:
            head.next = l1
        if l2:
            head.next = l2
        return dummy.next