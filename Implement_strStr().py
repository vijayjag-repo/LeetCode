class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        Input: haystack = "hello", needle = "ll"
        Output: 2
        """
        if(len(haystack)==0 and len(needle)==0):
            return(0)
        elif(len(haystack)==0 and len(needle)>=1):
            return(-1)
        elif(len(haystack)>=1 and len(needle)==0):
            return(0)
        result = haystack.find(needle)
        return(result)
        
        
            
        
