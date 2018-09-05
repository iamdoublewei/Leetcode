class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lines = [''] * numRows
        size = numRows * 2 - 2  # each sub component size

        if numRows <= 1 or numRows >= len(s):
            return s

        for i, v in enumerate(s):
            cur = i % size
            if cur < numRows:
                lines[cur] += v
            else:
                lines[size - cur] += v
        return ''.join(lines)
