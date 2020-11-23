class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        char = list(s.strip())
        
        if(not char):
            return(0)
        if(char[0]=='-'):
            sign = -1
        else:
            sign = +1
        
        if(char[0]=='-' or char[0]=='+'):
            del char[0]
        
        i = 0
        ret = 0
        while(i<len(char) and char[i].isdigit()):
            ret = (ret*10) + ord(char[i])-ord('0')
            i+=1
        
        if(sign*ret>0):
            return(min(sign*ret,2**31-1))
        else:
            return(max(sign*ret,-2**31))
