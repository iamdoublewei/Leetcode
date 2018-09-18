'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
'''

class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1: return True
        start, end = 0, num
        while start <= end:
            mid = (start + end) // 2
            t = mid * mid
            if t == num:
                return True
            elif t > num:
                end = mid - 1
            else:
                start = mid + 1
        return False