'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows: return []
        if numRows == 1: return [[1]]
        res = [[1], [1,1]]
        while len(res) < numRows:
            row = [1, 1]
            for i in range(len(res[-1]) - 1):
                row.insert(-1, res[-1][i] + res[-1][i + 1])
            res.append(row)
        return res