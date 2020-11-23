class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
    
        flag = 0
        value = 1
        while(value<N):
            if(N%(value)!=0):
                value+=1
            elif(N%(value)==0):
                if(flag==1):
                    flag = 0
                else:
                    flag = 1
                N = N - value
                value = 1
        
        return(flag==1)
        """
        
        return(N%2==0)
