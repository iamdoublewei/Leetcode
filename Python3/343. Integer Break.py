'''
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.
'''

class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 3: return 2
        mx = 1
        for i in range(2, n):
            div, mod = divmod(n, i)
            if mod and mod == 1:
                mx = max(mx, (i + mod) * i ** (div - 1))
            elif mod:
                mx = max(mx, mod * i ** div)
            else:
                mx = max(mx, i ** div)
        return mx