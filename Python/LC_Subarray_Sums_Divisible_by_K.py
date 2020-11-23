class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        
        Approach:
        Similar to Subarray sums equal to K.
        """
        d = dict()
        d[0] = 1
        sums = 0
        count = 0
        
        for i in range(len(A)):
            sums = (sums + A[i])%K
            if(sums in d):
                count+=d[sums]
                d[sums]+=1
            else:
                d[sums] = 1
        return(count)
