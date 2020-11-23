class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        new = ""
        while(A and B):
            if(A>B):
                new = new + 'aab'
                A-=2
                B-=1
            elif(B>A):
                new = new + 'bba'
                B-=2
                A-=1
            else:
                new = new + 'ab'
                A-=1
                B-=1
        
        i = 0
        j = 0
        while(i<A):
            new = new + 'a'
            i+=1
        while(j<B):
            new = new + 'b'
            j+=1
        return(new)
            
    
            
                    
