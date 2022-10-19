'''
Given a string s, return the longest palindromic substring in s.

A string is called a palindrome string if the reverse of that string is the same as the original string.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(s):
            i = 0
            j = len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        if len(s) <= 1: 
            return s
        res = ''
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if j - i <= len(res):
                    continue              
                if check(s[i:j]) and j - i > len(res):
                    res = s[i:j]
        return res