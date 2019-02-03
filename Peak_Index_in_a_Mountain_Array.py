class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        value = 0
        if(len(A)>=3):
            for i in range(len(A)-1):
                if(A[i]>A[i+1]):
                    value = i
                    break
        return(value)
                
        
