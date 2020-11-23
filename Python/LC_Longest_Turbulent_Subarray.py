class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        
        Approach:
        
        Walk through the code.
        """
        if not A:
            return 0
        local_max = global_max = 0
        
        for i in range(len(A)):
            if(i>=2 and (A[i-2]>A[i-1]<A[i] or A[i-2]<A[i-1]>A[i])):
                local_max+=1
            elif(i>=1 and A[i-1]!=A[i]):
                local_max = 2
            else:
                local_max = 1
            
            global_max = max(global_max,local_max)
    
        return global_max
