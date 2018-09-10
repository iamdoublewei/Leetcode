'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
1E2 + 9E2 = 82
8E2 + 2E2 = 68
6E2 + 8E2 = 100
1E2 + 0E2 + 0E2 = 1
'''

class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        lookup = {n}
        sum = 0
        while True:
            sum += pow(n % 10, 2)
            n //= 10
            if not n:
                if sum == 1:
                    return True
                if sum in lookup:
                    return False
                lookup.add(sum)
                n = sum
                sum = 0
