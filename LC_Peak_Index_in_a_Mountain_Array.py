class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        Alternatively, you can even do 
            return(A.index(max(A)))
        Only for this problem though because we know that there is only one mountain and the max element is a part of it.
        """
        for i in range(1,len(A)-1):
            if(A[i]>A[i-1] and A[i]>A[i+1]):
                return(i)
                
        
