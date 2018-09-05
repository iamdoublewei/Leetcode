class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if not n: return False
        while n != 1:
            if n % 2:
                return False
            n //= 2
        return True
