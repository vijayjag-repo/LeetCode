class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        new = []
        i = 0
        while(i<len(A)):
            if(A[i]%2==0):
                new.append(A[i])
            i+=1
        
        i = 0
        while(i<len(A)):
            if(A[i]%2!=0):
                new.append(A[i])
            i+=1
        return(new)
            
        
        
