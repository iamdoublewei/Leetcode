'''
Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:
Input: N = 10
Output: 9
Example 2:
Input: N = 1234
Output: 1234
Example 3:
Input: N = 332
Output: 299
Note: N is an integer in the range [0, 10^9].
'''

class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        num = []
        N = list(str(N))
        for i in range(len(N)):
            for j in range(1, 11):
                if j == 10:
                    num.append('9')
                if num + [str(j)] * (len(N) - i) > N:
                    num.append(str(j - 1))
                    break
        return int(''.join(num))