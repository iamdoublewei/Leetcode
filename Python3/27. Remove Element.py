class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        head = 0
        toe = len(nums) - 1
        while (head <= toe):
            if nums[head] == val:
                nums[head] = nums[toe]
                toe -= 1
            else:
                head += 1
        return head