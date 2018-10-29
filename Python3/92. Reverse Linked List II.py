'''
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        # caculate prev to be node before reverse
        for _ in range(m - 1):
            prev = prev.next
        start = first = prev.next
        second = prev
        for i in range(n - m + 1):
            if not i:
                first = first.next
                second = second.next
            else:
                next = first.next
                first.next = second
                second = first
                first = next
        start.next = first
        prev.next = second
        return dummy.next