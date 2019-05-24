class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        final = []
        if not s:
            return(0)
        for i in range(len(s)):
            if(s[i]!=' '):
                count+=1
            else:
                final.append(count)
                count = 0
        final.append(count)
        final = final[::-1]
        for j in final:
            if(j!=0):
                return(j)
        return(0)    
        
