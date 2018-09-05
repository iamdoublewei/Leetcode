#Approach 1: Brute Force
'''
class Solution:
    def twoSum(self, nums, target):
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                       return [i, j]
'''
#Approach 2: Hash Table	
			   
class Solution:
    def twoSum(self, nums, target):
        buffer = {}
        for i in range(len(nums)):
            if nums[i] in buffer:
                return [i, buffer[nums[i]]]
            buffer[target-nums[i]] = i
