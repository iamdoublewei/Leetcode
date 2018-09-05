class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        cur = m + n
        while n > 0:
            if m > 0 and nums1[m - 1] >= nums2[n - 1]:
                nums1[cur - 1] = nums1[m - 1]
                m -= 1
            elif nums2[n - 1] >= nums1[m - 1] or not m:
                nums1[cur - 1] = nums2[n - 1]
                n -= 1
            cur -= 1
