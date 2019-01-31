class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse = 0
        remainder = 0
        flag = False
        if(x < 0):
            x = 0 - x
            flag = True
        while(x > 0):
            remainder = x%10
            reverse = (reverse*10) + remainder
            x = x//10
        if(flag):
            reverse = 0 - reverse
        if((reverse > 2147483647) or (reverse < -2147483648)):
            return(0)
    
        return(reverse)
        
        
