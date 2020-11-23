class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p2 = n-1
        p = m+n-1
        
        while(p1>=0 and p2>=0):
            if(nums1[p1]<nums2[p2]):
                nums1[p] = nums2[p2]
                p2-=1
                p-=1
            else:
                nums1[p] = nums1[p1]
                p1-=1
                p-=1
        # Incase all the elements of nums1 are greater than nums2, the nums1 array will have only nums1 elements in the end.
        # So, we just have to put the elements present in nums2 to nums1.
        # In other words, all elements of nums2 are lesser than the least element of nums1. So we put nums2 infront of the nums1 elements.
        nums1[:p2+1] = nums2[:p2+1]
        
