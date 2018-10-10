'''
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
'''

class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        position, res, last = [], [], None
        for i, v in enumerate(S):
            if v == C:
                position.append(i)
        for i in range(len(S)):
            if position and i == position[0]:
                res.append(0)
                last = position.pop(0)
            elif position:
                if last == None:
                    res.append(position[0] - i)
                else:
                    res.append(min(position[0] - i, i - last))
            elif not position:
                res.append(res[-1] + 1)
        return res
            