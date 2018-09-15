'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''

#Original
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.replace(" ", "")
        if not s: return True
        res = ''
        s = list(s.lower())
        for cur in s:
            if cur >='a' and cur <= 'z' or cur >= '0' and cur <= '9':
                res += cur
        return res == ''.join(reversed(res))

#Improved:
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = ''
        for cur in s.lower():
            if cur.isalnum():
                res += cur
        return res == ''.join(reversed(res))

