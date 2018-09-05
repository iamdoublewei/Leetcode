class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """      
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if carry:
                digits[i] += 1
                carry = 0
            if digits[i] >= 10:
                carry, digits[i] = 1, 0
            else:
                return digits
        if carry:
            digits.insert(0, 1)
        return digits