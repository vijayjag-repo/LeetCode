class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if(len(A)!=len(B)):
            return(False)
        if(len(A)==len(B)==0):
            return(True)
        i = 0
        while(i<len(A)):
            if((A[i:] + A[:i])==B):
                return(True)
            else:
                i+=1
        return(False)
        
