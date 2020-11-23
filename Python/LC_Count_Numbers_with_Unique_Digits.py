class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        
        Pretty solution. Simple.
        """
        choices = [9,9,8,7,6,5,4,3,2,1]
        ans = 1
        product = 1
        
        for i in range(n):
            product*=choices[i]
            ans+= product
        
        return(ans)
            
        
