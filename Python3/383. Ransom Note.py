'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r = {}
        m = {}
        for i in ransomNote:
            if i in r:
                r[i] += 1
            else:
                r[i] = 1
        for i in magazine:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        for i in r:
            if i in m:
                if r[i] > m[i]:
                    return False
            else:
                return False
        return True