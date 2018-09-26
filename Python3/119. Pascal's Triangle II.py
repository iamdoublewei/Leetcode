'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
'''

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if not rowIndex: return [1]
        res = [1,1]
        while len(res) - 1 < rowIndex:
            row = [1, 1]
            for i in range(len(res) - 1):
                row.insert(-1, res[i] + res[i + 1])
            res = row
        return res