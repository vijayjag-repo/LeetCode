class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
    
        if(len(s)==0 or len(g)==0):
            return(0)
        g.sort()
        s.sort()
        j = 0
        count = 0
        for i in range(len(g)):
            while(j<len(s)):
                if(g[i]<=s[j]):
                    j+=1
                    count+=1
                    break
                else:
                    j+=1
        
        return(count)
                    
