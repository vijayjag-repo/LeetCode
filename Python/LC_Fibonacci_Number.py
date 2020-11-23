class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        d = dict()
        d[0] = 0
        d[1] = 1
        for i in range(2,N+1):
            d[i] = d[i-1] + d[i-2]
        
        return(d[N])
        
