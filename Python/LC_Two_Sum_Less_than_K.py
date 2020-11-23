class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        
        Approach:
        
        Two pointer approach.
        """
        maximum = -1
        A.sort()
        i = 0
        j = len(A)-1
        while(i<j):
            if(A[i]+A[j]<K):
                maximum = max(maximum,A[i]+A[j])
                i+=1
            else:
                j-=1
                
        return(maximum)
        
