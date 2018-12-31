data = dict()
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
       
        if n in data:
            return(data[n])
        if(n==1):
            data[1] = 1
            return(1)
        if(n==2):
            data[2] = 2
            return(2)
        else:
            result = self.climbStairs(n-1) + self.climbStairs(n-2)
            data[n] = result
            return(result)
        
        
