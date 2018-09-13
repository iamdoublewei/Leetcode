'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
'''

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        s = '1'
        t = ''
        cnt = 0
        for _ in range(n-1):
            t = s[0]
            for i in s:
                if i == t:
                    cnt += 1
                else:
                    res += str(cnt) + t
                    t = i 
                    cnt = 1
            if t:
                res += str(cnt) + t
                cnt = 0
            s = res
            res = ''
        return s