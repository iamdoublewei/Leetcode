'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        d1, d2, res = {}, {}, []
        for v in p:
            d1[v] = d1.get(v, 0) + 1
        for i, v in enumerate(s):
            d2[v] = d2.get(v, 0) + 1
            if i >= len(p):
                if d2[s[i - len(p)]] == 1:
                    del d2[s[i - len(p)]]
                else:
                    d2[s[i - len(p)]] -= 1
            if d1 == d2:
                res.append(i - len(p) + 1)
        return res