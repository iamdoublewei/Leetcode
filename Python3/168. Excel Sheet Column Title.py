'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
'''

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = ''
        while n:
            cur = n % 26
            n = n // 26
            if cur == 0:
                ret = 'Z' + ret
                n -= 1
            else:
                ret = chr(int(cur) + ord('A') - 1) + ret
        return ret
