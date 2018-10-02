'''
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
'''

class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        cnt = 0
        for i in points:
            dic = {}
            for j in points:
                if i == j:
                    continue
                distance = (i[0] - j[0])**2 + (i[1] - j[1])**2
                if distance in dic:
                    cnt += dic[distance]
                    dic[distance] += 1
                else:
                    dic[distance] = 1
        return cnt * 2