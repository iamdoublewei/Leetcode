'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        lr, lc = len(matrix), len(matrix[0])
        cnt = lr * lc
        res, r, c, d = [], 0, 0, 0
        while cnt:
            res.append(matrix[r][c])
            matrix[r][c] = None
            if r + dirs[d][0] < 0 or r + dirs[d][0] >= lr or c + dirs[d][1] < 0 or c + dirs[d][1] >= lc or matrix[r + dirs[d][0]][c + dirs[d][1]] == None:
                d = (d + 1) % 4
            r += dirs[d][0]
            c += dirs[d][1]
            cnt -= 1
        return res