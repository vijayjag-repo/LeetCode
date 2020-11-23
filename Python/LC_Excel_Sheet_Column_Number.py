class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        ans = 0
        y = 1
        for i in range(len(s)-1,-1,-1):
            if(i==len(s)-1):
                ans+=ord(s[i])-65+1
            else:
                ans+= ((26**y)*(ord(s[i])-65+1))
                y+=1
        return(ans)
