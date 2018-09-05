class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        lookup = {}
        for i, n in enumerate(nums):
            if n in lookup:
                if i - lookup[n] <= k:
                    return True
            lookup[n] = i
        return False
