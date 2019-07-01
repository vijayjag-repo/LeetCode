class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        
        Same as longest common substring.Draw table. Tushar Roy video.
        
        """
        dp = [[0 for i in range(len(B)+1)] for j in range(len(A)+1)]
        
        for i in range(1,len(A)+1):
            for j in range(1,len(B)+1):
                if(A[i-1]==B[j-1]):
                    dp[i][j] = dp[i-1][j-1] + 1
            
        return(max(max(i) for i in dp))
        
