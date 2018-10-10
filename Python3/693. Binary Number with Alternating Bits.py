'''
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.
Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.
Example 4:
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.
'''

class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math
        n = bin(n)[2:]
        times = math.ceil(len(n) / 2)
        alt1 = '01' * times
        if (len(alt1) > len(n)):
            alt1 = alt1[1:]
        alt2 = '10' * times
        if (len(alt2) > len(n)):
            alt2 = alt2[1:]
        return n == alt1 or n == alt2