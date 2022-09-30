'''
Given an integer n, add a dot (".") as the thousands separator and return it in string format.

 

Example 1:

Input: n = 987
Output: "987"
Example 2:

Input: n = 1234
Output: "1.234"
 

Constraints:

0 <= n <= 231 - 1
'''

class Solution:
    def thousandSeparator(self, n: int) -> str:
        res = ''
        cnt = 0
        
        for c in str(n)[::-1]:
            if cnt == 3:
                res = '.' + res
                cnt = 0
            res = c + res
            cnt += 1
            
        return res