class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = (x > 0) - (x < 0)
        res = int(str(s*x)[::-1])
        return s*res*(res < 2**31 - 1)