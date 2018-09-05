class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        lookup = {n}
        sum = 0
        while True:
            sum += pow(n % 10, 2)
            n //= 10
            if not n:
                if sum == 1:
                    return True
                if sum in lookup:
                    return False
                lookup.add(sum)
                n = sum
                sum = 0
