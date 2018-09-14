'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
'''

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <=0: return False
        dic = {4**0, 4**1, 4**2, 4**3, 4**4, 4**5, 4**6, 4**7, 4**8, 4**9, 4**10, 4**11, 4**12, 4**13, 4**14, 4**15}
        if num not in dic:
            return False
        return True