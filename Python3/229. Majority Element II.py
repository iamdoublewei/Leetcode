'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
'''

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        nums.sort()
        res, cnt, cur, limit = [], 0, nums[0], len(nums) / 3
        for num in nums:
            if num == cur:
                cnt += 1
            else:
                cur = num
                cnt = 1
            if cnt > limit and not res or cnt > limit and cur != res[-1]:
                res.append(cur)
        return res