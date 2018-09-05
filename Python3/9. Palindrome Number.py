class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        div = 1
        while x / div >= 10:
            div *= 10
        while x:
            highest = int(x / div)
            lowest = x % 10
            if highest != lowest:
                return False
            x = int((x % div) / 10)
            div /= 100
        return True