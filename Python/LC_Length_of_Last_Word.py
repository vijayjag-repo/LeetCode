class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = ""
        for i in range(len(s)-1,-1,-1):
            if(s[i]==' ' and ans==""):
                continue
            elif(s[i]!=' '):
                ans+=s[i]
            else:
                return(len(ans))
        
        if(len(ans)>0):
            return(len(ans))
        return(0)
