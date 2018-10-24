'''
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
'''

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = ''
        if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
            sign = '-'
        dividend, divisor, cur, res = list(str(abs(dividend))), abs(divisor), 0, 0
        while dividend:
            cur = int(str(cur) + dividend.pop(0))
            res = int(str(res) + '0')
            for i in range(1, 10):
                if cur - divisor >= 0:
                    cur -= divisor
                    res += 1
        res = int(sign + str(res))
        if res > 2147483647:
            return 2147483647
        return res