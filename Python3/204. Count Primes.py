'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3: return 0
        t = [True] * n
        t[0] = t[1] = False
        for i in range(2, int(n**0.5) + 1):
            if t[i]:
                t[i*i:n:i] = [False] * len(t[i*i:n:i])
        return sum(t)