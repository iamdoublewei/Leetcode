'''
You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation: 
The five points are show in the figure below. The red triangle is the largest.


Notes:

3 <= points.length <= 50.
No points will be duplicated.
 -50 <= points[i][j] <= 50.
Answers within 10^-6 of the true value will be accepted as correct.
'''

class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def area(x, y, z):
            return abs(x[0] * (y[1] - z[1]) + y[0] * (z[1] - x[1]) + z[0] * (x[1] - y[1])) * 0.5
        
        return max(area(*vertex) for vertex in itertools.combinations(points, 3))