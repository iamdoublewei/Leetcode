'''
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.values = []
        self.traversal(root)
        self.values.sort()
        self.addSum(root)
        return root
        
    def traversal(self, root):
        if not root:
            return 
        self.values.append(root.val)
        self.traversal(root.left)
        self.traversal(root.right)
        
    def addSum(self, root):
        if not root:
            return
        root.val = sum(self.values[self.values.index(root.val):])
        self.addSum(root.left)
        self.addSum(root.right)