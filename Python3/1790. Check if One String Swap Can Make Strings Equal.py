'''
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.
Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.
 

Constraints:

1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.
'''

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        c1 = -1
        c2 = -1
        s1 = list(s1)
        s2 = list(s2)
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if c1 == -1:
                    c1 = i
                elif c2 == -1:
                    c2 = i
                    break
        if c1 != -1 and c2 != -1:
            temp = s1[c1]
            s1[c1] = s1[c2]
            s1[c2] = temp
            if s1 == s2:
                return True
            else:
                return False
        else:
            return False