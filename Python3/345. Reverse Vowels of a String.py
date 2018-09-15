'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        dic = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        index = []
        values = []
        for i, v in enumerate(s):
            if v in dic:
                index.append(i)
                values.append(v)
        for i, v in enumerate(reversed(index)):
            s[v] = values[i]
        return ''.join(s)