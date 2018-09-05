class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if len(str) == 0: return 0
        res = 0
        sign = 0

        for i, v in enumerate(str):
            if not sign:
                if v == '+':
                    sign = 1
                elif v == '-':
                    sign = -1
                elif v.isdigit():
                    sign = 1
                    res = res * 10 + int(v)
                else:
                    return 0
                continue
            if sign:
                if v.isdigit():
                    res = res * 10 + int(v)
                else:
                    break

        if sign * res >= 2147483647:
            return 2147483647
        elif sign * res <= -2147483648:
            return -2147483648
        else:
            return sign * res
