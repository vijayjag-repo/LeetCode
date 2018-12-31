class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m]
        print(nums1)
        nums2[:] = nums2[:n]
        print(nums2)
        nums1[:] = nums1[:] + nums2[:]
        nums1.sort()
        
