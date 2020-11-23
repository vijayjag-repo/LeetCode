class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        
        """
        flag = False
        remainder,ans = 0,0
        if(x<0):
            x = 0 - x
            flag = True
        
        while(x>0):
            remainder = x % 10
            ans = (ans*10) + remainder
            x/=10
        if(flag):
            ans = 0 - ans
        return(0 if abs(ans)>(2**31)-1 else ans)
