'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1, n2, carry, tot, res = [], [], 0, 0, None
        while l1:
            n1.append(l1)
            l1 = l1.next
        while l2:
            n2.append(l2)
            l2 = l2.next
        while n1 or n2 or carry:
            if n1:
                tot += n1.pop().val
            if n2:
                tot += n2.pop().val
            if carry:
                tot += carry
                carry = 0
            carry, bit = divmod(tot, 10)
            cur = ListNode(bit)
            cur.next = res
            res = cur
            tot = 0
        return res
            