class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for i, v in enumerate(s):
            if i+1 < len(s) and d[v] < d[s[i+1]]:
                res -= d[v]
            else:
                res += d[v]
        return res