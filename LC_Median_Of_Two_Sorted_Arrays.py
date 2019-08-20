class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        Approach:
        
        Tushar Roy Video.
        """
        n1,n2 = len(nums1),len(nums2)
        if(n1<n2):
            return(self.findMedianSortedArrays(nums2,nums1))
        
        low,high = 0,n2*2
        while(low<=high):
            mid2 = (low+high)/2
            mid1 = n1+n2 - mid2
            
            l1 = float('-inf') if mid1==0 else nums1[(mid1-1)/2]
            l2 = float('-inf') if mid2==0 else nums2[(mid2-1)/2]
            r1 = float('inf') if mid1==n1*2 else nums1[(mid1)/2]
            r2 = float('inf') if mid2==n2*2 else nums2[(mid2)/2]
            
            if(l1>r2):
                low = mid2 + 1
            elif(l2>r1):
                high = mid2 - 1
            else:
                return(float(max(l1,l2)+min(r1,r2))/2)
        return(-1)
            
        
            
