'''
200. Number of Islands
Medium

15150

354

Add to List

Share
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''
			   
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:                
        island = 0
        m = len(grid)
        n = len(grid[0])
        def search(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] != '1':
                return
            grid[row][col] = '2'
            search(row-1, col)
            search(row+1, col)
            search(row, col-1)
            search(row, col+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    island += 1
                    search(i, j)
                
        return island
                