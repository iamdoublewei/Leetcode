'''
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
'''

class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort = sorted(nums)
        start = 0
        end = len(nums) - 1
        if sort == nums:
            return 0
        for i in range(len(nums)):
            if nums[i] != sort[i]:
                start = i
                break
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != sort[i]:
                end = i
                break
        return end - start + 1