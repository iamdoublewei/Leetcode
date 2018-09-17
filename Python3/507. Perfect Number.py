'''
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)
'''

class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1: return False
        start, end, total, perfect = 2, num, 1, num
        while start <= end:
            mid = num // start
            if not num % start:
                if start == mid:
                    total += start
                else:
                    total += start + mid
            start += 1
            end = mid - 1
        if total == perfect:
            return True
        return False