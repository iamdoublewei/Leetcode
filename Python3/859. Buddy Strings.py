'''
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

 

Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false
 

Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
'''

class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A == B:
            return len(set(A)) != len(A)
        if len(A) == 1:
            return False
        d = []
        for i in range(len(A)):
            if A[i] != B[i]:
                d.append(i)
            if len(d) > 2:
                return False
        if len(d) != 2:
            return False
        if A[0:d[0]] + A[d[1]] + A[d[0] + 1:d[1]] + A[d[0]] + A[d[1] + 1:] == B:
            return True
        return False
        
        