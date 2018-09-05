class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for i, v in enumerate(s[::-1]):
            sum += pow(26, i) * (ord(v) - ord('A') + 1)
        return sum
