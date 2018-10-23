'''
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
'''

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        print(nums)
        for i in range(0, len(nums) - 2, 3):
            if nums[i] == nums[i + 1] == nums[i + 2]:
                continue
            if nums[i] == nums[i + 1]:
                return nums[i + 2]
            elif nums[i] == nums[i + 2]:
                return nums[i + 1]
            elif nums[i + 1] == nums[i + 2]:
                return nums[i]
        return nums[-1]