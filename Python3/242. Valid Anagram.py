'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lookup = {}
        for letter in s:
            if letter in lookup:
                lookup[letter] += 1
            else:
                lookup[letter] = 1
        for letter in t:
            if letter in lookup:
                lookup[letter] -= 1
                if lookup[letter] == 0:
                    del lookup[letter]
            else:
                return False
        if len(lookup) == 0:
            return True
        else:
            return False