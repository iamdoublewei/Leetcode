'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs(nums, [])
        return list(set(tuple(x) for x in self.res))
    
    def dfs(self, nums, n):
        if not nums:
            self.res.append(n)
            return
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], n + [nums[i]])