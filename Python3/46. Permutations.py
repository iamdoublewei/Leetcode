'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs(nums, [])
        return self.res
    
    def dfs(self, nums, n):
        if not nums:
            self.res.append(n)
            return
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], n + [nums[i]])