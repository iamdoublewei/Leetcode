class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = ''
        while n:
            cur = n % 26
            n = n // 26
            if cur == 0:
                ret = 'Z' + ret
                n -= 1
            else:
                ret = chr(int(cur) + ord('A') - 1) + ret
        return ret
