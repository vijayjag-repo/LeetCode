class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        
        Approach:
        
        Expand around center.
        Intuitive approach.
        """
        ans = ""
        def helper(s,beg,end):
            while(beg>=0 and end<len(s) and s[beg]==s[end]):
                beg-=1
                end+=1
            return(s[beg+1:end])
            
        for i in range(len(s)):
            temp = helper(s,i,i)
            ans = max(ans,temp,key=len)
            
            temp = helper(s,i,i+1)
            ans = max(ans,temp,key=len)
        
        return(ans)
        
        
