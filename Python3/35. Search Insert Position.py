class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, v in enumerate(nums):
            if v >= target:
                return i
        return len(nums)