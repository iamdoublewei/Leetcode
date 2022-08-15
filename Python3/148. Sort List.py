'''
Given the head of a linked list, return the list after sorting it in ascending order.

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head):
        if head == None or head.next == None:
            return head
        
        def findmid(head):
            slow = fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
                
            return slow
        
        def merge(left, right):
            dummy = cur = ListNode()
            while left and right:
                if left.val <= right.val:
                    cur.next = left
                    left = left.next
                else:
                    cur.next = right
                    right = right.next
                cur = cur.next
                
            if left:
                cur.next = left
            if right:
                cur.next = right
                    
            return dummy.next
        
        mid = findmid(head)
        left = head
        right = mid.next
        mid.next = None
        left = self.sortList(left)
        right = self.sortList(right)
            
        return merge(left, right)
