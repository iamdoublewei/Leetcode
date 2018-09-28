'''
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False
'''

class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(0, int(c ** 0.5) + 1):
            d = c - i ** 2
            if d ** 0.5 == int(d ** 0.5):
                return True
        return False