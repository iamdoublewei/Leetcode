'''
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

 

Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15
'''

class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        magics = [[[4,3,8],[9,5,1],[2,7,6]], 
                  [[8,3,4],[1,5,9],[6,7,2]],
                  [[2,7,6],[9,5,1],[4,3,8]],
                  [[6,7,2],[1,5,9],[8,3,4]],
                  [[4,9,2],[3,5,7],[8,1,6]],
                  [[8,1,6],[3,5,7],[4,9,2]],
                  [[2,9,4],[7,5,3],[6,1,8]],
                  [[6,1,8],[7,5,3],[2,9,4]]]
        l, w, cnt = len(grid), len(grid[0]), 0
        if l < 3 or w < 3:
            return 0
        for i in range(l - 2):
            for j in range(w - 2):
                if [x[j:j + 3] for x in grid[i:i + 3]] in magics:
                    cnt += 1
        return cnt