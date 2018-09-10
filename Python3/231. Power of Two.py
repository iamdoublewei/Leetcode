'''
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 2E0 = 1
Example 2:

Input: 16
Output: true
Explanation: 2E4 = 16
Example 3:

Input: 218
Output: false
'''

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if not n: return False
        while n != 1:
            if n % 2:
                return False
            n //= 2
        return True
