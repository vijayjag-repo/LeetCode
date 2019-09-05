class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if not g or not s:
            return(0)
        
        pt1 = len(g)-1
        pt2 = len(s)-1
        g.sort()
        s.sort()
        
        count = 0
        while(pt1>=0 and pt2>=0):
            if(g[pt1]<=s[pt2]):
                count+=1
                pt1-=1
                pt2-=1
            elif(g[pt1]>s[pt2]):
                pt1-=1
        
        return(count)
                
                
