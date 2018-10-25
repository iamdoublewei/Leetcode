'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n: return []
        res = set(['()'])
        for i in range(1, n):
            t = set()
            for r in res:
                for j in range(len(r)):
                    l = list(r)
                    l.insert(j, '()')
                    t.add(''.join(l))
                t.add(r + '()')
            res = t
        return list(res)