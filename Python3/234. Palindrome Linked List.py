'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Reverse the first half of the LinkedList
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        l, h = 0, head
        while h:
            l += 1
            h = h.next
        h, pre = head, None
        for i in range(l//2):
            cur = h.next
            h.next = pre
            pre = h
            h = cur
        if l % 2:
            h = h.next
        while h or pre:
            if h.val != pre.val:
                return False
            h = h.next
            pre = pre.next
        return True