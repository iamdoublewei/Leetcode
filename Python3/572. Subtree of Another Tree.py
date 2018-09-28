'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
'''

class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.traversal(s, t)

    def isSame(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return t1.val == t2.val and self.isSame(t1.left, t2.left) and self.isSame(t1.right, t2.right)
    
    def traversal(self, s, t):
        if not t:
            return True
        if not s:
            return False
        if s.val == t.val and self.isSame(s, t):
            return True
        else:
            return self.traversal(s.left, t) or self.traversal(s.right, t)
    