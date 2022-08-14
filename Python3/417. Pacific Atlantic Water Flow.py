'''
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Example 2:

Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        pac = set()
        alt = set()
        res = []
        
        def search(r, c, h, ocean):
            if r < 0 or c < 0 or r >= row or c >= col or (r, c) in ocean or heights[r][c] < h:
                return
                
            ocean.add((r, c))               
            search(r + 1, c, heights[r][c], ocean)
            search(r - 1, c, heights[r][c], ocean)
            search(r, c + 1, heights[r][c], ocean)
            search(r, c - 1, heights[r][c], ocean)

        for i in range(col):
            search(0, i, 0, pac)
            search(row - 1, i, 0, alt)
        for i in range(0, row):
            search(i, 0, 0, pac)
            search(i, col - 1, 0, alt)
        
        for i in pac:
            if i in alt:
                res.append(list(i))
                
        return res
                
        