'''
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
'''

class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        diff = ord('a') - ord('A')
        r = ''
        for char in str:
            if char >= 'A' and char <= 'Z':
                r += chr(ord(char) + diff)
            else:
                r += char
        return r