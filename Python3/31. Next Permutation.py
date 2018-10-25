'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                t = i
                for j in range(i, len(nums)):
                    if nums[j] > nums[i - 1] and nums[j] < nums[t]:
                        t = j
                nums[i - 1], nums[t] = nums[t], nums[i - 1]
                nums[i:] = sorted(nums[i:])
                return
        nums.sort()