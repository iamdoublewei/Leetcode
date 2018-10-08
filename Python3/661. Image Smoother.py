'''
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].
'''

class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        l, w = len(M), len(M[0])
        res = [[0] * w for _ in range(l)]
        for i in range(l):
            for j in range(w):
                tot = []
                if i-1 >= 0: tot.append(M[i-1][j])
                if j-1 >= 0: tot.append(M[i][j-1])
                if i-1 >= 0 and j-1 >= 0: tot.append(M[i-1][j-1])
                if i+1 < l: tot.append(M[i+1][j])
                if j+1 < w: tot.append(M[i][j+1])
                if i+1 < l and j+1 < w: tot.append(M[i+1][j+1])
                if i+1 < l and j-1 >= 0: tot.append(M[i+1][j-1])
                if i-1 >= 0 and j+1 < w: tot.append(M[i-1][j+1])
                tot.append(M[i][j])
                res[i][j] = sum(tot) // len(tot)
        return res