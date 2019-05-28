class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        a = ""
        b = ""
        
        for i in S:
            if(i!='#'):
                a+=i
            else:
                a = a[:-1]
        for i in T:
            if(i!='#'):
                b+=i
            else:
                b = b[:-1]
        return(a==b)
        
            
        
