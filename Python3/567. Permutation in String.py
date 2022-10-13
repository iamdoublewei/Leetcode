'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(list(s1))
  
        for i in range(len(s2)):
            if i + len(s1) - 1 < len(s2):
                if s1 == sorted(s2[i:i+len(s1)]):
                    return True
            else:
                break

        return False