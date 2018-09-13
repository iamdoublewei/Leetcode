'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
Refer to www.leetcode.com
'''

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        x = len(grid)
        y = len(grid[0])
        for i in range(x):
            for j in range(y):
                if grid[i][j]:
                    if i - 1 < 0 or not grid[i-1][j]:
                        res += 1
                    if i + 1 >= x or not grid[i+1][j]:
                        res += 1
                    if j - 1 < 0 or not grid[i][j-1]:
                        res += 1
                    if j + 1 >= y or not grid[i][j+1]:
                        res += 1
        return res

